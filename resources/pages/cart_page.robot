*** Settings ***
Library      SeleniumLibrary
Variables    cart_page.py

*** Keywords ***
Continue to Checkout
    Click Element    ${checkout_button_css}