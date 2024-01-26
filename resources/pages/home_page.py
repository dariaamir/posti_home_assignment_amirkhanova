from selenium.webdriver.common.by import By

send_letters_and_products_with_stamps = 'div[id="send-letters-and-postcards-with-stamps"]'
send_letters_and_products_with_stamps_css = 'css:' + send_letters_and_products_with_stamps
send_letters_and_products_with_stamps_text_header_css = send_letters_and_products_with_stamps_css + ' h2'
all_stamps_and_envelopers_from_the_online_store_button_css = send_letters_and_products_with_stamps_css + ' button'

all_stamps_and_envelopers_from_the_online_store_button_by = \
    (By.CSS_SELECTOR, send_letters_and_products_with_stamps + ' button')