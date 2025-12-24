# Notes: Employee App (Python) - Testing Strategy

## Overview
This guide explains **when, why, and where** to apply each testing technique in the Python Employee application. Each section includes real examples from the codebase.

---

## The Testing Pyramid

```
        /\
       /E2E\         ← Few tests, expensive, slow
      /------\
     /  API   \      ← Some tests, medium cost
    /----------\
   / Unit Tests \    ← Many tests, cheap, fast
  /--------------\
```

| Level | Speed | Cost | Confidence | Count |
|-------|-------|------|------------|-------|
| Unit | Fast (ms) | Low | Component-level | Many |
| API/Integration | Medium (s) | Medium | Contract-level | Some |
| E2E | Slow (min) | High | System-level | Few |

---

## 1. Unit Tests - When & Why

### When to Use Unit Tests
1. **Testing business logic** in services
2. **Validating input/output** of functions
3. **Testing edge cases** and error handling
4. **Quick feedback** during development

### Why Unit Tests for Business Logic

**Example: ExpenseService Validation**

```python
# service/expense_service.py
def submit_expense(self, user_id, amount, description, date=None):
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")
    if not description or description.strip() == "":
        raise ValueError("Description is required")
```

**Why unit test this?**
- ✅ **Isolated logic**: No database, no HTTP, no external dependencies
- ✅ **Fast execution**: Runs in milliseconds
- ✅ **Many edge cases**: Test 0, negative, empty string, whitespace
- ✅ **Clear cause of failure**: If test fails, you know exactly what's broken

**Test Example:**
```python
# tests/unit/test_expense_service.py
def test_submit_expense_zero_amount(self, expense_service):
    """Test Case: TC-EXP-002 - Business rule validation"""
    with pytest.raises(ValueError) as exc_info:
        expense_service.submit_expense(user_id=1, amount=0, description="Test")
    assert "Amount must be greater than 0" in str(exc_info.value)
```

---

## 2. Mocking - When, Why, Where

### What is Mocking?
Mocking replaces real objects with **fake objects** that you control. This isolates the code under test.

### When to Use Mocks

| Use Mock When... | Don't Mock When... |
|------------------|-------------------|
| Testing services that call repositories | Testing the repository itself |
| Avoiding database operations | You need to verify database SQL |
| Simulating error conditions | Integration testing is the goal |
| Speeding up test execution | Testing real interactions |

### Why Mock? - The Dependency Problem

**Problem:** `AuthenticationService` uses `UserRepository`

```python
# service/authentication_service.py
class AuthenticationService:
    def __init__(self, user_repository, jwt_secret_key='secret'):
        self.user_repository = user_repository  # DEPENDENCY!
    
    def authenticate_user(self, username, password):
        user = self.user_repository.find_by_username(username)  # DB call!
        if user and user.password == password:
            return user
        return None
```

**Without mocking:**
- ❌ Need real database with test data
- ❌ Tests are slow (database I/O)
- ❌ Tests can fail due to database issues
- ❌ Hard to test "user not found" scenario

**With mocking:**
- ✅ No database needed
- ✅ Tests run in milliseconds
- ✅ Control exactly what repository returns
- ✅ Easy to simulate any scenario

### Where to Mock - The Boundary Rule

**Mock at the layer boundary:**

```
┌─────────────────┐
│   Controller    │  ← Mock: Service layer
├─────────────────┤
│    Service      │  ← Mock: Repository layer (MOST COMMON)
├─────────────────┤
│   Repository    │  ← Mock: Database connection
├─────────────────┤
│    Database     │
└─────────────────┘
```

**In this project, we mock repositories when testing services:**

```python
# tests/unit/test_authentication_service.py
@pytest.fixture
def mock_user_repo(self):
    """Mock the repository layer"""
    return MagicMock()

@pytest.fixture
def auth_service(self, mock_user_repo):
    """Inject mock into service"""
    return AuthenticationService(mock_user_repo, jwt_secret_key='test-secret')
```

### Mock Techniques

#### 1. return_value - Simulate success
```python
mock_user_repo.find_by_username.return_value = User(id=1, username='test', ...)
result = auth_service.authenticate_user('test', 'password')
assert result is not None
```

#### 2. return_value = None - Simulate "not found"
```python
mock_user_repo.find_by_username.return_value = None
result = auth_service.authenticate_user('unknown', 'any')
assert result is None
```

#### 3. side_effect - Simulate exceptions
```python
mock_repo.find_by_id.side_effect = DatabaseError("Connection failed")
with pytest.raises(DatabaseError):
    service.get_expense(1)
```

---

## 3. API Tests - When & Why

### When to Use API Tests
1. **Verifying HTTP contracts** (status codes, headers, JSON structure)
2. **Testing authentication/authorization** flows
3. **Testing request validation** before hitting business logic
4. **Integration between controller and service**

