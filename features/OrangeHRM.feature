Feature: Orange HRM Logo

  Scenario: Logo Presence on Orange Home Page
    Given launch Crome Browser
    When open Orange HRM homepage
    Then verify that the logo present on page
    And close Browser
