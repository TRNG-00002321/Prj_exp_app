"""
API Tests for Expense Endpoints


- Testing CRUD operations via API
- Testing authorization (401 responses)
- Testing validation (400 responses)

Test Cases Covered: TC-API-007 through TC-API-018
"""
import pytest
import requests
import allure


BASE_URL = "http://localhost:5000"


@allure.epic("Employee App")
@allure.feature("Expense API")
class TestExpenseAPI:
    """
    API tests for expense management endpoints.
    
    IMPORTANT: Flask server must be running on port 5000
    """
    
    @pytest.fixture
    def authenticated_session(self):
        """
        Create an authenticated session for API tests.
        
        This logs in as employee1 and returns a session
        with the JWT cookie set.
        """
        session = requests.Session()
        login_url = f"{BASE_URL}/api/auth/login"
        credentials = {"username": "employee1", "password": "password123"}
        session.post(login_url, json=credentials)
        yield session
        session.close()
    
    @pytest.fixture
    def unauthenticated_session(self):
        """Create a session without authentication."""
        session = requests.Session()
        yield session
        session.close()
    
    @pytest.fixture
    def sample_expense(self):
        """Sample expense data for tests."""
        return {
            "amount": 75.50,
            "description": "API Test Expense",
            "date": "2024-12-21"
        }
    
    # ==================== SUBMIT EXPENSE TESTS ====================
    
    @allure.story("Submit Expense")
    @allure.title("Submit expense successfully when authenticated")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    def test_submit_expense_authenticated(self, authenticated_session, sample_expense):
        """
        Test Case: TC-API-007
        
        Test that authenticated user can submit an expense.
        """
        # Arrange
        url = f"{BASE_URL}/api/expenses"
        
        # Act
        response = authenticated_session.post(url, json=sample_expense)
        
        # Assert
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        json_response = response.json()
        assert "expense" in json_response
        assert json_response["expense"]["amount"] == 75.50
        assert json_response["expense"]["status"] == "pending"
    
    @allure.story("Submit Expense")
    @allure.title("Submit expense fails when not authenticated")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    def test_submit_expense_unauthenticated(self, unauthenticated_session, sample_expense):
        """
        Test Case: TC-API-008
        
        Test that unauthenticated user gets 401.
        """
       
    
    @allure.story("Submit Expense")
    @allure.title("Submit expense fails with invalid amount")
    @allure.severity(allure.severity_level.HIGH)
    @pytest.mark.api
    def test_submit_expense_invalid_amount(self, authenticated_session):
        """
        Test Case: TC-API-009
        
        Test validation of amount field.
        """
       
    
    # ==================== GET EXPENSES TESTS ====================
    
    @allure.story("Get Expenses")
    @allure.title("Get all expenses when authenticated")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    def test_get_expenses_authenticated(self, authenticated_session):
        """
        Test Case: TC-API-010
        
        Test retrieving all expenses for authenticated user.
        """
       
    
    @allure.story("Get Expenses")
    @allure.title("Get expenses fails when not authenticated")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    def test_get_expenses_unauthenticated(self, unauthenticated_session):
        """
        Test Case: TC-API-011
        
        Test that unauthenticated access is denied.
        """
       
    
    @allure.story("Get Expenses")
    @allure.title("Filter expenses by pending status")
    @pytest.mark.api
    def test_get_expenses_filter_pending(self, authenticated_session):
        """
        Test Case: TC-API-012
        
        Test filtering expenses by status query parameter.
        """
       
    
    # ==================== GET SINGLE EXPENSE TESTS ====================
    
    @allure.story("Get Single Expense")
    @allure.title("Get expense by ID when owner")
    @pytest.mark.api
    def test_get_expense_by_id_owner(self, authenticated_session, sample_expense):
        """
        Test Case: TC-API-013
        
        Test getting a specific expense by ID.
        """
        # First create an expense
        
            
            # Now get it
           
    
    @allure.story("Get Single Expense")
    @allure.title("Get non-existent expense returns 404")
    @pytest.mark.api
    def test_get_expense_not_found(self, authenticated_session):
        """
        Test Case: TC-API-014 (variant)
        
        Test that non-existent expense returns 404.
        """
       
    
    # ==================== UPDATE EXPENSE TESTS ====================
    
    @allure.story("Update Expense")
    @allure.title("Update pending expense successfully")
    @pytest.mark.api
    def test_update_expense_pending(self, authenticated_session, sample_expense):
        """
        Test Case: TC-API-015
        
        Test updating a pending expense.
        """
        # Create expense first
        
            
            # Update it
           
    
    # ==================== DELETE EXPENSE TESTS ====================
    
    @allure.story("Delete Expense")
    @allure.title("Delete pending expense successfully")
    @pytest.mark.api
    def test_delete_expense_pending(self, authenticated_session, sample_expense):
        """
        Test Case: TC-API-017
        
        Test deleting a pending expense.
        """
        # Create expense first
        create_url = f"{BASE_URL}/api/expenses"
        
            
            # Delete it
            

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
