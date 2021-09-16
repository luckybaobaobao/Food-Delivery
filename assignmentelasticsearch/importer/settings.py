import os

MATHEM_PRODUCTS_URL = os.getenv('MATHEM_PRODUCTS_URL')
BATCH_SIZE = int(os.getenv('BATCH_SIZE', 10))

MAX_TRY = int(os.getenv('MAX_TRY', 3))
TIMEOUT = int(os.getenv('TIMEOUT', 10))

INDEX_PREFIX = os.getenv('INDEX_PREFIX', 'products')
ALIAS = os.getenv('ALIAS', 'products')

ES_HOST = os.getenv("ES_HOST", "127.0.0.1")
ES_PORT = os.getenv("ES_PORT", 9200)
ES_USER = os.getenv("ES_USER")
ES_PWD = os.getenv("ES_PWD")

