# Feature: Manager Expense Approval

Feature: Manager Expense Approval Workflow
  As a manager
  I want to review and process expense requests
  So that I can manage team reimbursements effectively

  Background:
    Given the Manager app is running on port 5001
    And I am on the manager login page

  # Test Case: TC-E2E-008
  @login @happy_path
  Scenario: Manager login successfully
    Given I enter manager username "manager1"
    And I enter manager password "password123"
    When I click the manager login button
    Then I should be redirected to the manager dashboard
    And I should see the expense management panel

  # Test Case: TC-E2E-009
  @pending @view
  Scenario: View pending expenses
    Given I am logged in as manager "manager1" with password "password123"
    When I navigate to the pending expenses tab
    Then I should see a list of pending expenses
    And each expense should show employee name and amount and status

  # Test Case: TC-E2E-010
  @approval
  Scenario: Approve an expense
    Given 
    And 
    When 
    Then 
    And 

  # Test Case: TC-E2E-011
  @denial
  Scenario: Deny an expense with comment
    Given 
    And 
    When 
    And 
    Then 
    And 

  # Test Case: TC-E2E-012
  @reports
  Scenario: Generate expense CSV report
    Given
    When 
    And 
    Then 
    And 

  @logout
  Scenario: Manager logout
    Given 
    When 
    Then 
    And 

  # Scenario Outline for multiple approval decisions
  @approval @parameterized
  Scenario Outline: Process expense with different decisions
    Given 
    And 
    When
    And 
    Then 

    Examples:
      | expense_id | decision | comment              | result_status |
      | 1          | approve  | Good documentation   | approved      |
      | 2          | deny     | Missing receipts     | denied        |

  @view_all
  Scenario: View all expenses
    Given 
    When 
    Then 
    And 
