Feature: User Login
  As a user of the application
  I want to be able to log in with valid credentials
  So that I can access my account and its features

  Scenario: Successful Login with Valid Credentials
    Given the login page is displayed
#    When I enter raj.gamebegins@gmail.com in the email field
#    And I enter Learning1# in the password field
    When I enter user in the email field
    And I enter pass in the password field
    And I click on the login button
    Then I should be logged into the application
