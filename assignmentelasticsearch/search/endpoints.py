from assignmentelasticsearch.search import app
from assignmentelasticsearch.search.functions import find_most_expensive, find_greenest, find_allweeklong


@app.endpoint("most-expensive")
def mostexpensive():
    return {"most expensive 10 product": find_most_expensive()}


@app.endpoint("greenest")
def greenest():
    return {"greenest": find_greenest()}


@app.endpoint("all-week-long")
def allweeklong():
    return {"all-week-long": find_allweeklong()}
