"""
Unit Tests for ExpenseService

- Testing business logic with mocked repositories
- Validating happy path and sad path scenarios
- Testing exception handling
- Using Side Effects in mocks 

Test Cases Covered:
- TC-EXP-001 through TC-EXP-012
"""
import pytest
from unittest.mock import MagicMock
import allure
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from service.expense_service import ExpenseService
from repository.expense_model import Expense
from repository.approval_model import Approval


@allure.epic("Employee App")
@allure.feature("Expense Service")
class TestExpenseService:
    """
    Test suite for ExpenseService class.
    
    This tests the business logic layer which:
    - Validates input data
    - Coordinates between repositories
    - Enforces business rules (e.g., can't edit approved expenses)
    """
    
    @pytest.fixture
    def mock_expense_repo(self):
        """Mock ExpenseRepository."""
        return MagicMock()
    
    @pytest.fixture
    def mock_approval_repo(self):
        """Mock ApprovalRepository."""
        return MagicMock()
    
    @pytest.fixture
    def expense_service(self, mock_expense_repo, mock_approval_repo):
        """Create ExpenseService with mock repositories."""
        return ExpenseService(mock_expense_repo, mock_approval_repo)
    
    @pytest.fixture
    def sample_expense(self):
        """Sample expense for testing."""
        return Expense(id=1, user_id=1, amount=100.00, description="Business lunch", date="2024-01-01")
    
    @pytest.fixture
    def pending_approval(self):
        """Sample pending approval."""
        return Approval(id=1, expense_id=1, status="pending", reviewer=None, comment=None, review_date=None)
    
    @pytest.fixture
    def approved_approval(self):
        """Sample approved approval."""
        return Approval(id=1, expense_id=1, status="approved", reviewer=2, comment="Approved", review_date="2024-01-02")
    
    # ==================== SUBMIT EXPENSE TESTS ====================
    
    @allure.story("Expense Submission")
    @allure.title("Submit expense with valid data")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.unit
    def test_submit_expense_valid_data(self, expense_service, mock_expense_repo, sample_expense):
        """
        Test Case: TC-EXP-001
        
        Test submitting an expense with valid data.
        - Mocking return values
        - Verifying method calls with specific arguments
        """
        # Arrange
        mock_expense_repo.create.return_value = sample_expense
        
        # Act
        result = expense_service.submit_expense(
            user_id=1,
            amount=100.00,
            description="Business lunch",
            date="2024-01-01"
        )
        
        # Assert
        assert result is not None
        assert result.amount == 100.00
        assert result.description == "Business lunch"
        mock_expense_repo.create.assert_called_once()
    
    @allure.story("Expense Submission")
    @allure.title("Submit expense without date uses current date")
    @pytest.mark.unit
    def test_submit_expense_no_date(self, expense_service, mock_expense_repo, sample_expense):
        """
        Test that submitting without date uses current date.
        """
        # Arrange
        #TO DO: Mock current date
        
        # Act - No date provided
        #TO DO: Mock current date and call submit_expense without date
        
        # Assert
        assert result is not None
        # The create method should still be called
        mock_expense_repo.create.assert_called_once()
    
    @allure.story("Expense Submission")
    @allure.title("Reject expense with zero amount")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.unit
    def test_submit_expense_zero_amount(self, expense_service):
        """
        Test Case: TC-EXP-002
        
        Test that amount = 0 raises ValueError.
      - Testing exception handling with pytest.raises
        - Validating error messages
        """
        # Act & Assert
       # TO DO: Call submit_expense with amount=0
        
        # Verify error message
        # TO DO: Add assertions for error message
    
    @allure.story("Expense Submission")
    @allure.title("Reject expense with negative amount")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.unit
    def test_submit_expense_negative_amount(self, expense_service):
        """
        Test Case: TC-EXP-003
        
        Test that negative amount raises ValueError.
        """
        # Act & Assert
        # TO DO: Call submit_expense with negative amount
        
        # Verify error message
        # TO DO: Add assertions for error message
    
    @allure.story("Expense Submission")
    @allure.title("Reject expense with empty description")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.unit
    def test_submit_expense_empty_description(self, expense_service):
        """
        Test Case: TC-EXP-004
        
        Test that empty description raises ValueError.
        """
        # Act & Assert
        # TO DO: Call submit_expense with empty description
        
        # Verify error message
        # TO DO: Add assertions for error message
    
    @allure.story("Expense Submission")
    @allure.title("Reject expense with whitespace-only description")
    @pytest.mark.unit
    def test_submit_expense_whitespace_description(self, expense_service):
        """
        Test edge case: description with only whitespace.
        """
        # Act & Assert
        # TO DO: Call submit_expense with whitespace-only description
    
    # ==================== GET EXPENSES TESTS ====================
    
    @allure.story("Expense Retrieval")
    @allure.title("Get user expenses with status")
    @pytest.mark.unit
    def test_get_user_expenses_with_status(self, expense_service, mock_approval_repo, sample_expense, pending_approval):
        """
        Test Case: TC-EXP-005
        
        Test retrieving all expenses for a user.
        """
        # Arrange
       #TO DO: Mock the return values for the repositories
        
        # Act
        #TO DO: Call get_user_expenses with user_id and status_filter
        
        # Assert
        #TO DO: Add assertions to verify the result
    
    @allure.story("Expense Retrieval")
    @allure.title("Get expense by ID for owner")
    @pytest.mark.unit
    def test_get_expense_by_id_owner(self, expense_service, mock_expense_repo, sample_expense):
        """
        Test Case: TC-EXP-006
        
        Test getting expense by ID when user is the owner.
        """
        # Arrange
        #TO DO: Mock the return values for the repositories
        
        # Act - user_id matches expense.user_id
        #TO DO: Call get_expense_by_id with user_id matching expense.user_id
        
        # Assert
        #TO DO: Add assertions to verify the result
    
    @allure.story("Expense Retrieval")
    @allure.title("Reject get expense by ID for non-owner")
    @pytest.mark.unit
    def test_get_expense_by_id_non_owner(self, expense_service, mock_expense_repo, sample_expense):
        """
        Test Case: TC-EXP-007
        
        Test that non-owner cannot access expense.
        """
        # Arrange
       
        
        # Act - user_id 2 doesn't own expense 1
       
        
        # Assert
        
    
    # ==================== UPDATE EXPENSE TESTS ====================
    
    @allure.story("Expense Update")
    @allure.title("Update pending expense successfully")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_update_expense_pending(self, expense_service, mock_expense_repo, mock_approval_repo, sample_expense, pending_approval):
        """
        Test Case: TC-EXP-008
        
        Test updating a pending expense.
        
        - Setting up multiple mocks that work together
        - Testing business rule: only pending expenses can be edited
        """
        # Arrange
        
        
        # Act
    
        
        # Assert
        assert result is not None
       
    
    @allure.story("Expense Update")
    @allure.title("Reject update of approved expense")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_update_expense_approved_rejected(self, expense_service, mock_expense_repo, mock_approval_repo, sample_expense, approved_approval):
        """
        Test Case: TC-EXP-009
        
        Test that approved expenses cannot be updated.
        
        Business Rule: Once reviewed, expenses are locked.
        """
        # Arrange
       
        
        # Act & Assert
        
        
       
    
    # ==================== DELETE EXPENSE TESTS ====================
    
    @allure.story("Expense Deletion")
    @allure.title("Delete pending expense successfully")
    @pytest.mark.unit
    def test_delete_expense_pending(self, expense_service, mock_expense_repo, mock_approval_repo, sample_expense, pending_approval):
        """
        Test Case: TC-EXP-010
        
        Test deleting a pending expense.
        """
        # Arrange
        
        
        # Act
       
        
        # Assert
       
    
    @allure.story("Expense Deletion")
    @allure.title("Reject deletion of approved expense")
    @pytest.mark.unit
    def test_delete_expense_approved_rejected(self, expense_service, mock_expense_repo, mock_approval_repo, sample_expense, approved_approval):
        """
        Test Case: TC-EXP-011
        
        Test that approved expenses cannot be deleted.
        """
        # Arrange
       
        
        # Act & Assert
       
    
    # ==================== FILTER TESTS ====================
    
    @allure.story("Expense Filtering")
    @allure.title("Filter expenses by pending status")
    @pytest.mark.unit
    def test_get_expense_history_filter_pending(self, expense_service, mock_approval_repo, sample_expense, pending_approval):
        """
        Test Case: TC-EXP-012
        
        Test filtering expenses by status.
        """
        # Arrange
       
        
        # Act
        
        
        # Assert
    
    
    @allure.story("Expense Filtering")
    @allure.title("Filter expenses with invalid status returns filtered list")
    @pytest.mark.unit
    def test_get_expense_history_invalid_filter(self, expense_service, mock_approval_repo, sample_expense, pending_approval):
        """
        Test that invalid filter returns all expenses (no filtering applied).
        """
        # Arrange
       
        
        # Act - Invalid status filter
        
        
        # Assert - Should return all (no filter applied)
        


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
