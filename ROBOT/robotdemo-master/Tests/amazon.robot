*** Settings ***
Documentation     This is a test
Library           Selenium2Library
Resource          ../Resources/AmazonOld.robot
Resource          ../Resources/CommonOld.robot    # pybot -d results tests/amazon.robot

*** Variables ***
${SEARCH_TERM}    dune
${START_URL}      http://www.amazon.in
${BROWSER}        chrome

*** Test Cases ***
User must sign in to checkout
    [Documentation]    This is some basic info about the test
    Begin Web Test
    Search for Products
    Select Product from Search Results
    Add Product to Cart
    Begin Checkout
    End Web Test

*** Keywords ***
Begin Web Test
    open browser    ${START_URL}    ${BROWSER}
    maximize browser window

Search for Products
    wait until page contains    Your Amazon.in
    input text    id=twotabsearchtextbox    ${SEARCH_TERM}
    click button    xpath=//*[@id="nav-search"]/form/div[2]/div/input
    wait until page contains    results for "${SEARCH_TERM}"

Select Product from Search Results
    click element    //li[@id='result_0']/div/div/div/div[2]/div/a/h2
    wait until page contains    Back to search results

Add Product to Cart
    click button    id=add-to-cart-button
    wait until page contains    Added to Cart

Begin Checkout
    click element    id=hlb-ptc-btn-native
    page should contain element    css=.a-spacing-small
    wait until page contains    Sign In

End Web Test
    close browser
