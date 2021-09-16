from Assignment.main import future_two_weeks, change_weekday_to_date, check_if_green_day, find_delivery_date
import datetime
from Assignment.test_data import product_list_1, post_code, product_list_2, expect_delivery_response_for_product_list_2


def test_change_weekday_to_date():
    deliveryweekdays = [0, 1, 2, 3, 4, 5, 6]
    expect_dates = change_weekday_to_date(deliveryweekdays)
    return future_two_weeks == expect_dates


def test_check_if_green_day():
    date = datetime.date(2021, 9, 5)
    return check_if_green_day(date) == True


def test_find_delivery_date_fail():
    result = find_delivery_date(post_code, product_list_2)
    expected_result = expect_delivery_response_for_product_list_2
    return result == expected_result


print(test_change_weekday_to_date())
print(test_check_if_green_day())
print(test_find_delivery_date_fail())


def test_find_delivery_date_success():
    result = find_delivery_date(post_code, product_list_1)
    print(result)


test_find_delivery_date_success()
