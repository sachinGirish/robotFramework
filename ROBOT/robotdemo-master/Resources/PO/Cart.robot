*** Settings ***
Library  Selenium2Library

*** Keywords ***
Verify Product Added
    wait until page contains  Added to Cart

Proceed to Checkout
    click element  id=hlb-ptc-btn-native
    page should contain element  css=.a-spacing-small