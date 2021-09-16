from ssl import create_default_context

import certifi
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from assignmentelasticsearch.importer import settings
from assignmentelasticsearch.importer.convert import convert_products
from assignmentelasticsearch.importer.loader import load_products
from assignmentelasticsearch.importer.mappings import mappings


if settings.ES_USER and settings.ES_PWD:
    context = create_default_context(cafile=certifi.where())
    es = Elasticsearch([settings.ES_HOST], port=settings.ES_PORT,
                       use_ssl=True, scheme='https', ssl_context=context,
                       http_auth=(settings.ES_USER, settings.ES_PWD), timeout=60)
else:
    es = Elasticsearch([{'host': settings.ES_HOST, 'port': settings.ES_PORT}], timeout=60)


def setup_index():
    from datetime import datetime
    new_index_name = "%s-%s" % (settings.INDEX_PREFIX, datetime.now().strftime('%Y%m%d-%H%M'))
    es.indices.create(index=new_index_name, body=mappings)
    return new_index_name


def put_alias(new_index):
    return es.indices.put_alias(index=new_index, name=settings.ALIAS)


def bulk_generator(documents, index_name):
    for document in documents:
        doc_id = document.get('id')
        yield {'_index': index_name,
               '_id': doc_id,
               '_source': document}


def bulk_index(products, index_name):
    action_iterator = bulk_generator(products, index_name)
    result = bulk(es, action_iterator)
    return result[0]


def main():
    new_index = setup_index()
    products, length = load_products()
    batch_size = settings.BATCH_SIZE
    for nr in range(length // batch_size + 1):
        if (nr + 1) * batch_size <= length:
            converted_products = convert_products(products[nr * batch_size: (nr + 1) * batch_size])
        else:
            converted_products = convert_products(products[nr * batch_size:])
        bulk_index(converted_products, new_index)
    put_alias(new_index)
    print('finished')


main()

