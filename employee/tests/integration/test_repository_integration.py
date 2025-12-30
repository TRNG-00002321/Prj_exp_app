"""
Integration Tests for Repository Layer (Python Employee App)

These tests use a REAL SQLite database to verify repository operations.
The test database is created at a SEPARATE PATH from the production database.


- Testing with real database connections (vs mocked)
- Database setup and teardown patterns
- Integration test isolation
"""
import pytest
import sqlite3
import os
import sys
import allure

# Add parent directories to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from repository.database import DatabaseConnection
from repository.user_repository import UserRepository
from repository.expense_repository import ExpenseRepository
from repository.approval_repository import ApprovalRepository
from repository.user_model import User
from repository.expense_model import Expense
from repository.approval_model import Approval


# Test database path - SEPARATE from production
TEST_DB_PATH = os.path.join(os.path.dirname(__file__), 'test_expense_manager.db')
SEED_SQL_PATH = os.path.join(os.path.dirname(__file__), 'seed_data_20241229.sql')


@pytest.fixture(scope='module')
def test_db_connection():
    """
    Create a real database connection for integration testing.
    Uses a separate test database file.
    
    Scope is 'module' to reuse connection across all tests in this file.
    """
    # Create database connection with test path
    db_conn = DatabaseConnection(TEST_DB_PATH)
    
    # Initialize database schema
    db_conn.initialize_database()
    
    # Load and execute seed data
    with open(SEED_SQL_PATH, 'r') as f:
        seed_sql = f.read()
    
    with db_conn.get_connection() as conn:
        conn.executescript(seed_sql)
        conn.commit()
    
    yield db_conn
    
    # Cleanup: remove test database after tests
   # if os.path.exists(TEST_DB_PATH):
    #    os.remove(TEST_DB_PATH)


@pytest.fixture
def user_repository(test_db_connection):
    """Create UserRepository with real database connection."""
    return UserRepository(test_db_connection)


@pytest.fixture
def expense_repository(test_db_connection):
    """Create ExpenseRepository with real database connection."""
    return ExpenseRepository(test_db_connection)


@pytest.fixture
def approval_repository(test_db_connection):
    """Create ApprovalRepository with real database connection."""
    return ApprovalRepository(test_db_connection)


@allure.epic("Employee App")
@allure.feature("User Repository Integration")
class TestUserRepositoryIntegration:
    """Integration tests for UserRepository with real database."""
    
    @allure.story("Find User")
    @allure.title("TC-INT-USER-001: Find user by username from real database")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.integration
    def test_find_by_username_real_db(self, user_repository):
        """Test finding user by username from seeded database."""
        # Act
        result = user_repository.find_by_username('employee1')
        
        # Assert
        assert result is not None
        assert result.id == 1
        assert result.username == 'employee1'
        assert result.role == 'Employee'
    
    @allure.story("Find User")
    @allure.title("TC-INT-USER-002: Find user by ID from real database")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.integration
    def test_find_by_id_real_db(self, user_repository):
        """Test finding user by ID from seeded database."""
        # Act
       
        
        # Assert
       
    
    @allure.story("Find User")
    @allure.title("TC-INT-USER-003: Find non-existent user returns None")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.integration
    def test_find_nonexistent_user(self, user_repository):
        """Test finding non-existent user returns None."""
        # Act
       
        
        # Assert
       
    
    @allure.story("Create User")
    @allure.title("TC-INT-USER-004: Create new user in real database")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.integration
    def test_create_user_real_db(self, user_repository):
        """Test creating a new user in real database."""
        # Arrange
        
        
        # Act
       
        
        # Assert
       
        
        # Verify by finding the user
        


@allure.epic("Employee App")
@allure.feature("Expense Repository Integration")
class TestExpenseRepositoryIntegration:
    """Integration tests for ExpenseRepository with real database."""
    
    @allure.story("Find Expense")
    @allure.title("TC-INT-EXP-001: Find expense by ID from real database")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.integration
    def test_find_by_id_real_db(self, expense_repository):
        """Test finding expense by ID from seeded database."""
        # Act
        result = expense_repository.find_by_id(1)
        
        # Assert
        assert result is not None
        assert result.id == 1
        assert result.amount == 150.00
        assert result.description == 'Business lunch'
    
    @allure.story("Find Expense")
    @allure.title("TC-INT-EXP-002: Find expenses by user ID from real database")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.integration
    def test_find_by_user_id_real_db(self, expense_repository):
        """Test finding all expenses for a user from seeded database."""
        # Act
       
        
        # Assert
       
    
    @allure.story("Create Expense")
    @allure.title("TC-INT-EXP-003: Create new expense in real database")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.integration
    def test_create_expense_real_db(self, expense_repository, approval_repository):
        """Test creating a new expense with approval record."""
        # Arrange
       
        
        # Act
        
        
        # Assert
        
        
        # Verify approval record was created
       
    
    @allure.story("Update Expense")
    @allure.title("TC-INT-EXP-004: Update expense in real database")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.integration
    def test_update_expense_real_db(self, expense_repository):
        """Test updating an expense in real database."""
        # Arrange - first find an expense
       
        
        # Modify the expense
       
        
        # Act
        
        
        # Assert
       
        
        # Verify by fetching again
       
    
    @allure.story("Delete Expense")
    @allure.title("TC-INT-EXP-005: Delete expense from real database")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.integration
    def test_delete_expense_real_db(self, expense_repository):
        """Test deleting an expense and its approval record."""
        # Create an expense to delete
       
        
        # Act
       
        
        # Assert
       
        
        # Verify expense is gone
       

@allure.epic("Employee App")
@allure.feature("Approval Repository Integration")
class TestApprovalRepositoryIntegration:
    """Integration tests for ApprovalRepository with real database."""
    
    @allure.story("Find Approval")
    @allure.title("TC-INT-APR-001: Find approval by expense ID from real database")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.integration
    def test_find_by_expense_id_real_db(self, approval_repository):
        """Test finding approval by expense ID from seeded database."""
        # Act
       
        
        # Assert
       
    
    @allure.story("Find Approval")
    @allure.title("TC-INT-APR-002: Find pending approval from real database")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.integration
    def test_find_pending_approval_real_db(self, approval_repository):
        """Test finding pending approval from seeded database."""
        # Act
       
        
        # Assert
       
    
    @allure.story("Update Approval")
    @allure.title("TC-INT-APR-003: Update approval status in real database")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.integration
    def test_update_status_real_db(self, approval_repository):
        """Test updating approval status in real database."""
        # Act
      
        
        # Assert
      
        
        # Verify by finding the approval
      
    
    @allure.story("Find with Status")
    @allure.title("TC-INT-APR-004: Find expenses with status for user")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.integration
    def test_find_expenses_with_status_real_db(self, approval_repository):
        """Test finding expenses with approval status for a user."""
        # Act
      
        
        # Assert
      
        
        # Check structure of returned tuples
      


if __name__ == '__main__':
    pytest.main([__file__, '-v', '-m', 'integration'])
