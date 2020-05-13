@stable
Feature: Download Chrome
  As a user
  I want to download chrome on different platforms
  So I can be sure my product is available for everybody


  Scenario Outline: Download Chrome on Mac OS
    Given a user is at the "<chrome>" website on Mac
    When the user clicks on the Download button in the hero section
    Then the user is redirected to the thank you page
#    And retry link is displayed on the thank you page
    Examples:
    |chrome  |
    |/chrome |
    |/intl/es-419/chrome/|
