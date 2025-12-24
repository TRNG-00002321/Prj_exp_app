# Manager App (Java) - Testing Strategy

## Overview
This guide explains **when, why, and where** to apply each testing technique in the Java Manager application. Each section includes real examples from the codebase.

---

## The Testing Pyramid in Java

```
        /\
       /E2E\         ← Cucumber + Selenium
      /------\
     /  API   \      ← REST Assured
    /----------\
   / Unit Tests \    ← JUnit 5 + Mockito
  /--------------\
```

---

## 1. Unit Tests with JUnit 5 - When & Why

### When to Use Unit Tests
1. **Testing service layer logic** - Business rules, calculations
2. **Testing validation** - Input checking, null handling
3. **Testing conditional logic** - if/else branches
4. **Fast feedback** - Runs in <1 second

### Why Unit Tests for AuthenticationService

**The Code:**
```java
// service/AuthenticationService.java
public Optional<User> authenticateManager(String username, String password) {
    Optional<User> userOpt = authenticateUser(username, password);
    if (userOpt.isPresent() && isManager(userOpt.get())) {
        return userOpt;
    }
    return Optional.empty();  // Not a manager!
}
```

**Why Unit Test?**
- ✅ **Tests business rule**: "Only managers can login to manager app"
- ✅ **Tests edge case**: What if valid user is an employee?
- ✅ **Isolated**: No HTTP, no database
- ✅ **Fast**: Runs in milliseconds

**Test Example:**
```java
// src/test/java/com/revature/service/AuthenticationServiceTest.java
@Test
@DisplayName("TC-MAUTH-002: Employee cannot login to manager app")
void testAuthenticateManager_EmployeeRole_ReturnsEmpty() {
    // Arrange: Return an employee user
    when(userRepository.findByUsername("employee1"))
            .thenReturn(Optional.of(testEmployee));  // Employee, not Manager!

    // Act
    Optional<User> result = authenticationService
            .authenticateManager("employee1", "password123");

    // Assert: Should fail - employees can't login as managers
    assertTrue(result.isEmpty(), "Employees should not be able to login");
}
```

---

## 2. Mockito - When, Why, Where

### The Problem: Dependencies

**Real code has dependencies:**

```java
public class ExpenseService {
    private final ExpenseRepository expenseRepository;    // Dependency!
    private final ApprovalRepository approvalRepository;  // Dependency!
    
    public boolean approveExpense(int expenseId, int managerId, String comment) {
        return approvalRepository.updateApprovalStatus(
            expenseId, "approved", managerId, comment
        );
    }
}
```

**Without mocking:**
- ❌ Need real database
- ❌ Need test data in database
- ❌ Tests are slow
- ❌ Tests can fail due to database issues

### Why Mock?

| Without Mocks | With Mocks |
|---------------|------------|
| Slow (database I/O) | Fast (in-memory) |
| Flaky (database state) | Reliable (controlled) |
| Complex setup | Simple setup |
| Hard to test errors | Easy error simulation |

### Where to Mock - The Boundary Rule

**Mock at the layer below what you're testing:**

```
┌─────────────────────────────────────────────────┐
│   ExpenseController                             │
│   └─ Mock: ExpenseService                       │
├─────────────────────────────────────────────────┤
│   ExpenseService                   ← TEST THIS  │
│   └─ Mock: ExpenseRepository, ApprovalRepository│
├─────────────────────────────────────────────────┤
│   Repositories                                  │
│   └─ Mock: DatabaseConnection                   │
└─────────────────────────────────────────────────┘
```

### Mockito Annotations Explained

```java
@ExtendWith(MockitoExtension.class)  // Enable Mockito for JUnit 5
class ExpenseServiceTest {

    @Mock  // Creates fake repository
    private ExpenseRepository expenseRepository;

    @Mock
    private ApprovalRepository approvalRepository;

    @InjectMocks  // Creates real service, injects mocks automatically
    private ExpenseService expenseService;
}
```

