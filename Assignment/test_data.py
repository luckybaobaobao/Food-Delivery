product_list_1 = [
    {'productId': '1',
     'name': 'watermelon',
     'deliveryDays': [0, 1, 2, 4, 5],
     'productType': 'external',
     'daysInAdvance': 5
     },
    {'productId': '2',
     'name': 'bread',
     'deliveryDays': [2, 3, 4, 5],
     'productType': 'normal',
     'daysInAdvance': 2
     },
    {'productId': '3',
     'name': 'strawberry',
     'deliveryDays': [2, 3, 4, 6],
     'productType': 'temporary',
     'daysInAdvance': 3
     }
]


expect_delivery_response_for_product_list_1 = {
 'status': 'success',
 'data': {'deliveryDates': [
  {'postalCode': '11252',
   'deliveryDate': '2021-09-17T00:00:00+01:00',
   'isGreenDelivery': False},
  {'postalCode': '11252',
   'deliveryDate': '2021-09-22T00:00:00+01:00',
   'isGreenDelivery': True},
  {'postalCode': '11252',
   'deliveryDate': '2021-09-24T00:00:00+01:00',
   'isGreenDelivery': False}]}}


product_list_2 = [
    {'productId': '1',
     'name': 'watermelon',
     'deliveryDays': [0],
     'productType': 'external',
     'daysInAdvance': 14
     },
    {'productId': '2',
     'name': 'bread',
     'deliveryDays': [2],
     'productType': 'normal',
     'daysInAdvance': 2
     },
    {'productId': '3',
     'name': 'strawberry',
     'deliveryDays': [6],
     'productType': 'temporary',
     'daysInAdvance': 3
     }
]


expect_delivery_response_for_product_list_2 = {
 'status': 'fail',
 'data': {'deliveryDates': []}}


post_code = '11252'
