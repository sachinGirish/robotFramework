*** Settings ***
Documentation  This file is for test setup and teardown
Library  Selenium2Library

*** Variables ***
${START_URL}  http://www.amazon.com
${BROWSER}  chrome

*** Keywords ***
Begin Web Test
    open browser  ${START_URL}  ${BROWSER}
    maximize browser window

End Web Test
    close browser