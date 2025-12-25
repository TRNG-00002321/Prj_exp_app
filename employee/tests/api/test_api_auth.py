"""
API Tests for Authentication Endpoints

Test Cases Covered: TC-API-001 through TC-API-006
"""
import pytest
import requests
import allure
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


# Base URL for the Employee API
BASE_URL = "http://localhost:5000"


@allure.epic("Employee App")
@allure.feature("Authentication API")
class TestAuthenticationAPI:
    """
    API tests for authentication endpoints.
    
    IMPORTANT: These tests require the Flask server to be running.
    Start the server with: python main.py
    - Using requests library for HTTP calls
    - Session management with cookies
    - Testing different HTTP methods (POST, GET)
    """
    
    @pytest.fixture
    def api_session(self):
        """
        Create a requests session for API testing.
        
        A session maintains cookies across requests,
        which is needed for JWT authentication.
        """
        session = requests.Session()
        yield session
        session.close()
    
    @pytest.fixture
    def valid_credentials(self):
        """Valid employee credentials for testing."""
        return {
            "username": "employee1",
            "password": "password123"
        }
    
    @pytest.fixture
    def invalid_credentials(self):
        """Invalid credentials for testing."""
        return {
            "username": "employee1",
            "password": "wrongpassword"
        }
    
    # ==================== LOGIN TESTS ====================
    
    @allure.story("Login Endpoint")
    @allure.title("Successful login with valid credentials")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.api
    def test_login_success(self, api_session, valid_credentials):
        """
        Test Case: TC-API-001
        
        Test successful login returns 200 and sets JWT cookie.
        
        - POST request with JSON body
        - Checking response status codes
        - Verifying response JSON structure
        - Checking cookies are set
        """
        # Arrange
        url = f"{BASE_URL}/api/auth/login"
        
        # Act
        response = api_session.post(url, json=valid_credentials)
        
        # Assert
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        # Check response body
        json_response = response.json()
        assert "message" in json_response, "Response should have 'message' field"
        assert "user" in json_response, "Response should have 'user' field"
        assert json_response["user"]["username"] == "employee1"
        
        # Check JWT cookie was set
        assert "jwt_token" in api_session.cookies, "JWT cookie should be set"
    
    @allure.story("Login Endpoint")
    @allure.title("Login fails with invalid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    def test_login_invalid_credentials(self, api_session, invalid_credentials):
        """
        Test Case: TC-API-002
        
        Test that invalid credentials return 401 Unauthorized.
        
       - Testing sad path / negative case
        - Validating error responses
        """
        # Arrange
       
        
        # Act
       
        
        # Assert
       
    
    @allure.story("Login Endpoint")
    @allure.title("Login fails with missing username")
    @allure.severity(allure.severity_level.HIGH)
    @pytest.mark.api
    def test_login_missing_username(self, api_session):
        """
        Test Case: TC-API-003
        
        Test that missing username returns 400 Bad Request.
        """
        # Arrange
      
        
        # Act
       
        
        # Assert
       
    
    @allure.story("Login Endpoint")
    @allure.title("Login fails with missing password")
    @pytest.mark.api
    def test_login_missing_password(self, api_session):
        """
        Test that missing password returns 400 Bad Request.
        """
        # Arrange
       
        
        # Act
      
        
        # Assert
       
    
    # ==================== LOGOUT TESTS ====================
    
    @allure.story("Logout Endpoint")
    @allure.title("Successful logout clears cookie")
    @allure.severity(allure.severity_level.HIGH)
    @pytest.mark.api
    def test_logout_success(self, api_session, valid_credentials):
        """
        Test Case: TC-API-004
        
        Test that logout clears the JWT cookie.
        
        - Sequential API calls (login then logout)
        - Verifying cookie behavior
        """
        # Arrange - First login
       
        
        # Act - Logout
        
        
        # Assert
       
    
    # ==================== STATUS TESTS ====================
    
    @allure.story("Status Endpoint")
    @allure.title("Status returns unauthenticated when no cookie")
    @allure.severity(allure.severity_level.HIGH)
    @pytest.mark.api
    def test_status_unauthenticated(self, api_session):
        """
        Test Case: TC-API-005
        
        Test auth status when not logged in.
        """
        # Arrange
       
        
        # Act
       
        
        # Assert
       
    @allure.story("Status Endpoint")
    @allure.title("Status returns authenticated after login")
    @allure.severity(allure.severity_level.HIGH)
    @pytest.mark.api
    def test_status_authenticated(self, api_session, valid_credentials):
        """
        Test Case: TC-API-006
        
        Test auth status after successful login.
        """
        # Arrange - Login first
       
        
        # Act
        
        
        # Assert
       


if __name__ == '__main__':
    print("NOTE: Start the Flask server before running API tests.")
    print("Run: python main.py")
    print()
    pytest.main([__file__, '-v'])
