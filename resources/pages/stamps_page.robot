*** Settings ***
Library      SeleniumLibrary
Library    ../utils.py
Variables   stamps_page.py
Library      stamps_page.py
Variables   cart_page.py


*** Keywords ***
Navigate to Letters and Stamps with E-Value
    Click Element    ${letters_and_cards_with_e_value_menu_item_xpath}
    Wait Until Element Contains     ${page_title_xpath}    ${letters_and_cards_with_e_value}


Get Number Of Items In The Cart
    ${number_of_items}=   Get Text    ${cart_quantity_css}
    RETURN   ${number_of_items}

Navigate to the Cart
    Click Element    ${cart_button_css}
    Wait Until Element Contains     ${cart_page_title_id}    ${cart_page_title}
    Wait Until Element Is Enabled    ${checkout_button_css}