**How @InjectMocks works:**
1. Mockito creates mock objects for all @Mock fields
2. Creates real ExpenseService instance
3. Finds constructor that matches mock types
4. Injects mocks into the constructor

### Stubbing with when().thenReturn()

```java
// Tell the mock what to return
when(expenseRepository.findPendingExpensesWithUsers())
        .thenReturn(mockExpenses);

// Now when the service calls the mock, it returns mockExpenses
List<ExpenseWithUser> result = expenseService.getPendingExpenses();
```

### Verifying with verify()

```java
// Call the method
expenseService.approveExpense(1, 2, "Approved");

// Verify the mock was called correctly
verify(approvalRepository).updateApprovalStatus(
    eq(1),           // expense ID
    eq("approved"),  // status
    eq(2),           // manager ID
    eq("Approved")   // comment
);
```

### Simulating Errors with thenThrow()

```java
// Simulate database error
when(expenseRepository.findById(anyInt()))
        .thenThrow(new RuntimeException("Database connection lost"));

// Test that service handles error gracefully
assertThrows(ServiceException.class, () -> 
        expenseService.getExpense(1));
```

---

## 3. API Tests with REST Assured - When & Why

### When to Use API Tests
1. **Testing HTTP contracts** - Status codes, headers, body format
2. **Testing authentication** - JWT validation, role checking
3. **Testing serialization** - JSON responses
4. **Integration verification** - Controller + Service + Repository

### Why API Tests?

**Unit tests can't catch:**
- Wrong HTTP method handling (POST vs GET)
- Missing @PreAuthorize or role checks
- JSON serialization bugs
- Response header issues
- Cookie handling

### REST Assured Fluent API

```java
// src/test/java/com/revature/api/ExpenseApiTest.java
@Test
@DisplayName("TC-MAPI-003: Get pending expenses when authenticated")
void testGetPendingExpenses_Authenticated_Returns200() {
    
    // Login first to get JWT cookie
    String jwt = given()
            .contentType(ContentType.JSON)
            .body("{\"username\": \"manager1\", \"password\": \"password123\"}")
            .post("/api/auth/login")
            .getCookie("jwt");

    // Use cookie to access protected endpoint
    given()
            .cookie("jwt", jwt)          // Authentication!
    .when()
            .get("/api/expenses/pending")
    .then()
            .statusCode(200)             // HTTP status
            .body("success", equalTo(true))   // JSON field
            .body("data", notNullValue())     // JSON field exists
            .body("count", greaterThanOrEqualTo(0)); // Numeric check
}
```

### API Test vs Unit Test Decision

| Scenario | Use API Test | Use Unit Test |
|----------|--------------|---------------|
| Test business logic in service | ❌ | ✅ |
| Test HTTP 401 when not authenticated | ✅ | ❌ |
| Test JSON response structure | ✅ | ❌ |
| Test validation error messages | ✅ | ✅ (both) |
| Test cookie is set on login | ✅ | ❌ |
| Test internal method behavior | ❌ | ✅ |

---

## 4. E2E Tests with Cucumber - When & Why

### When to Use E2E Tests
1. **Critical user journeys** - Login → Approve → Report
2. **Browser-specific behavior** - JavaScript, cookies, redirects
3. **Final verification** - Before release
4. **Acceptance criteria** - User stories become tests

### Why Cucumber?

**Cucumber connects user stories to tests:**

```gherkin
# User Story (JIRA):
# As a manager, I want to approve expenses so employees get reimbursed

# Cucumber Feature (executable specification):
Feature: Manager Expense Approval
  
  Scenario: Approve an expense
    Given I am logged in as manager "manager1"
    And there is a pending expense to review
    When I click the approve button
    Then the expense status should change to "approved"
```

### Step Definitions

