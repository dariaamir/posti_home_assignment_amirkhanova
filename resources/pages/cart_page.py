import re

from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

cart_page_title_id = 'id:cart-page-title'
cart_page_title = 'Cart'

item_title_xpath = '(//div[@id="cart-item-name"])'
item_price_xpath = '(//div[@data-testid="item-total-price"])'
subtotal_value = 'cart-totals-subtotal-value'
delivery_fee_id = 'cart-totals-shipping-value'
total_value_id = 'cart-totals-total-value'

checkout_button_css = 'css:button[data-testid="checkout"]'

pattern_for_price = r'(^\d*\.\d{2})'


def assert_lists_are_equal(list_1: list, list_2: list):
    return len(list_1) == len(list_2) and sorted(list_1) == sorted(list_2)


def get_price_from_string(string: str):
    return float(re.search(pattern_for_price, string).group(1))


def calculate_subtotal(price_list: list):
    prices = [get_price_from_string(list_item) for list_item in price_list]
    return sum(prices)


def calculate_delivery_fee(subtotal: float):
    if subtotal < 45:
       return 5.0
    else:
        return 0.0


def calculate_total(subtotal: float, delivery_fee: float):
    return subtotal + delivery_fee


@keyword('Check Items in the Cart')
def check_items_in_the_cart(stamp_titles: list, stamp_prices: list):
    """Checks, that all items, that were added to the cart, are correctly displayed there"""
    selenium_library: SeleniumLibrary = BuiltIn().get_library_instance('SeleniumLibrary')
    driver: WebDriver = selenium_library.driver

    all_items_in_the_cart_titles = [el.text for el in driver.find_elements(By.XPATH, item_title_xpath)]
    assert assert_lists_are_equal(stamp_titles, all_items_in_the_cart_titles), \
        f'ERROR: Incorrect items in the cart. Actual: {all_items_in_the_cart_titles}, expected: {stamp_titles}'
    all_items_in_the_cart_prices = [el.text.replace('€', ' €')
                                    for el in driver.find_elements(By.XPATH, item_price_xpath)]
    assert assert_lists_are_equal(stamp_prices, all_items_in_the_cart_prices), \
        (f'ERROR: Incorrect prices for the items in the cart. '
         f'Actual: {all_items_in_the_cart_prices}, expected: {stamp_prices}')


@keyword('Check Total in the Cart')
def check_total_in_the_cart(stamp_prices: list):
    """Checks, that subtotal, delivery and total prices are calculated correctly"""
    selenium_library: SeleniumLibrary = BuiltIn().get_library_instance('SeleniumLibrary')
    driver: WebDriver = selenium_library.driver

    subtotal = calculate_subtotal(stamp_prices)
    cart_subtotal = get_price_from_string(driver.find_element(By.ID, subtotal_value).text)
    assert subtotal == cart_subtotal, (f'ERROR: subtotal is not calculated correctly.'
                                      f'Actual: {cart_subtotal}, expected: {subtotal}')

    delivery_fee = calculate_delivery_fee(subtotal)
    cart_delivery_fee = get_price_from_string(driver.find_element(By.ID, delivery_fee_id).text)
    assert delivery_fee == cart_delivery_fee, (f'ERROR: delivery fee is not calculated correctly. '
                                               f'Actual: {cart_delivery_fee}, expected: {delivery_fee}')

    total = calculate_total(subtotal, delivery_fee)
    cart_total = get_price_from_string(driver.find_element(By.ID, total_value_id).text)
    assert total == cart_total, (f'ERROR: total is not calculated correctly.'
                                 f'Actual: {cart_total}, expected: {total}')
