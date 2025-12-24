"""
Unit Tests for Repository Layer (Python Employee App)
- Testing database operations with mocked connections
- Mocking SQLite cursor and connection objects
- Testing CRUD operations in isolation

"""
import pytest
from unittest.mock import MagicMock, patch
import allure
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from repository.user_repository import UserRepository
from repository.expense_repository import ExpenseRepository
from repository.approval_repository import ApprovalRepository
from repository.user_model import User
from repository.expense_model import Expense
from repository.approval_model import Approval


@allure.epic("Employee App")
@allure.feature("User Repository")
class TestUserRepository:
    """Test suite for UserRepository class."""
    
    @pytest.fixture
    def mock_db_connection(self):
        """Create mock database connection."""
        return MagicMock()
    
    @pytest.fixture
    def user_repository(self, mock_db_connection):
        """Create UserRepository with mock connection."""
        return UserRepository(mock_db_connection)
    
    @pytest.fixture
    def mock_cursor(self):
        """Create mock cursor with row data."""
        cursor = MagicMock()
        return cursor
    
    # ==================== FIND BY USERNAME TESTS ====================
    
    @allure.story("Find User")
    @allure.title("TC-REPO-USER-001: Find user by username - found")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.unit
    def test_find_by_username_found(self, user_repository, mock_db_connection):
        """Test finding existing user by username."""
        # Arrange
        mock_row = {'id': 1, 'username': 'employee1', 'password': 'password123', 'role': 'Employee'}
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = mock_row
        mock_conn = MagicMock()
        mock_conn.execute.return_value = mock_cursor
        mock_conn.__enter__ = MagicMock(return_value=mock_conn)
        mock_conn.__exit__ = MagicMock(return_value=False)
        mock_db_connection.get_connection.return_value = mock_conn
        
        # Act
        result = user_repository.find_by_username('employee1')
        
        # Assert
        assert result is not None
        assert result.id == 1
        assert result.username == 'employee1'
        assert result.role == 'Employee'
    
    @allure.story("Find User")
    @allure.title("TC-REPO-USER-002: Find user by username - not found")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_find_by_username_not_found(self, user_repository, mock_db_connection):
        """Test finding non-existent user by username."""
        # Arrange
        
        
        # Act
       
        
        # Assert
       
    
    # ==================== FIND BY ID TESTS ====================
    
    @allure.story("Find User")
    @allure.title("TC-REPO-USER-003: Find user by ID - found")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_find_by_id_found(self, user_repository, mock_db_connection):
        """Test finding existing user by ID."""
        # Arrange
        
        
        # Act
        
        
        # Assert
        
    
    @allure.story("Find User")
    @allure.title("TC-REPO-USER-004: Find user by ID - not found")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_find_by_id_not_found(self, user_repository, mock_db_connection):
        """Test finding non-existent user by ID."""
        # Arrange
       
        
        # Act
       
        
        # Assert
       
    
    # ==================== CREATE USER TESTS ====================
    
    @allure.story("Create User")
    @allure.title("TC-REPO-USER-005: Create new user")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.unit
    def test_create_user(self, user_repository, mock_db_connection):
        """Test creating a new user."""
        # Arrange
        mock_cursor = MagicMock()
        mock_cursor.lastrowid = 5
        mock_conn = MagicMock()
        mock_conn.execute.return_value = mock_cursor
        mock_conn.__enter__ = MagicMock(return_value=mock_conn)
        mock_conn.__exit__ = MagicMock(return_value=False)
        mock_db_connection.get_connection.return_value = mock_conn
        
        new_user = User(id=None, username='newuser', password='newpass', role='Employee')
        
        # Act
        result = user_repository.create(new_user)
        
        # Assert
        assert result.id == 5
        mock_conn.commit.assert_called_once()