```java
// src/test/java/com/revature/e2e/steps/ExpenseSteps.java

@Given("I am logged in as manager {string} with password {string}")
public void iAmLoggedInAsManager(String username, String password) {
    driver.get(BASE_URL + "/login.html");
    driver.findElement(By.id("username")).sendKeys(username);
    driver.findElement(By.id("password")).sendKeys(password);
    driver.findElement(By.id("loginBtn")).click();
    
    // Wait for redirect to dashboard
    wait.until(ExpectedConditions.urlContains("manager"));
}

@When("I click the approve button for the expense")
public void iClickTheApproveButton() {
    WebElement approveBtn = wait.until(
        ExpectedConditions.elementToBeClickable(By.cssSelector(".approve-btn"))
    );
    approveBtn.click();
}

@Then("the expense status should change to {string}")
public void theExpenseStatusShouldChangeTo(String status) {
    wait.until(driver -> driver.getPageSource().contains(status));
}
```

### What to Test with E2E vs API

| Test This With E2E | Test This With API |
|--------------------|--------------------|
| Login form works in browser | Login endpoint returns JWT |
| Approve button is clickable | Approve endpoint changes status |
| Success message appears | Response has success: true |
| Redirect after login | Return value contains redirect URL |
| JavaScript validation | Server-side validation |

---

## 5. Integration Tests - The Middle Ground

### What is an Integration Test?

**Integration tests:**
- Test multiple components together
- May use real database
- Don't involve browser

**In this project, REST Assured tests are integration tests:**

```java
// This IS an integration test (not unit):
// - Real Javalin server running
// - Real database (or in-memory)
// - Tests Controller → Service → Repository flow

@Test
void testApproveExpense_Integration() {
    given()
        .cookie("jwt", loginAndGetJwt())
        .body("{\"comment\": \"Looks good\"}")
    .when()
        .post("/api/expenses/1/approve")  // Real HTTP call!
    .then()
        .statusCode(200);
        
    // Verify in database (if needed)
    // Expense status should actually be "approved"
}
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
│ Business logic│      │ HTTP endpoint   │      │ User clicks     │
│ calculation   │      │ JSON response   │      │ through browser │
│ validation    │      │ status code     │      │ JavaScript      │
└───────┬───────┘      └────────┬────────┘      └────────┬────────┘
        │                       │                        │
        ▼                       ▼                        ▼
   ┌─────────┐          ┌─────────────┐           ┌──────────┐
   │ JUnit 5 │          │REST Assured │           │ Cucumber │
   │+Mockito │          │             │           │+Selenium │
   └─────────┘          └─────────────┘           └──────────┘
```

---

## 7. Manager App - Test Mapping

| Component | Test Type | Why This Type? | Mock What? |
|-----------|-----------|----------------|------------|
| `AuthenticationService.authenticateManager()` | Unit | Tests role-checking logic | UserRepository |
| `AuthenticationService.isManager()` | Unit | Simple boolean logic | Nothing |
| `ExpenseService.approveExpense()` | Unit | Tests approval workflow | ApprovalRepository |
| `ExpenseService.generateCsvReport()` | Unit | Tests CSV formatting | Nothing (pure function) |
| `ExpenseController.getPendingExpenses()` | Unit | Tests HTTP response building | ExpenseService |
| `ReportController.getExpensesCsv()` | Unit | Tests CSV download | ExpenseService |
| `UserRepository.findByUsername()` | Unit | Tests SQL execution | DatabaseConnection |
| `ExpenseRepository.findPendingExpensesWithUsers()` | Unit | Tests JOINs | DatabaseConnection |
| `POST /api/auth/login` | API | Tests HTTP + cookie | Nothing (real server) |
| `GET /api/expenses/pending` | API | Tests auth + JSON | Nothing (real server) |
| Manager login → approve → logout | E2E | Critical workflow | Nothing (real everything) |

---

## 8. Controller Layer Testing

### When to Test Controllers
1. **Testing HTTP response building** - JSON structure, status codes
2. **Testing input validation** - Path parameters, request body
3. **Testing error responses** - 400, 404, 500 handling
4. **Testing authentication middleware** - JWT validation

