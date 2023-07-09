Feature: Register Account functionality


  @register @second
  Scenario: Register with mandatory fields
	Given I navigated to Register Page
	When I enter below details into mandatory fields
	  | first_name   | last_name      | telephone | password  |
	  | Manas Ranjan | Singdev sachan | 12345     | Manas@123 |
	And I click on Continue button
	Then Account should get created

  @register @second
  Scenario: Register with all fields
	Given I navigated to Register Page
	When I enter below details into all fields
	  | first_name   | last_name      | telephone | password  |
	  | Manas Ranjan | Singdev sachan | 12345     | Manas@123 |
	And I click on Continue button
	Then Account should get created

  @register
  Scenario: Register with duplicate email address
	Given I navigated to Register Page
	When I enter details into all fields except email field
	And I enter existing accounts email into email field
	And I click on Continue button
	Then Proper warning message informing about duplicate account should be displayed

  @register
  Scenario: Register without providing any details
	Given I navigated to Register Page
	When I dont enter anything into the field
	And I click on Continue button
