Feature: update the product in cart

  Scenario: Remove ADIDAS ORIGINAL from cart
    Given User is in my cart page
    Then Remove the product ADIDAS ORIGINAL from cart
    When User clicks on the checkout button
    Then User moves to the payment Method page