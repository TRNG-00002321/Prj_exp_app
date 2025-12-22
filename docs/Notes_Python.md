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
| `/api/auth/login` | API | HTTP flow, cookie handling | No - Real server |
| `/api/expenses` | API | Request validation, auth | No - Real server |
| Login → Submit → View | E2E | Critical user journey | No - Real everything |

---

## Summary

| Test Type | Use For | Tools | Speed |
|-----------|---------|-------|-------|
| **Unit** | Business logic, validation | pytest, mock | ms |
| **API** | HTTP contracts, auth | requests | s |
| **E2E** | User journeys | Behave, Selenium | min |

**Golden Rule:** Write many unit tests, some API tests, few E2E tests.
