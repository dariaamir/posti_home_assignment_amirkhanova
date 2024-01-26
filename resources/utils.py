from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def get_driver():
    selenium_library: SeleniumLibrary = BuiltIn().get_library_instance('SeleniumLibrary')
    return selenium_library.driver


@keyword('Scroll To Element')
def scroll_to_element(by: By, element_locator: str):
    driver: WebDriver = get_driver()
    element = driver.find_element(by=by, value=element_locator)
    driver.execute_script("arguments[0].scrollIntoView();", element)
