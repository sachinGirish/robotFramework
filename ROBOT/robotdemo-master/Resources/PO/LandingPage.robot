*** Settings ***
Library  Selenium2Library

*** Keywords ***
Load
    go to  http://www.amazon.com
    wait until page contains  Your Amazon.com