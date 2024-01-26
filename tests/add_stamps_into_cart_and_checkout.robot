*** Settings ***
Library        SeleniumLibrary
Resource       ../resources/setup.robot
Resource       ../resources/pages/home_page.robot
Resource       ../resources/pages/stamps_page.robot
Resource       ../resources/pages/checkout_page.robot
Resource       ../resources/pages/cart_page.robot
Library        ../resources/pages/cart_page.py
Library        ../resources/pages/checkout_page.py

Test Setup     Browser Setup
Test Teardown  Close Browser

*** Variables ***
${stamps_count}                 3
${adittional_stamps_count}      1
${total_stamps_count}           ${${stamps_count}+${adittional_stamps_count}}

*** Test Cases ***
Add stamps into cart and checkout
    Navigate to Home Page
    Check that Send Letters With Postcards Section Is Present
    Navigate to Stamps Page
    Navigate to Letters and Stamps with E-Value
    ${stamp_titles}     ${stamp_prices}=   Add Stamps To Cart      ${stamps_count}
    ${number_of_items}=     Get Number Of Items In The Cart
    Should Be Equal As Numbers    ${number_of_items}    ${stamps_count}
    Navigate to the Cart
    Check Items in the Cart     ${stamp_titles}     ${stamp_prices}
    Check Total in the Cart     ${stamp_prices}
    Go Back
    Go Back
    Sleep    1s
    ${adittional_stamp_titles}     ${adittional_stamp_prices}=   Add Stamps To Cart      ${adittional_stamps_count}
    ${number_of_items}=     Get Number Of Items In The Cart
    Should Be Equal As Numbers    ${number_of_items}    ${total_stamps_count}
    ${stamp_titles}=    Combine Lists       ${stamp_titles}     ${adittional_stamp_titles}
    ${stamp_prices}=    Combine Lists       ${stamp_prices}     ${adittional_stamp_prices}
    Navigate to the Cart
    Check Items in the Cart     ${stamp_titles}     ${stamp_prices}
    Check Total in the Cart     ${stamp_prices}
    Continue to Checkout
    Fill Up User Information
    Check Postcode Validation Field