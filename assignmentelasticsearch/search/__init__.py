import certifi
from elasticsearch import Elasticsearch
from flask import Flask
from ssl import create_default_context
from assignmentelasticsearch.search import settings


app = Flask(__name__)

if settings.ES_USER and settings.ES_PWD:
    context = create_default_context(cafile=certifi.where())
    es = Elasticsearch([settings.ES_HOST], port=settings.ES_PORT,
                       use_ssl=True, scheme='https', ssl_context=context,
                       http_auth=(settings.ES_USER, settings.ES_PWD), timeout=60)
else:
    es = Elasticsearch([{'host': settings.ES_HOST, 'port': settings.ES_PORT}], timeout=60)


from assignmentelasticsearch.search.endpoints import mostexpensive, greenest, allweeklong

app.add_url_rule("/most-expensive", endpoint="most-expensive")
app.add_url_rule("/greenest", endpoint="greenest")
app.add_url_rule("/all-week-long", endpoint="all-week-long")

