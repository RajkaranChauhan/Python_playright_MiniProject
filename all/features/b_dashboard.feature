Feature: Selects the items from the page and add to cart
  Background: user login to the application and navigates to dashboard page

  Scenario: Add items to cart
#    Given User login to the application using raj.gamebegins@gmail.com and Learning1# as credentials and is in dashboard page

    Given user should navigate to the Dashboard page
    Then add ADIDAS ORIGINAL
    Then add IPHONE 13 PRO
    Then go to Cart

