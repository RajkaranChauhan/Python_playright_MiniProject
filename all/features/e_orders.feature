Feature: goto orders page and verify the order that user have made is available there
  and when user clicks on the view button user gets the
  order summary details

  Scenario: verify order details
    When User clicks on the Orders button user navigates to order details page
    Then Verify the Order is available there
    When User clicks on the View button of the order id that he made he moves to order summary page
    Then Verify order id is displayed there
    Then Verify Delivery Address has email as raj.gamebegins@gmail.com