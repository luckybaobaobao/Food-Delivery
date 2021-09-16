import time

from assignmentelasticsearch.importer import settings
import requests


def load_products():
    content = get_with_tries()
    products = []
    length = 0
    if content:
        products = content.get('products', [])
        length = len(products)
    return products, length


def get_with_tries():
    fail = 0
    fail_max = settings.MAX_TRY
    url = settings.MATHEM_PRODUCTS_URL
    timeout = settings.TIMEOUT
    while True:
        try:
            response = requests.get(url, timeout=timeout)
            return response.json()
        except requests.exceptions.RequestException as e:
            fail += 1
            time.sleep(0.3)
            if fail >= fail_max:
                raise e
