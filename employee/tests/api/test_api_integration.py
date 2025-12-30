"""
API Integration Tests with Real Database (Python Employee App)


These tests use the Flask test client with a REAL SQLite database.
The test database is created at a SEPARATE PATH from production.


- API testing with real database backend
- Flask test client usage
- End-to-end API flow testing
"""
import pytest
import os
import sys
import json
import allure

# Add parent directories to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from repository.database import DatabaseConnection


# Test database path - SEPARATE from production
TEST_DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                            'integration', 'test_expense_manager.db')
SEED_SQL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                             'integration', 'seed_data_20241229.sql')


@pytest.fixture(scope='module')
def test_app():
    """
    Create Flask test application with real database.
    """
    # Initialize test database
    db_conn = DatabaseConnection(TEST_DB_PATH)
    db_conn.initialize_database()
    
    # Load seed data
    with open(SEED_SQL_PATH, 'r') as f:
        seed_sql = f.read()
    
    with db_conn.get_connection() as conn:
        conn.executescript(seed_sql)
        conn.commit()
    
    # Set environment variable for app to use test database
    os.environ['DATABASE_PATH'] = TEST_DB_PATH
    
    # Import and create app after setting env var
    from main import create_app
    app = create_app()
    app.config['TESTING'] = True
    
    yield app
    
    # Cleanup
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
    if 'DATABASE_PATH' in os.environ:
        del os.environ['DATABASE_PATH']


@pytest.fixture
def client(test_app):
    """Create Flask test client."""
    return test_app.test_client()


@pytest.fixture
def authenticated_client(client):
    """Create authenticated client session."""
    # Login as employee1
    response = client.post('/api/auth/login', 
                          data=json.dumps({
                              'username': 'employee1',
                              'password': 'password123'
                          }),
                          content_type='application/json')
    
    # The test client automatically handles cookies
    return client


@allure.epic("Employee App")
@allure.feature("API Integration Tests")
class TestAuthApiIntegration:
    """API Authentication tests with real database."""
    
    @allure.story("Login")
    @allure.title("TC-API-INT-001: Login with valid credentials from seeded data")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.integration
    def test_login_valid_credentials_real_db(self, client):
        """Test login with credentials from seeded database."""
        response = client.post('/api/auth/login',
                              data=json.dumps({
                                  'username': 'employee1',
                                  'password': 'password123'
                              }),
                              content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data.get('success') == True
        assert 'jwt_token' in response.headers.get('Set-Cookie', '')
    
    @allure.story("Login")
    @allure.title("TC-API-INT-002: Login with invalid password")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.integration
    def test_login_invalid_password_real_db(self, client):
        """Test login with wrong password."""
       
    
    @allure.story("Login")
    @allure.title("TC-API-INT-003: Login with non-existent user")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.integration
    def test_login_nonexistent_user(self, client):
        """Test login with user not in database."""
       


@allure.epic("Employee App")
@allure.feature("API Integration Tests")
class TestExpenseApiIntegration:
    """Expense API tests with real database."""
    
    @allure.story("Get Expenses")
    @allure.title("TC-API-INT-004: Get expenses for authenticated user")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.integration
    def test_get_expenses_authenticated_real_db(self, authenticated_client):
        """Test getting expenses from seeded database."""
      
        
        # Should have expenses from seed data (employee1 has 3 expenses)
        
    
    @allure.story("Get Expenses")
    @allure.title("TC-API-INT-005: Get expenses unauthenticated returns 401")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.integration
    def test_get_expenses_unauthenticated(self, client):
        """Test that unauthenticated access is rejected."""
       
    
    @allure.story("Submit Expense")
    @allure.title("TC-API-INT-006: Submit new expense with real database")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.integration
    def test_submit_expense_real_db(self, authenticated_client):
        """Test submitting a new expense to real database."""
      
        
        # Should succeed
       
        # Verify expense was created with an ID
       
    
    @allure.story("Submit Expense")
    @allure.title("TC-API-INT-007: Submit expense with invalid amount")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.integration
    def test_submit_expense_invalid_amount(self, authenticated_client):
        """Test validation of amount field."""
       
        
       
        
        # Should fail validation
        
    
    @allure.story("Get Expense")
    @allure.title("TC-API-INT-008: Get specific expense by ID from seeded data")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.integration
    def test_get_expense_by_id_real_db(self, authenticated_client):
        """Test getting a specific expense from seeded database."""
        # Expense ID 1 exists in seed data for employee1
       
        
        # May return 200 or 403 depending on ownership logic
        
        
       


@allure.epic("Employee App")
@allure.feature("API Integration Tests")
class TestHealthCheckIntegration:
    """Health check endpoint tests."""
    
    @allure.story("Health")
    @allure.title("TC-API-INT-009: Health check endpoint")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.integration
    def test_health_check(self, client):
        """Test health check endpoint."""
      

if __name__ == '__main__':
    pytest.main([__file__, '-v', '-m', 'integration'])
