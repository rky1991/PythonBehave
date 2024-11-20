Feature: Orange HRM Logo

  Scenario: Logo Presence on Orange Home Page
    Given launch Crome Browser
    When open Orange HRM homepage
    Then Enter UserName "Admin" and Password "admin123"
    Then Click on Login Button
    Then User successfully login to the dashboard page
    And close Browser

  Scenario Outline: Logo Presence on Orange Home Page
    Given launch Crome Browser
    When open Orange HRM homepage
    Then Enter UserName "<UserName>" and Password "<Password>"
    Then Click on Login Button
    Then User successfully login to the dashboard page
    And close Browser
    Examples:
      | UserName | Password    |
      | Admin    | admin123    |
      | Admin123 | admin123    |
      | Admin    | admin123xct |