### Why API Tests?

**Unit tests can't catch:**
- Incorrect HTTP method handling
- Missing authentication checks
- Wrong status codes
- JSON serialization issues
- Route not found errors

**Example: Testing Authentication Flow**

```python
# tests/api/test_api_auth.py
def test_login_success(self, api_session, valid_credentials):
    """
    TC-API-001: Verify the full login flow
    
    Why API test?
    - Verify JWT cookie is SET correctly
    - Verify JSON response structure
    - Verify status code is 200
    """
    response = api_session.post(f"{BASE_URL}/api/auth/login", 
                                json=valid_credentials)
    
    assert response.status_code == 200
    assert "jwt_token" in api_session.cookies  # Cookie set!
    assert response.json()["user"]["username"] == "employee1"
```

### API vs Unit Test Decision

| Question | If Yes → | If No → |
|----------|----------|---------|
| Testing HTTP status codes? | API Test | Unit Test |
| Testing request/response format? | API Test | Unit Test |
| Testing pure business logic? | Unit Test | API Test |
| Need database state? | API Test | Mock in Unit |
| Testing error messages in JSON? | API Test | Unit Test |

---

## 4. E2E Tests - When & Why

### When to Use E2E Tests
1. **Critical user journeys** (login → submit → view)
2. **Testing UI-to-backend integration**
3. **Verifying JavaScript behavior**
4. **Final verification before release**

### Why E2E Tests?

**E2E tests verify what unit and API tests cannot:**
- Browser behavior
- JavaScript execution
- CSS/DOM interactions
- Full user workflow

### E2E Test Selection

**Test the CRITICAL paths only:**

```gherkin
# tests/e2e/features/expense_management.feature

# ✅ GOOD - Critical user journey
Scenario: Successful employee login
  Given I am on the login page
  When I enter valid credentials
  Then I should be redirected to the dashboard

# ✅ GOOD - Core functionality
Scenario: Submit a new expense
  Given I am logged in
  When I submit an expense
  Then it should appear in my list

# ❌ BAD - Too granular for E2E
Scenario: Password field masks input
  Given I am on the login page
  When I type in password field
  Then characters should be hidden
```

---

## 5. Integration Test vs E2E Test

### Integration Test (API Level)
- Tests: Controller → Service → Repository → Database
- **No browser involved**
- Uses: requests/REST Assured

```python
# This is an INTEGRATION test
def test_submit_expense_integration(authenticated_session):
    response = authenticated_session.post("/api/expenses", json={...})
    assert response.status_code == 201
    # Expense is actually in the database
```

### E2E Test (UI Level)
- Tests: Browser → Controller → Service → Repository → Database
- **Browser automation**
- Uses: Selenium

```python
# This is an E2E test
def test_submit_expense_e2e(browser):
    browser.get("/login")
    browser.find_element(By.ID, "username").send_keys("user")
    # ...clicks, waits, assertions...
```

---

## 6. Test Decision Flowchart

```
                     ┌────────────────────────┐
                     │ What are you testing?  │
                     └───────────┬────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        ▼                        ▼                        ▼
┌───────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ Pure function │      │ HTTP endpoint   │      │ User workflow   │
│ or business   │      │ or API contract │      │ through browser │
│ logic?        │      │ ?               │      │ ?               │
└───────┬───────┘      └────────┬────────┘      └────────┬────────┘
        │                       │                        │
        ▼                       ▼                        ▼
   ┌─────────┐          ┌─────────────┐           ┌──────────┐
   │  UNIT   │          │  API/INT    │           │   E2E    │
   │  TEST   │          │   TEST      │           │   TEST   │
   └─────────┘          └─────────────┘           └──────────┘
        │                       │                        │
        ▼                       ▼                        ▼
   Mock external          May use real            Use real
   dependencies           database                everything
```

---

## 7. Employee App - Test Mapping

| Component | Test Type | Why | Mock? |
|-----------|-----------|-----|-------|
| `authentication_service.py` | Unit | Business logic, JWT handling | Yes - UserRepository |
| `expense_service.py` | Unit | Validation rules, CRUD logic | Yes - Both repositories |
| `auth_controller.py` | Unit | HTTP handling, request/response | Yes - Services |
| `expense_controller.py` | Unit | CRUD endpoints | Yes - ExpenseService |
| `user_repository.py` | Unit | Database operations | Yes - DatabaseConnection |
| `expense_repository.py` | Unit | CRUD operations | Yes - DatabaseConnection |
| `/api/auth/login` | API | HTTP flow, cookie handling | No - Real server |
| `/api/expenses` | API | Request validation, auth | No - Real server |
| Login → Submit → View | E2E | Critical user journey | No - Real everything |

---

## 8. Controller Layer Testing

