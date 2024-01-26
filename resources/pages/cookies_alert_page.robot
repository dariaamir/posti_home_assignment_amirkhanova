*** Settings ***
Library      SeleniumLibrary
Variables    cookies_alert_page.py

*** Keywords ***
Accept Cookies
    Element Should Be Visible    ${cookies_alert}
    Click Button    ${accept_all_cookies_button}
    Wait Until Element Is Not Visible    ${cookies_alert}