@allure.epic("Employee App")
@allure.feature("Expense Repository")
class TestExpenseRepository:
    """Test suite for ExpenseRepository class."""
    
    @pytest.fixture
    def mock_db_connection(self):
        """Create mock database connection."""
        return MagicMock()
    
    @pytest.fixture
    def expense_repository(self, mock_db_connection):
        """Create ExpenseRepository with mock connection."""
        return ExpenseRepository(mock_db_connection)
    
    # ==================== CREATE EXPENSE TESTS ====================
    
    @allure.story("Create Expense")
    @allure.title("TC-REPO-EXP-001: Create new expense with approval")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.unit
    def test_create_expense(self, expense_repository, mock_db_connection):
        """Test creating a new expense with initial approval record."""
        # Arrange
       
        
        # Act
       
        
        # Assert
       
    
    # ==================== FIND BY ID TESTS ====================
    
    @allure.story("Find Expense")
    @allure.title("TC-REPO-EXP-002: Find expense by ID - found")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_find_by_id_found(self, expense_repository, mock_db_connection):
        """Test finding existing expense by ID."""
        # Arrange
        
        
        # Act
       
        
        # Assert
       
    
    @allure.story("Find Expense")
    @allure.title("TC-REPO-EXP-003: Find expense by ID - not found")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_find_by_id_not_found(self, expense_repository, mock_db_connection):
        """Test finding non-existent expense by ID."""
        # Arrange
        
        
        # Act
       
        
        # Assert
        
    
    # ==================== FIND BY USER ID TESTS ====================
    
    @allure.story("Find Expenses")
    @allure.title("TC-REPO-EXP-004: Find expenses by user ID")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_find_by_user_id(self, expense_repository, mock_db_connection):
        """Test finding all expenses for a user."""
        # Arrange
       
        
        # Act
        
        
        # Assert
        
    
    @allure.story("Find Expenses")
    @allure.title("TC-REPO-EXP-005: Find expenses by user ID - empty")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.unit
    def test_find_by_user_id_empty(self, expense_repository, mock_db_connection):
        """Test finding expenses for user with none."""
        # Arrange
      
        
        # Act
        
        
        # Assert
        
    
    # ==================== UPDATE EXPENSE TESTS ====================
    
    @allure.story("Update Expense")
    @allure.title("TC-REPO-EXP-006: Update expense")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_update_expense(self, expense_repository, mock_db_connection):
        """Test updating an expense."""
        # Arrange
       
        
        # Act
       
        
        # Assert
        
    
    # ==================== DELETE EXPENSE TESTS ====================
    
    @allure.story("Delete Expense")
    @allure.title("TC-REPO-EXP-007: Delete expense - success")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_delete_expense_success(self, expense_repository, mock_db_connection):
        """Test deleting an expense successfully."""
        # Arrange
       
        
        # Act
       
        
        # Assert
       
    
    @allure.story("Delete Expense")
    @allure.title("TC-REPO-EXP-008: Delete expense - not found")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.unit
    def test_delete_expense_not_found(self, expense_repository, mock_db_connection):
        """Test deleting non-existent expense."""
        # Arrange
       
        
        # Act
       
        
        # Assert
       


@allure.epic("Employee App")
@allure.feature("Approval Repository")
class TestApprovalRepository:
    """Test suite for ApprovalRepository class."""
    
    @pytest.fixture
    def mock_db_connection(self):
        """Create mock database connection."""
        return MagicMock()
    
    @pytest.fixture
    def approval_repository(self, mock_db_connection):
        """Create ApprovalRepository with mock connection."""
        return ApprovalRepository(mock_db_connection)
    
    # ==================== FIND BY EXPENSE ID TESTS ====================
    
    @allure.story("Find Approval")
    @allure.title("TC-REPO-APR-001: Find approval by expense ID - found")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_find_by_expense_id_found(self, approval_repository, mock_db_connection):
        """Test finding approval by expense ID."""
        # Arrange
       
        
        # Act
       
        
        # Assert
       
    @allure.story("Find Approval")
    @allure.title("TC-REPO-APR-002: Find approval by expense ID - not found")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_find_by_expense_id_not_found(self, approval_repository, mock_db_connection):
        """Test finding non-existent approval."""
        # Arrange
       
        
        # Act
       
        
        # Assert
        
    
    # ==================== UPDATE STATUS TESTS ====================
    
    @allure.story("Update Approval")
    @allure.title("TC-REPO-APR-003: Update approval status - success")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.unit
    def test_update_status_success(self, approval_repository, mock_db_connection):
        """Test updating approval status."""
        # Arrange
       
        
        # Act
        
        
        # Assert
       
    
    @allure.story("Update Approval")
    @allure.title("TC-REPO-APR-004: Update approval status - not found")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.unit
    def test_update_status_not_found(self, approval_repository, mock_db_connection):
        """Test updating non-existent approval."""
        # Arrange
       
        
        # Act
       
        
        # Assert
       


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
