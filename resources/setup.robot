*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${browser}       Chrome
${wait_timeout}  10s


*** Keywords ***
Browser Setup
    Open Browser    browser=${browser}
    Maximize Browser Window
    Set Browser Implicit Wait    ${wait_timeout}

Go Back
    Execute Javascript  history.back()