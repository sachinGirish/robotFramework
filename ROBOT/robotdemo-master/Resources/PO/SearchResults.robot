*** Settings ***
Library  Selenium2Library

*** Keywords ***
Verify Search Completed
    wait until page contains  results for "dune"

Click Product Link
    [Documentation]  Clicks on the first product in the search results list
    click element  //li[@id='result_0']/div/div/div/div[2]/div/a/h2