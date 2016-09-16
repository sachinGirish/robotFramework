*** Settings ***
Documentation  Amazon top navigation
Library  Selenium2Library

*** Keywords ***
Search for Products
    Enter Search Term
    Submit Search

Enter Search Term
    input text  id=twotabsearchtextbox  dune

Submit Search
    click button  xpath=//*[@id="nav-search"]/form/div[2]/div/input