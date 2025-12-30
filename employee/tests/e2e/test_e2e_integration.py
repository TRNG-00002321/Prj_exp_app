"""
E2E Integration Tests with Real Database (Python Employee App)
Created: 2024-12-29T19:19:00-06:00

These tests simulate end-to-end user workflows using Flask test client
with a REAL SQLite database backend.

- E2E testing with real database
- Complete workflow testing (login → action → verify)
- Session handling in tests
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
    """Create Flask test application with real database."""
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


@allure.epic("Employee App")
@allure.feature("E2E Integration Tests")
class TestLoginWorkflowE2E:
    """End-to-end login workflow tests."""
    
    @allure.story("Login Flow")
    @allure.title("TC-E2E-INT-001: Complete login workflow with real database")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.e2e
    @pytest.mark.integration
    def test_complete_login_workflow(self, client):
        """Test complete login workflow with seeded user."""
        # Step 1: Access login page
        response = client.get('/')
        assert response.status_code == 200
        
        # Step 2: Login with valid credentials
        login_response = client.post('/api/auth/login',
                                    data=json.dumps({
                                        'username': 'employee1',
                                        'password': 'password123'
                                    }),
                                    content_type='application/json')
        
        assert login_response.status_code == 200
        
        # Step 3: Access protected resource
        expenses_response = client.get('/api/expenses')
        assert expenses_response.status_code == 200
        
        # Step 4: Logout
        logout_response = client.post('/api/auth/logout')
        assert logout_response.status_code in [200, 302]
    
    @allure.story("Login Flow")
    @allure.title("TC-E2E-INT-002: Failed login blocks access")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.e2e
    @pytest.mark.integration
    def test_failed_login_blocks_access(self, client):
        """Test that failed login prevents access to protected resources."""
        # Step 1: Try login with wrong password
        
        
        # Step 2: Try to access protected resource - should fail
        


@allure.epic("Employee App")
@allure.feature("E2E Integration Tests")
class TestExpenseWorkflowE2E:
    """End-to-end expense management workflow tests."""
    
    @allure.story("Expense Submission")
    @allure.title("TC-E2E-INT-003: Complete expense submission workflow")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.e2e
    @pytest.mark.integration
    def test_complete_expense_submission_workflow(self, client):
        """Test complete workflow: login → submit expense → verify."""
        # Step 1: Login
      
        
        # Step 2: Get initial expense count
       
        
        # Step 3: Submit new expense
       
        
        # Step 4: Verify expense appears in list
       
        
        # Should have one more expense
        
    
    @allure.story("Expense View")
    @allure.title("TC-E2E-INT-004: View expense list from seeded data")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.e2e
    @pytest.mark.integration
    def test_view_seeded_expenses(self, client):
        """Test viewing expenses from seeded database."""
        # Login
      
        
        # Get expenses
       
      
        
        # Employee1 has 3 expenses in seed data (IDs 1, 2, 3)
        # May have more if previous tests added expenses
      
    
    @allure.story("Expense Update")
    @allure.title("TC-E2E-INT-005: Update pending expense workflow")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.e2e
    @pytest.mark.integration
    def test_update_expense_workflow(self, client):
        """Test updating a pending expense."""
        # Login
      
        
        # Create a new expense to update
      
        
     
                # Update the expense
              
                
                # Should succeed or may fail if already approved
             


@allure.epic("Employee App")
@allure.feature("E2E Integration Tests")
class TestMultiUserWorkflowE2E:
    """Multi-user workflow tests."""
    
    @allure.story("Multi-User")
    @allure.title("TC-E2E-INT-006: Different users see different expenses")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.e2e
    @pytest.mark.integration
    def test_different_users_different_expenses(self, client):
        """Test that different users only see their own expenses."""
        # Login as employee1 and get their expenses
    
        
        # Logout
        client.post('/api/auth/logout')
        
        # Login as employee2 and get their expenses
        
        
       
            # Both should have data but different counts
            # (employee1 has 3, employee2 has 2 in seed data)
           
            
            # They should have different expense counts
           


if __name__ == '__main__':
    pytest.main([__file__, '-v', '-m', 'e2e or integration'])