### Controller Test Example

```java
// src/test/java/com/revature/api/ExpenseControllerTest.java
@Test
@Story("Get Pending")
@DisplayName("TC-CTRL-001: Get pending expenses returns JSON response")
@Severity(SeverityLevel.CRITICAL)
void testGetPendingExpenses_Success() {
    // Arrange
    List<ExpenseWithUser> mockExpenses = List.of(createMockExpenseWithUser());
    when(mockExpenseService.getPendingExpenses()).thenReturn(mockExpenses);
    
    // Act
    expenseController.getPendingExpenses(ctx);
    
    // Assert
    verify(ctx).json(responseCaptor.capture());
    Map<String, Object> response = responseCaptor.getValue();
    assertTrue((Boolean) response.get("success"));
    assertEquals(1, response.get("count"));
}
```

### Testing Mocked Javalin Context

```java
@Mock
private Context ctx;

@Mock
private Validator<Integer> intValidator;

@BeforeEach
void setUp() {
    // Mock path parameter validation
    when(ctx.pathParamAsClass("expenseId", Integer.class)).thenReturn(intValidator);
    when(intValidator.get()).thenReturn(1);
}

@Test
@DisplayName("TC-CTRL-005: Approve non-existent expense returns 404")
void testApproveExpense_NotFound() {
    // Arrange
    when(mockExpenseService.approveExpense(eq(1), anyInt(), any()))
        .thenReturn(false);
    
    // Act
    expenseController.approveExpense(ctx);
    
    // Assert
    verify(ctx).status(404);
}
```

### Testing Report Controller (CSV Downloads)

```java
// src/test/java/com/revature/api/ReportControllerTest.java
@Test
@DisplayName("TC-RPT-001: Generate all expenses CSV")
void testGetAllExpensesCsv_Success() {
    // Arrange
    String mockCsv = "ID,Amount,Description\n1,100.00,Test\n";
    when(mockExpenseService.generateAllExpensesCsv()).thenReturn(mockCsv);
    
    // Act
    reportController.getAllExpensesCsv(ctx);
    
    // Assert
    verify(ctx).contentType("text/csv");
    verify(ctx).header(eq("Content-Disposition"), contains("expenses_all"));
    verify(ctx).result(mockCsv);
}
```

---

## 9. Repository Layer Testing

### When to Test Repositories
1. **Testing SQL query execution** - Parameter binding
2. **Testing result set mapping** - Column to object
3. **Testing exception handling** - SQLException wrapping
4. **Testing multiple row results** - List operations

### Repository Test Example

```java
// src/test/java/com/revature/repository/UserRepositoryTest.java
@Test
@Story("Find User")
@DisplayName("TC-REPO-MUSER-001: Find user by ID - found")
@Severity(SeverityLevel.CRITICAL)
void testFindById_Found() throws SQLException {
    // Arrange
    when(mockDatabaseConnection.getConnection()).thenReturn(mockConnection);
    when(mockConnection.prepareStatement(anyString())).thenReturn(mockStatement);
    when(mockStatement.executeQuery()).thenReturn(mockResultSet);
    when(mockResultSet.next()).thenReturn(true);
    when(mockResultSet.getInt("id")).thenReturn(1);
    when(mockResultSet.getString("username")).thenReturn("manager1");
    when(mockResultSet.getString("password")).thenReturn("password123");
    when(mockResultSet.getString("role")).thenReturn("Manager");

    // Act
    Optional<User> result = userRepository.findById(1);

    // Assert
    assertTrue(result.isPresent());
    assertEquals(1, result.get().getId());
    assertEquals("manager1", result.get().getUsername());
    verify(mockStatement).setInt(1, 1);
}
```

### Testing Complex Queries with JOINs

