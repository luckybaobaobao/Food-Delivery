

def convert_products(products):
    converted_products = []
    for product in products:
        converted_products.append({
            'id': product.get('id', None),
            'name': product.get('name', None),
            'department': product.get('department', {}),
            'price': int(product.get('price', 0)),
            'preferences': product.get('preferences', None),
            'url': product.get('url', None),
            'deliverableweekdays': product.get('deliverableWeekdays', [])
        })
    return converted_products