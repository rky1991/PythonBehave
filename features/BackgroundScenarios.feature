Feature: Orange HRM Logo

  Background: Comon Steps
    Given launch Crome Browser
    When open Orange HRM homepage
    Then Enter UserName "Admin" and Password "admin123"
    Then Click on Login Button

  Scenario: Logo Presence on Orange Home Page
    Then User successfully login to the dashboard page
    And close Browser

  Scenario: Search User
    When I navigate to search page
    Then Search page should be display
    And close Browser


  Scenario: Advance Search User
    When I navigate to advance search page
    Then Adavnce search page should be display
    And close Browser