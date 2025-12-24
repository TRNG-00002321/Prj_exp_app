# Notes - Revature Expense Manager P1 Testing


---

## Unit Testing

### Python Unit Tests (pytest + pytest-mock)

#### Key  Points

1. **Test Structure (AAA Pattern)**
```python
def test_authenticate_valid_user(self):
    # Arrange: Set up test data and mocks
    mock_repo.find_by_username.return_value = test_user
    
    # Act: Call the method being tested
    result = auth_service.authenticate_user("user1", "pass123")
    
    # Assert: Verify the expected outcome
    assert result is not None
```

2. **Mocking with pytest-mock**
- `@pytest.fixture` creates reusable test data
- `MagicMock()` creates mock objects that track calls
- `mock.return_value` sets what the mock returns
- `mock.assert_called_once_with()` verifies correct usage

3. **Coverage Objectives**
- Run: `pytest --cov=. --cov-report=html`
- Target: 70% minimum coverage
- Review uncovered lines in `htmlcov/index.html`

### Java Unit Tests (JUnit 5 + Mockito)

#### Key  Points

1. **JUnit 5 Annotations**
```java
@Test              // Marks a test method
@BeforeEach        // Runs before each test
@DisplayName       // Human-readable test name
@ExtendWith        // Enables Mockito extension
```

2. **Mockito Annotations**
```java
@Mock              // Creates mock object
@InjectMocks       // Injects mocks into SUT
when(...).thenReturn(...)  // Stubbing behavior
verify(mock).method()      // Verify interaction
```

3. **Running Tests**
```bash
mvn test                    # Run all tests
mvn test -Dtest=AuthenticationServiceTest  # Single class
```

---

## API & Performance Testing

### Python API Tests (requests)

#### Key  Points

1. **Session Management**
```python
session = requests.Session()  # Maintains cookies
response = session.post(url, json=data)
assert response.status_code == 200
```

2. **Testing Happy/Sad Paths**
- 200: Success
- 400: Validation error
- 401: Unauthorized
- 404: Not found

### Java API Tests (REST Assured)

#### Key  Points

1. **REST Assured Fluent API**
```java
given()
    .contentType(ContentType.JSON)
    .body(requestBody)
.when()
    .post("/api/auth/login")
.then()
    .statusCode(200)
    .body("success", equalTo(true));
```

2. **Extracting Responses**
```java
String token = given()...extract().response().getCookie("jwt");
```

### JMeter Performance Testing

#### Key  Points

1. **CLI Execution (for CI/CD)**
```bash
jmeter -n -t employee_load_test.jmx -l results.jtl -e -o report
```

2. **Key Metrics to Monitor**
- Response Time (avg < 500ms)
- Error Rate (< 5%)
- Throughput (requests/sec)

3. **Test Plan Components**
- Thread Group: Simulates users
- HTTP Request: API calls
- Assertions: Pass/fail criteria
- Listeners: Results collection

### Postman Collections

#### Key  Points
- Pre-request scripts for setup
- Post-test scripts for validation
- Collection variables for environment
- Import via Postman > Import

---

## E2E Testing

### Python E2E (Behave + Selenium)

#### Key  Points

1. **Gherkin Syntax**
```gherkin
Feature: Employee Login
  Scenario: Successful login
    Given I am on the login page
    When I enter valid credentials
    Then I should see the dashboard
```

2. **Step Definitions**
```python
@given('I am on the login page')
def step_impl(context):
    context.driver.get("http://localhost:5000/login")
```

3. **Selenium Locators**
- `By.ID` - Preferred, most reliable
- `By.CSS_SELECTOR` - Flexible
- `By.XPATH` - Complex queries

4. **Running E2E Tests**
```bash
behave tests/e2e/features/
```

### Java E2E (Cucumber + Selenium)


#### Key  Points

1. **Cucumber Runner**
```java
@Suite
@IncludeEngines("cucumber")
@SelectClasspathResource("features")
public class TestRunner {}
```

2. **Step Definitions**
```java
@Given("I am on the login page")
public void iAmOnLoginPage() {
    driver.get(BASE_URL + "/login.html");
}
```

3. **WebDriverManager**
```java
WebDriverManager.chromedriver().setup();  // Auto-installs driver
```

---

## Allure Reporting

### Setup

**Python:**
```bash
pip install allure-pytest allure-behave
pytest --alluredir=allure-results
allure serve allure-results
```

**Java:**
```bash
mvn test
mvn allure:serve
```

### Annotations
- `@allure.epic()` - Top-level grouping
- `@allure.feature()` - Feature grouping
- `@allure.story()` - User story
- `@allure.severity()` - Test importance

---

## Running All Tests

### Employee App (Python)
```bash
cd employee

# Unit tests with coverage
pytest tests/unit --cov=. --cov-report=html

# API tests (requires server running)
python main.py &  # Start server
pytest tests/api -v

# E2E tests
behave tests/e2e/features/

# Generate Allure report
pytest --alluredir=allure-results
allure serve allure-results
```

### Manager App (Java)
```bash
cd manager

# Run all tests with coverage
mvn clean test

# View JaCoCo coverage report
open target/site/jacoco/index.html

# Generate Allure report
mvn allure:serve
```

---

## Common Student Issues

| Issue | Solution |
|-------|----------|
| Tests fail with ModuleNotFoundError | Add `__init__.py` to test folders |
| Mocks not working | Verify mock is patching the right module |
| Selenium can't find element | Add explicit waits |
| REST Assured 401 errors | Ensure cookie is being passed |
| JMeter connection refused | Verify server is running |

---

## Assessment Checklist

- [ ] Unit tests demonstrate mocking
- [ ] API tests cover authentication
- [ ] E2E tests cover critical flows
- [ ] Performance tests run without errors
- [ ] Coverage reports generate correctly
- [ ] Allure reports display properly
