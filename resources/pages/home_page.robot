*** Settings ***
Library      SeleniumLibrary
Library      Collections
Library      ../utils.py
Variables    home_page.py
Resource     cookies_alert_page.robot

*** Variables ***
${home_page_url}    https://www.posti.fi/en
${send_letters_and_products_with_stamps_text}    Send letters and postcards with stamps

*** Keywords ***
Navigate to Home Page
    Go To    ${home_page_url}
    Accept Cookies

Check that Send Letters With Postcards Section Is Present
    Element Should Be Visible    ${send_letters_and_products_with_stamps_css}
    Element Text Should Be    ${send_letters_and_products_with_stamps_text_header_css}    ${send_letters_and_products_with_stamps_text}

Click All Stamps Button
    Scroll To Element     ${all_stamps_and_envelopers_from_the_online_store_button_by}[0]    ${all_stamps_and_envelopers_from_the_online_store_button_by}[1]
    Sleep    2s
    Click Button            ${all_stamps_and_envelopers_from_the_online_store_button_css}

Navigate to Stamps Page
    Click All Stamps Button
    Sleep    2s
    Switch Window  locator=NEW
    Title Should Be    	Stamps