```java
// src/test/java/com/revature/repository/ExpenseRepositoryTest.java
@Test
@DisplayName("TC-REPO-MEXP-003: Find pending expenses - returns list")
void testFindPendingExpensesWithUsers_ReturnsList() throws SQLException {
    // Arrange
    when(mockDatabaseConnection.getConnection()).thenReturn(mockConnection);
    when(mockConnection.prepareStatement(anyString())).thenReturn(mockStatement);
    when(mockStatement.executeQuery()).thenReturn(mockResultSet);
    when(mockResultSet.next())
        .thenReturn(true)   // First row
        .thenReturn(true)   // Second row
        .thenReturn(false); // End
    
    // Mock result set columns for ExpenseWithUser mapping
    when(mockResultSet.getInt("id")).thenReturn(1, 2);
    when(mockResultSet.getDouble("amount")).thenReturn(100.00, 200.00);
    when(mockResultSet.getString("status")).thenReturn("pending");

    // Act
    List<ExpenseWithUser> result = expenseRepository.findPendingExpensesWithUsers();

    // Assert
    assertEquals(2, result.size());
}
```

### Testing UPDATE Operations

```java
// src/test/java/com/revature/repository/ApprovalRepositoryTest.java
@Test
@DisplayName("TC-REPO-MAPR-004: Update approval status - success")
void testUpdateApprovalStatus_Success() throws SQLException {
    // Arrange
    when(mockDatabaseConnection.getConnection()).thenReturn(mockConnection);
    when(mockConnection.prepareStatement(anyString())).thenReturn(mockStatement);
    when(mockStatement.executeUpdate()).thenReturn(1);

    // Act
    boolean result = approvalRepository.updateApprovalStatus(
        1, "approved", 2, "Looks good");

    // Assert
    assertTrue(result);
    verify(mockStatement).setString(1, "approved");
    verify(mockStatement).setInt(2, 2);
    verify(mockStatement).setString(3, "Looks good");
}
```

### Testing SQLException Handling

```java
@Test
@DisplayName("TC-REPO-MUSER-003: Find user by ID - SQL exception")
void testFindById_SQLException() throws SQLException {
    // Arrange
    when(mockDatabaseConnection.getConnection())
        .thenThrow(new SQLException("Connection failed"));

    // Act & Assert
    assertThrows(RuntimeException.class, () -> userRepository.findById(1));
}
```

---

## 10. Common Mistakes to Avoid

### ❌ Mistake 1: Mocking what you're testing
```java
// WRONG: Testing ExpenseService but mocking its method
when(expenseService.approveExpense(1, 2)).thenReturn(true);
assertTrue(expenseService.approveExpense(1, 2)); // Always passes!
```

### ❌ Mistake 2: Over-mocking (testing nothing)
```java
// WRONG: Everything is mocked, no real code runs
@Mock ExpenseService service;
@Test
void test() {
    when(service.getExpenses()).thenReturn(List.of());
    assertTrue(service.getExpenses().isEmpty()); // What are we testing?
}
```

### ❌ Mistake 3: Testing private methods
```java
// WRONG: Don't test private methods directly
// Test them through public methods
```

### ✅ Correct: Mock dependencies, test real logic
```java
// RIGHT: Mock repository, test service logic
@Mock ApprovalRepository approvalRepo;
@InjectMocks ExpenseService service;  // Real service!

@Test
void testApprove() {
    when(approvalRepo.updateApprovalStatus(...)).thenReturn(true);
    boolean result = service.approveExpense(1, 2, "OK");  // Real method!
    assertTrue(result);
}
```

---

## Summary Table

| Test Type | Framework | Use For | Speed | Mock? |
|-----------|-----------|---------|-------|-------|
| **Unit (Service)** | JUnit 5 + Mockito | Business logic | ms | Yes - Repositories |
| **Unit (Controller)** | JUnit 5 + Mockito | HTTP handling | ms | Yes - Services |
| **Unit (Repository)** | JUnit 5 + Mockito | SQL operations | ms | Yes - JDBC |
| **API/Integration** | REST Assured | HTTP contracts, auth | s | No |
| **E2E** | Cucumber + Selenium | User journeys | min | No |

---


