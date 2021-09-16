import datetime
from Assignment import settings

today = datetime.date.today()
this_sunday = today + datetime.timedelta(6 - today.weekday())
future_two_weeks = set([today + datetime.timedelta(num) for num in range(1, 15)])


def change_weekday_to_date(deliveryweekdays):
    deliverydays = set()
    for deliveryweekday in deliveryweekdays:
        days_ahead = deliveryweekday - today.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        deliverydays.add(today + datetime.timedelta(days_ahead))
        deliverydays.add(today + datetime.timedelta(days_ahead + 7))
    return deliverydays


def find_valid_delivery_date(product):
    product_delivery_dates = change_weekday_to_date(product['deliveryDays'])
    valid_delivery_dates = set()
    for product_delivery_date in product_delivery_dates:
        #  a delivery date is not valid if a product must be ordered more days in advance than possible
        if product_delivery_date < today + datetime.timedelta(product['daysInAdvance']):
            continue
        # all external products need to be ordered 5 days in advance
        if product['productType'] == settings.EXTERNAL and product_delivery_date < today + datetime.timedelta(settings.EXTERNAL_ORDER_MINDAYS):
            continue
        # temporary products can only be ordered within the current week (Mon-Sun)
        if product['productType'] == settings.TEMPORARY and product_delivery_date < this_sunday:
            continue
        valid_delivery_dates.add(product_delivery_date)
    return valid_delivery_dates


def get_delivery_union_days(products_delivery_date):
    union_days = future_two_weeks
    for dates in products_delivery_date.values():
        union_days = union_days.intersection(dates)
    return list(union_days)


def check_if_green_day(date):
    if date.weekday() == 2 or int(date.strftime("%d")) in settings.GREEN_DELIVERY_DAYS:
        return True
    return False


def find_delivery_date(postcode, product_list):
    products_delivery_date = {}
    for product in product_list:
        products_delivery_date[product['productId']] = find_valid_delivery_date(product)
    valid_delivery_dates = get_delivery_union_days(products_delivery_date)
    valid_delivery_dates.sort()

    delivery_dates = []
    for valid_delivery_date in valid_delivery_dates:
        is_green = check_if_green_day(valid_delivery_date)
        delivery_dates.append({
            "postalCode": postcode,
            "deliveryDate": valid_delivery_date.strftime("%Y-%m-%dT%H:%M:%S") + "+01:00",
            "isGreenDelivery": is_green
        })

    status = 'success' if delivery_dates else 'fail'
    return {"status": status,
            "data": {
                "deliveryDates": delivery_dates
            }}

