*** Settings ***
Resource  ../Resources/Common.robot  #necessary for test setup and test teardown
Resource  ../Resources/Amazon.robot
Test Setup  Begin Web Test
Test Teardown  End Web Test
# pybot -d results tests/amazon2.robot

*** Test Cases ***
Logged out user can search for products
    Amazon.Search for Products

Logged out user can view a product
    Amazon.Search for Products
    Amazon.Select Product from Search Results

Logged out user can add product to cart
    Amazon.Search for Products
    Amazon.Select Product from Search Results
    Amazon.Add Product to Cart

Logged out user must sign in to check out
    Amazon.Search for Products
    Amazon.Select Product from Search Results
    Amazon.Add Product to Cart
    Amazon.Begin Checkout
