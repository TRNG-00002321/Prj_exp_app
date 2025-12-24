"""
Unit Tests for ExpenseController

- Testing protected Flask endpoints
- Mocking authentication decorators
- Testing CRUD operations through controller layer
- Testing validation and error handling

"""
import pytest
from unittest.mock import MagicMock, patch
import allure
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from repository.user_model import User
from repository.expense_model import Expense
from repository.approval_model import Approval


@allure.epic("Employee App")
@allure.feature("Expense Controller")
class TestExpenseController:
    """
    Test suite for expense_controller.py endpoints.
    
    Tests cover:
    - POST /api/expenses (submit)
    - GET /api/expenses (list)
    - GET /api/expenses/<id> (get one)
    - PUT /api/expenses/<id> (update)
    - DELETE /api/expenses/<id> (delete)
    """
    
    @pytest.fixture
    def mock_auth_service(self):
        """Create a mock AuthenticationService."""
        return MagicMock()
    
    @pytest.fixture
    def mock_expense_service(self):
        """Create a mock ExpenseService."""
        return MagicMock()
    
    @pytest.fixture
    def sample_employee(self):
        """Provide sample employee user for tests."""
        return User(id=1, username='employee1', password='password123', role='Employee')
    
    @pytest.fixture
    def sample_expense(self):
        """Provide sample expense for tests."""
        return Expense(id=1, user_id=1, amount=100.00, description='Business lunch', date='2024-12-21')
    
    @pytest.fixture
    def sample_approval(self):
        """Provide sample approval for tests."""
        return Approval(id=1, expense_id=1, status='pending', reviewer=None, comment=None, review_date=None)
    
    @pytest.fixture
    def app_with_mock_services(self, mock_auth_service, mock_expense_service):
        """Create Flask app with mocked services."""
        from main import create_app
        app = create_app()
        app.config['TESTING'] = True
        app.auth_service = mock_auth_service
        app.expense_service = mock_expense_service
        return app
    
    @pytest.fixture
    def authenticated_client(self, app_with_mock_services, mock_auth_service, sample_employee):
        """Create authenticated Flask test client."""
        mock_auth_service.get_user_from_token.return_value = sample_employee
        client = app_with_mock_services.test_client()
        client.set_cookie('jwt_token', 'valid.jwt.token')
        return client
    
    @pytest.fixture
    def unauthenticated_client(self, app_with_mock_services):
        """Create unauthenticated Flask test client."""
        return app_with_mock_services.test_client()
    
    # ==================== SUBMIT EXPENSE TESTS ====================
    
    @allure.story("Submit Expense")
    @allure.title("TC-CTRL-EXP-001: Submit expense with valid data")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.unit
    def test_submit_expense_success(self, authenticated_client, mock_expense_service, sample_expense):
        """
        Test successful expense submission returns 201 Created.
       - Testing authenticated POST endpoints
        - Response should include created expense data
        """
        # Arrange
        mock_expense_service.submit_expense.return_value = sample_expense
        
        # Act
        response = authenticated_client.post('/api/expenses',
            json={'amount': 100.00, 'description': 'Business lunch', 'date': '2024-12-21'})
        
        # Assert
        assert response.status_code == 201
        data = response.get_json()
        assert data['message'] == 'Expense submitted successfully'
        assert data['expense']['amount'] == 100.00
        assert data['expense']['description'] == 'Business lunch'
        assert data['expense']['status'] == 'pending'
        
        # Verify service was called
        mock_expense_service.submit_expense.assert_called_once()
    
    @allure.story("Submit Expense")
    @allure.title("TC-CTRL-EXP-002: Submit expense without amount")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_submit_expense_missing_amount(self, authenticated_client):
        """
        Test submission with missing amount returns 400 Bad Request.
        """
        # Act
        #TODO: Implement test for missing amount
        
        # Assert
        #TODO: Implement assertion for missing amount
    
    @allure.story("Submit Expense")
    @allure.title("TC-CTRL-EXP-003: Submit expense without description")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_submit_expense_missing_description(self, authenticated_client):
        """
        Test submission with missing description returns 400 Bad Request.
        """
        # Act
       #TODO: Implement test for missing description
        
        # Assert
        #TODO: Implement assertion for missing description
    
    @allure.story("Submit Expense")
    @allure.title("TC-CTRL-EXP-004: Submit expense with invalid amount")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_submit_expense_invalid_amount(self, authenticated_client):
        """
        Test submission with non-numeric amount returns 400 Bad Request.
        """
        # Act
        #TODO: Implement test for invalid amount
        
        # Assert
        #TODO: Implement assertion for invalid amount
    
    @allure.story("Submit Expense")
    @allure.title("TC-CTRL-EXP-005: Submit expense without authentication")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.unit
    def test_submit_expense_unauthenticated(self, unauthenticated_client):
        """
        Test that unauthenticated request returns 401 Unauthorized.
        """
        # Act
        #TODO: Implement test for unauthenticated request
        
        # Assert
        #TODO: Implement assertion for unauthenticated request
    
    @allure.story("Submit Expense")
    @allure.title("Submit expense handles service exception")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_submit_expense_service_exception(self, authenticated_client, mock_expense_service):
        """
        Test that service exceptions return 500 Internal Server Error.
        """
        # Arrange
       #TODO: Implement test for service exception
        
        # Act
        #TODO: Implement test for service exception
        
        # Assert
        assert response.status_code == 500
    
    # ==================== GET EXPENSES TESTS ====================
    
    @allure.story("Get Expenses")
    @allure.title("TC-CTRL-EXP-006: Get all expenses for user")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.unit
    def test_get_expenses_success(self, authenticated_client, mock_expense_service, sample_expense, sample_approval):
        """
        Test getting expense list returns expenses with status.
        """
        # Arrange
       #TODO: Implement test for getting expenses with status
        
        # Act
        #TODO: Implement test for getting expenses with status
        
        # Assert
        #TODO: Implement assertion for getting expenses with status
    
    @allure.story("Get Expenses")
    @allure.title("TC-CTRL-EXP-007: Get expenses with status filter")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_get_expenses_with_filter(self, authenticated_client, mock_expense_service):
        """
        Test getting expenses with status filter passes filter to service.
        """
        # Arrange
        #TODO: Implement test for getting expenses with status filter
        
        # Act
        #TODO: Implement test for getting expenses with status filter
        
        # Assert
        #TODO: Implement assertion for getting expenses with status filter
    
    @allure.story("Get Expenses")
    @allure.title("Get expenses returns empty list when none exist")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.unit
    def test_get_expenses_empty(self, authenticated_client, mock_expense_service):
        """
        Test getting expenses when none exist returns empty list.
        """
        # Arrange
        #TODO: Implement test for getting empty expenses list
        
        # Act
        # TO DO Implement test for getting empty expenses list
        
        # Assert
        #TO DO Implement assertion for getting empty expenses list
    
    @allure.story("Get Expenses")
    @allure.title("Get expenses without authentication")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.unit
    def test_get_expenses_unauthenticated(self, unauthenticated_client):
        """
        Test that unauthenticated request returns 401 Unauthorized.
        """
        # Act
        #TODO: Implement test for unauthenticated request
        
        # Assert
        #TODO: Implement assertion for unauthenticated request
    
    # ==================== GET SINGLE EXPENSE TESTS ====================
    
    @allure.story("Get Expense")
    @allure.title("TC-CTRL-EXP-008: Get specific expense by ID")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_get_expense_by_id(self, authenticated_client, mock_expense_service, sample_expense, sample_approval):
        """
        Test getting a specific expense returns expense data.
        """
        # Arrange
        #TODO: Implement test for getting specific expense by ID
        
        # Act
        #TODO: Implement test for getting specific expense by ID
        
        # Assert
        #TODO: Implement assertion for getting specific expense by ID
    
    @allure.story("Get Expense")
    @allure.title("TC-CTRL-EXP-009: Get non-existent expense returns 404")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_get_expense_not_found(self, authenticated_client, mock_expense_service):
        """
        Test getting non-existent expense returns 404 Not Found.
        """
        # Arrange
        #TODO: Implement test for getting non-existent expense
        
        # Act
        #TODO: Implement test for getting non-existent expense
        
        # Assert
        #TODO: Implement assertion for getting non-existent expense
    
    # ==================== UPDATE EXPENSE TESTS ====================
    
    @allure.story("Update Expense")
    @allure.title("TC-CTRL-EXP-010: Update pending expense")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.unit
    def test_update_expense_success(self, authenticated_client, mock_expense_service, sample_expense):
        """
        Test updating a pending expense returns updated data.
        """
        # Arrange
        #TODO: Implement test for updating a pending expense
        
        # Act
        #TODO: Implement test for updating a pending expense
        
        # Assert
        #   TODO: Implement assertion for updating a pending expense
    
    @allure.story("Update Expense")
    @allure.title("TC-CTRL-EXP-011: Update non-existent expense returns 404")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_update_expense_not_found(self, authenticated_client, mock_expense_service):
        """
        Test updating non-existent expense returns 404 Not Found.
        """
        # Arrange
        #TODO: Implement test for updating non-existent expense
        
        # Act
        #TODO: Implement test for updating non-existent expense
        
        # Assert
        #TODO: Implement assertion for updating non-existent expense
    
    @allure.story("Update Expense")
    @allure.title("TC-CTRL-EXP-012: Update expense with missing fields")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_update_expense_missing_fields(self, authenticated_client):
        """
        Test updating expense with missing required fields returns 400.
        """
        # Act
        #TODO: Implement test for updating expense with missing fields
        
        # Assert
       #TODO: Implement assertion for updating expense with missing fields
    
    @allure.story("Update Expense")
    @allure.title("Update approved expense returns error")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_update_approved_expense_error(self, authenticated_client, mock_expense_service):
        """
        Test updating an already approved expense returns error.
        """
        # Arrange - Service raises ValueError for non-pending expense
        #TODO: Implement test for updating approved expense
        
        # Act
        #TODO: Implement test for updating approved expense
        
        # Assert
        #TODO: Implement assertion for updating approved expense
    
    # ==================== DELETE EXPENSE TESTS ====================
    
    @allure.story("Delete Expense")
    @allure.title("TC-CTRL-EXP-013: Delete pending expense")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.unit
    def test_delete_expense_success(self, authenticated_client, mock_expense_service):
        """
        Test deleting a pending expense returns success.
        """
        # Arrange
        #TODO: Implement test for deleting a pending expense
        
        # Act
        #TODO: Implement test for deleting a pending expense
        
        # Assert
        #TODO: Implement assertion for deleting a pending expense
    
    @allure.story("Delete Expense")
    @allure.title("TC-CTRL-EXP-014: Delete non-existent expense returns 404")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_delete_expense_not_found(self, authenticated_client, mock_expense_service):
        """
        Test deleting non-existent expense returns 404 Not Found.
        """
        # Arrange
        #TODO: Implement test for deleting non-existent expense
        
        # Act
        #TODO: Implement test for deleting non-existent expense
        
        # Assert
        #TODO: Implement assertion for deleting non-existent expense
    
    @allure.story("Delete Expense")
    @allure.title("Delete approved expense returns error")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_delete_approved_expense_error(self, authenticated_client, mock_expense_service):
        """
        Test deleting an already approved expense returns error.
        """
        # Arrange
        #TODO: Implement test for deleting approved expense
        
        # Act
       #TODO: Implement test for deleting approved expense
        
        # Assert
        #  TODO: Implement assertion for deleting approved expense
    
    @allure.story("Delete Expense")
    @allure.title("Delete expense without authentication")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.unit
    def test_delete_expense_unauthenticated(self, unauthenticated_client):
        """
        Test that unauthenticated delete request returns 401 Unauthorized.
        """
        # Act
        #TODO: Implement test for unauthenticated delete request
        
        # Assert
        # TODO: Implement assertion for unauthenticated delete request


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
