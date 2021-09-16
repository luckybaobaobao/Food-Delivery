from assignmentelasticsearch.search import es, settings


def marsha_result(response):
    hits = response.get('hits', {}).get('hits', [])
    return [{'name': hit.get('_source', {}).get('name', None),
             'price': hit.get('_source', {}).get('price', None),
             'department': hit.get('_source', {}).get('department', None),
             'url': hit.get('_source', {}).get('url', None)} for hit in hits]


def find_most_expensive():
    query = {
        "size": 10,
        "sort": [{"price": "desc"}],
        "query": {"match_all": {}}
    }
    response = es.search(body=query, index=settings.INDEX)
    return marsha_result(response)


def find_greenest():
    query = {
        "size": 10,
        "query": {
            "match": {"preferences.dietary.name.keyword": "Vegansk"}
        }
    }
    response = es.search(body=query, index=settings.INDEX)
    return marsha_result(response)


def find_allweeklong():
    query = {
        "size": 10,
        "query": {
            "bool": {
                "must_not": [{
                    "exists": {
                        "field": "deliverableweekdays"
                    }
                }]
            }
        }
    }
    response = es.search(body=query, index=settings.INDEX)
    return marsha_result(response)
