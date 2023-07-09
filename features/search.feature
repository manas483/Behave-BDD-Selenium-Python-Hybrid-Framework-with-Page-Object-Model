Feature: Search functionality

  @search
  Scenario: Search for valid product
    Given I goto navigated to home page
    When I entered valid product say "HP" into the search box
    And I click on Search button
    Then Valid product should get displayed in the search result
  @search
  Scenario: Search for an invalid product
    Given I goto navigated to home page
    When I entered invalid product say "HONDA" into the search box
    And I click on Search button
    Then Proper message should be displayed in Search results
  @search
  Scenario: Search without entering any product
    Given I goto navigated to home page
    When I dont enter anything into the search box
    And I click on Search button
    Then Proper message should be displayed in Search results



