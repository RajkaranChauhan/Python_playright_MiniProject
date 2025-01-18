Feature: In Payment method page user should verify the email and update the email
  and select the country and place order

  Scenario: User updating the shipping address
    Given User is in payment method page
    Then Verify the populated email is raj.gamebegins@gmail.com
    Then User update the email to don.piet2008@gmail.com
    Then Verify the populated email is don.piet2008@gmail.com
    Then User selects the country as India
    When User click on the button Place Order
    Then User should be in Order confirmation page
