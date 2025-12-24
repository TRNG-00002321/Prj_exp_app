"""
Pytest configuration and shared fixtures for all tests.

This file is automatically discovered by pytest and provides:
- Shared test fixtures for database, services, and Flask app
- Allure reporting integration
- Test data setup and teardown

"""
import pytest
import allure
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture(scope="session")
def mock_db_connection():
    """
    Create a mock database connection for testing.
    Scope is 'session' to reuse across all tests.

    """
    from unittest.mock import MagicMock
    mock_conn = MagicMock()
    return mock_conn


@pytest.fixture
def mock_user_repository(mock_db_connection):
    """
    Create a mock UserRepository for testing services.

    """
    from unittest.mock import MagicMock
    from repository.user_model import User
    
    mock_repo = MagicMock()
    
    # Setup default behavior for common operations
    test_user = User(id=1, username="testuser", password="password123", role="Employee")
    mock_repo.find_by_username.return_value = test_user
    mock_repo.find_by_id.return_value = test_user
    
    return mock_repo


@pytest.fixture
def mock_expense_repository(mock_db_connection):
    """
    Create a mock ExpenseRepository for testing services.
    """
    from unittest.mock import MagicMock
    from repository.expense_model import Expense
    
    mock_repo = MagicMock()
    
    # Setup default behavior
    test_expense = Expense(id=1, user_id=1, amount=100.00, description="Test expense", date="2024-01-01")
    mock_repo.find_by_id.return_value = test_expense
    mock_repo.create.return_value = test_expense
    
    return mock_repo


@pytest.fixture
def mock_approval_repository(mock_db_connection):
    """
    Create a mock ApprovalRepository for testing services.
    """
    from unittest.mock import MagicMock
    from repository.approval_model import Approval
    
    mock_repo = MagicMock()
    
    # Setup default behavior
    test_approval = Approval(id=1, expense_id=1, status="pending", reviewer=None, comment=None, review_date=None)
    mock_repo.find_by_expense_id.return_value = test_approval
    
    return mock_repo


@pytest.fixture
def flask_app():
    """
    Create Flask test application.

    """
    from main import create_app
    app = create_app()
    app.config['TESTING'] = True
    return app


@pytest.fixture
def client(flask_app):
    """
    Create Flask test client for API testing.
    """
    return flask_app.test_client()


@pytest.fixture
def auth_headers():
    """
    Create authorization headers for API tests.
    Returns a function to generate headers with a JWT token.
    """
    def _get_headers(token=None):
        headers = {'Content-Type': 'application/json'}
        if token:
            headers['Cookie'] = f'jwt_token={token}'
        return headers
    return _get_headers


@pytest.fixture
def sample_expense_data():
    """
    Provide sample expense data for tests.

    """
    return {
        'amount': 100.00,
        'description': 'Business lunch',
        'date': '2024-12-21'
    }


@pytest.fixture
def sample_user_data():
    """
    Provide sample user data for tests.
    """
    return {
        'username': 'employee1',
        'password': 'password123'
    }


# Allure reporting helpers
@allure.step("Validate response status code")
def assert_status_code(response, expected_code):
    """Helper to validate status codes with Allure step."""
    assert response.status_code == expected_code, \
        f"Expected {expected_code}, got {response.status_code}"


@allure.step("Validate response contains key")
def assert_response_has_key(response_json, key):
    """Helper to validate response structure with Allure step."""
    assert key in response_json, f"Response missing key: {key}"
