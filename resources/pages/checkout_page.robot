*** Settings ***
Library      SeleniumLibrary
Variables    checkout_page.py
Library      checkout_page.py

*** Keywords ***
Fill Up User Information
    Wait Until Element Is Enabled    ${first_name_field_id}
    Input Text    ${first_name_field_id}      ${first_name}
    Input Text    ${last_name_field_id}      ${last_name}
    Click Element   ${address_click_css}
    Input Text    ${address_css}      ${address}
    Sleep    1s
    Press Keys    ${address_css}    RETURN
    Input Text    ${phone_id}      ${phone}
    Input Text    ${email_id}      ${email}
    Sleep    2s

Check Postcode Validation Field
    Clear Element Text    ${postcode_id}
    Assert Postcode is Invalid Message
    Input Text    ${postcode_id}      ${postcode_less_than_5_numbers}
    Assert Postcode is Invalid Message
    Input Text    ${postcode_id}      ${postcode_more_than_5_numbers}
    Assert Postcode is Invalid Message
    Input Text    ${postcode_id}      ${postcode_numbers_and_letters}
    Assert Postcode is Invalid Message
    Input Text    ${postcode_id}      ${postcode_numbers_and_symbols}
    Assert Postcode is Invalid Message
    Input Text    ${postcode_id}      ${postcode_correct}
    Click Element    ${save_and_continue_button_id}
    Check That Postcode Is Saved
