Feature: Login Functionality

  @login @first
  Scenario Outline: Login with valid credentials
	Given I navigated to Login page
	When I enter valid email as "<email>" and valid password as "<password>"into the fields
	And I click on Login Button
	Then I should get logged in
	Examples:
	  | email           | password  |
	  | m483@gmail.com  | Manas@483 |
	  | ma483@gmail.com | Manas@483 |

  @login @third
  Scenario: Login with invalid email and valid password
	Given I navigated to Login page
	When I enter invalid email and valid password into the fields
	And I click on Login Button
	Then I should get a proper warning message

  @login
  Scenario: Login with valid email and invalid password
	Given I navigated to Login page
	When I enter valid email and invalid password into the fields
	And I click on Login Button
	Then I should get a proper warning message

  @login
  Scenario: Login with invalid credentials
	Given I navigated to Login page
	When I enter invalid email and invalid password into the fields
	And I click on Login Button
	Then I should get a proper warning message

  @login
  Scenario: Login without entering any credentials
	Given I navigated to Login page
	When I dont enter anything into email and password the fields
	And I click on Login Button
	Then I should get a proper warning message



