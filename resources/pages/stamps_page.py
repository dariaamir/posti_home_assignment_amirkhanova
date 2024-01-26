from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


page_title_xpath = 'xpath://div[contains(@class, "Grid__Cell")]/div/span'

letters_and_cards_with_e_value_menu_item_xpath = 'xpath://a[text()="For letters and cards with €-value"]'
letters_and_cards_with_e_value = 'For letters and cards with €-value'

cart_button_css = 'css:a[data-testid="cart-button"]'
cart_quantity = 'span[data-testid="cart-quantity"]'
cart_quantity_by = (By.CSS_SELECTOR, cart_quantity)
cart_quantity_css = 'css:' + cart_quantity

product_title_xpath = '(//div[contains(@class, "ProductCardstyle__StyledHeadline")]/div)'
product_price_xpath = '(//div[contains(@class, "ProductCardstyle__Row")]/div)'
product_add_to_cart_button_xpath = '(//div[contains(@class, "ProductCardstyle__Row")]/div/button)'

notification_by = (By.CSS_SELECTOR, 'li[class*="Notifications__ListItem"]')


@keyword('Add Stamps To Cart')
def add_stamps_to_cart(count):
    """Adds desired number of items into the cart and returns their titles and prices as 2 lists"""
    selenium_library: SeleniumLibrary = BuiltIn().get_library_instance('SeleniumLibrary')
    driver = selenium_library.driver
    stamp_titles = []
    stamp_prices = []
    for i in range(1, int(count)+1):
        title = driver.find_element(By.XPATH, product_title_xpath+f'[{i}]').text
        stamp_titles.append(title)
        add_to_cart_button = driver.find_element(By.XPATH, product_add_to_cart_button_xpath+f'[{i}]')
        add_to_cart_button.click()

    for j in range(1, int(count)*2, 2):
        price = driver.find_element(By.XPATH, product_price_xpath+f'[{j}]').text
        stamp_prices.append(price)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.invisibility_of_element_located(notification_by))

    return stamp_titles, stamp_prices
