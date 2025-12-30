# Feature: Employee Expense Management

Feature: Employee Expense Management
  As an employee
  I want to manage my expenses through the web application
  So that I can submit reimbursement requests and track their status

  Background:
    Given the Employee app is running on port 5000
    And I am on the login page

  # Test Case: TC-E2E-001
  @login @happy_path
  Scenario: Successful employee login
    Given I enter username "employee1"
    And I enter password "password123"
    When I click the login button
    Then I should be redirected to the expense dashboard
    And I should see a welcome message

  # Test Case: TC-E2E-002
  @login @sad_path
  Scenario: Failed login with invalid credentials
    Given 
    And 
    When 
    Then 
    And 

  # Test Case: TC-E2E-003
  @expense @submit
  Scenario: Submit a new expense
    Given I am logged in as "employee1" with password "password123"
    When I navigate to the expense submission form
    And I enter expense amount "75.50"
    And I enter expense description "Team lunch meeting"
    And I select today's date
    And I click the submit button
    Then I should see a success message
    And the expense should appear in my expense list with status "pending"

  # Test Case: TC-E2E-004
  @expense @view
  Scenario: View expense list
    Given 
    When 
    Then 
    And 

  # Test Case: TC-E2E-005
  @expense @edit
  Scenario: Edit a pending expense
    Given 
    And 
    When 
    And 
    And 
    And 
    Then 
    And 

  # Test Case: TC-E2E-007 - Scenario Outline
  @expense @filter
  Scenario Outline: Filter expenses by status
    Given 
    When 
    And 
    Then 

    Examples:
      | status   |
      | pending  |
      | approved |
      | denied   |

  @logout
  Scenario: Employee logout
    Given 
    When 
    Then 
    And 
