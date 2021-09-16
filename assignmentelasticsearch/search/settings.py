import os

API_VERSION = '1.0'

ES_HOST = os.getenv("ES_HOST", "127.0.0.1")
ES_PORT = os.getenv("ES_PORT", 9200)
ES_USER = os.getenv("ES_USER")
ES_PWD = os.getenv("ES_PWD")

INDEX = os.getenv("index", "products")