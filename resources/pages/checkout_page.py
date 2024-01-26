from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

first_name_field_id = 'id:billing-firstname-field'
last_name_field_id = 'id:billing-lastname-field'
address_click_css = 'css:div[class*="select__control"]'
address_css = 'css:div[class*="select__input-container"] input'
postcode_id = 'id:billing-postcode-field'
phone_id = 'id:billing-telephone-field'
email_id = 'id:billing-email-field'
save_and_continue_button_id = 'id:checkoutNexBtn'

postcode_error_message_text = ('Value must be in the following form:\n'
                               'NNNNN (where N = number, A = letter and X = number or letter).')
postcode_error_message_by = By.CSS_SELECTOR, 'div[class*="PostcodeField__PostcodeMessageWrapper"]'

first_name = 'John'
last_name = 'Smith'
address = 'Ale'
phone = '12345678'
email = 'test@test.com'

postcode_correct = '12345'
postcode_less_than_5_numbers = '123'
postcode_more_than_5_numbers = '123456'
postcode_numbers_and_letters = '123ab'
postcode_numbers_and_symbols = '1234!'


@keyword('Assert Postcode is Invalid Message')
def assert_postcode_is_invalid_message():
    selenium_library: SeleniumLibrary = BuiltIn().get_library_instance('SeleniumLibrary')
    driver: WebDriver = selenium_library.driver
    assert (driver.find_element(By.CSS_SELECTOR, 'div[class*="PostcodeField__PostcodeMessageWrapper"]').text
            == postcode_error_message_text), 'ERROR: Error message for incorrect postcode is not displayed '


@keyword('Check That Postcode Is Saved')
def check_that_postcode_is_saved():
    selenium_library: SeleniumLibrary = BuiltIn().get_library_instance('SeleniumLibrary')
    driver: WebDriver = selenium_library.driver
    postcode_at_the_checkout = driver.find_element(By.ID, 'billing-summary-postcode').text
    assert postcode_at_the_checkout == postcode_correct,\
        f'ERROR: Postcode is not saved correctly. Actual: {postcode_at_the_checkout}, expected: {postcode_correct}'