### When to Test Controllers
1. **Testing request/response handling** - JSON parsing, status codes
2. **Testing authentication decorators** - JWT validation
3. **Testing error handling** - 400, 401, 404 responses
4. **Testing route logic** - Parameter extraction, query strings

### Controller Test Example

```python
# tests/unit/test_auth_controller.py
@allure.story("Login")
@allure.title("TC-CTRL-AUTH-001: Login with valid credentials")
@pytest.mark.unit
def test_login_valid_credentials(self, client, mock_auth_service, sample_employee):
    """Test successful login returns 200 and sets cookie."""
    # Arrange - Mock service returns user and token
    mock_auth_service.authenticate_user.return_value = sample_employee
    mock_auth_service.generate_token.return_value = 'valid.jwt.token'
    
    # Act
    response = client.post('/api/auth/login', 
        json={'username': 'employee1', 'password': 'password123'})
    
    # Assert
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Login successful'
    assert 'jwt_token' in response.headers.get('Set-Cookie', '')
```

### Testing Authentication Errors

```python
@allure.title("TC-CTRL-AUTH-002: Login with invalid credentials")
def test_login_invalid_credentials(self, client, mock_auth_service):
    """Test invalid credentials returns 401."""
    # Arrange - Mock service returns None (auth failed)
    mock_auth_service.authenticate_user.return_value = None
    
    # Act
    response = client.post('/api/auth/login', 
        json={'username': 'employee1', 'password': 'wrong'})
    
    # Assert
    assert response.status_code == 401
    data = response.get_json()
    assert 'Invalid credentials' in data['error']
```

### Key Concept: Mocking the Authentication Decorator

```python
# Conftest fixture to bypass auth for unit tests
@pytest.fixture
def authenticated_client(flask_app, mock_expense_service, sample_employee):
    """Create test client with mocked authentication."""
    with patch('api.auth.get_current_user', return_value=sample_employee):
        with patch('api.auth.require_employee_auth', lambda f: f):
            with flask_app.test_client() as client:
                yield client
```

---

## 9. Repository Layer Testing

### When to Test Repositories
1. **Testing SQL query execution** - Correct parameters passed
2. **Testing result mapping** - Row to object conversion
3. **Testing error handling** - SQLException handling
4. **Testing transactions** - Commit/rollback behavior

### Repository Test Example

```python
# tests/unit/test_repositories.py
@allure.story("Find User")
@allure.title("TC-REPO-USER-001: Find user by username - found")
@pytest.mark.unit
def test_find_by_username_found(self, user_repository, mock_db_connection):
    """Test finding existing user by username."""
    # Arrange - Mock returns row data
    mock_row = {'id': 1, 'username': 'employee1', 
                'password': 'password123', 'role': 'Employee'}
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
```

### Testing CRUD Operations

```python
@allure.title("TC-REPO-EXP-001: Create expense with approval")
def test_create_expense(self, expense_repository, mock_db_connection):
    """Test creating expense creates both expense and approval records."""
    # Arrange
    mock_cursor = MagicMock()
    mock_cursor.lastrowid = 10
    mock_conn = MagicMock()
    mock_conn.execute.return_value = mock_cursor
    mock_conn.__enter__ = MagicMock(return_value=mock_conn)
    mock_conn.__exit__ = MagicMock(return_value=False)
    mock_db_connection.get_connection.return_value = mock_conn
    
    new_expense = Expense(id=None, user_id=1, amount=100.00, 
                         description='Test expense', date='2024-12-23')
    
    # Act
    result = expense_repository.create(new_expense)
    
    # Assert
    assert result.id == 10
    # Verify both INSERT statements called (expense + approval)
    assert mock_conn.execute.call_count == 2
    mock_conn.commit.assert_called_once()
```

### Testing Not Found Scenarios

```python
@allure.title("TC-REPO-USER-002: Find user by username - not found")
def test_find_by_username_not_found(self, user_repository, mock_db_connection):
    """Test finding non-existent user returns None."""
    # Arrange - Cursor returns nothing
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_conn = MagicMock()
    mock_conn.execute.return_value = mock_cursor
    mock_conn.__enter__ = MagicMock(return_value=mock_conn)
    mock_conn.__exit__ = MagicMock(return_value=False)
    mock_db_connection.get_connection.return_value = mock_conn
    
    # Act
    result = user_repository.find_by_username('unknown')
    
    # Assert
    assert result is None
```

---

## Summary

| Test Type | Use For | Tools | Speed |
|-----------|---------|-------|-------|
| **Unit** | Business logic, validation | pytest, mock | ms |
| **Controller** | HTTP handling, auth | Flask test client | ms |
| **Repository** | Database operations | mock DB connections | ms |
| **API** | HTTP contracts, auth | requests | s |
| **E2E** | User journeys | Behave, Selenium | min |

**Golden Rule:** Write many unit tests, some API tests, few E2E tests.

