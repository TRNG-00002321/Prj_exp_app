# Test Case Document - Revature Expense Manager P1

## Document Information
| Item | Details |
|------|---------|
| Project | Revature Expense Manager |
| Test Phase | Phase 2 Testing |
| Date | December 23, 2024 |

---

## Test Case Summary

### By Test Type
| Test Type | Count | Percentage |
|-----------|-------|------------|
| Unit Tests | 159 | 68% |
| API Tests | 26 | 11% |
| E2E Tests | 18 | 8% |
| Performance Tests | 5 | 2% |
| Repository Tests | 42 | 18% |
| Controller Tests | 63 | 27% |
| **Total** | **233** | **100%** |

### By Application
| Application | Unit | API | E2E | Total |
|-------------|------|-----|-----|-------|
| Employee (Python) | 76 | 18 | 8 | 102 |
| Manager (Java) | 83 | 8 | 10 | 101 |
| **Total** | **159** | **26** | **18** | **203** |

### By Test Layer (Unit Tests Only)
| Layer | Python | Java | Total |
|-------|--------|------|-------|
| Service | 26 | 27 | 53 |
| Controller | 32 | 31 | 63 |
| Repository | 17 | 25 | 42 |
| Middleware | 1 | 7 | 8 |
| **Total** | **76** | **83** | **159** |

### By Scenario Type
| Scenario Type | Count | Description |
|---------------|-------|-------------|
| Happy Path | 98 | Valid inputs, expected success |
| Sad Path | 85 | Invalid inputs, error handling |
| Edge Cases | 20 | Boundary conditions, empty data |
| Security | 30 | Authentication, authorization |
| **Total** | **233** | |

---

## 1. Unit Test Cases

### 1.1 Employee App (Python) - Authentication Service

| TC ID | Description | Input | Expected Result | Type |
|-------|-------------|-------|-----------------|------|
| TC-AUTH-001 | Authenticate valid employee | username="employee1", password="password123" | Returns User object | Happy |
| TC-AUTH-002 | Authenticate invalid password | username="employee1", password="wrong" | Returns None | Sad |
| TC-AUTH-003 | Authenticate non-existent user | username="unknown", password="any" | Returns None | Sad |
| TC-AUTH-004 | Generate JWT token | Valid User object | Returns token string | Happy |
| TC-AUTH-005 | Validate valid JWT token | Valid token | Returns decoded payload | Happy |
| TC-AUTH-006 | Validate expired JWT token | Expired token | Returns None | Sad |
| TC-AUTH-007 | Validate malformed JWT token | "invalid.token" | Returns None | Sad |
| TC-AUTH-008 | Get user from valid token | Valid token | Returns User object | Happy |

### 1.2 Employee App (Python) - Expense Service

| TC ID | Description | Input | Expected Result | Type |
|-------|-------------|-------|-----------------|------|
| TC-EXP-001 | Submit expense with valid data | amount=100.00, desc="Lunch" | Creates expense with pending status | Happy |
| TC-EXP-002 | Submit expense with zero amount | amount=0, desc="Test" | Raises ValueError | Sad |
| TC-EXP-003 | Submit expense with negative amount | amount=-50, desc="Test" | Raises ValueError | Sad |
| TC-EXP-004 | Submit expense with empty description | amount=100, desc="" | Raises ValueError | Sad |
| TC-EXP-005 | Get user expenses | user_id=1 | Returns list of (Expense, Approval) tuples | Happy |
| TC-EXP-006 | Get expense by ID (owner) | expense_id=1, user_id=1 (owner) | Returns expense | Happy |
| TC-EXP-007 | Get expense by ID (non-owner) | expense_id=1, user_id=2 (not owner) | Returns None | Sad |
| TC-EXP-008 | Update pending expense | expense_id=1, status=pending | Updates successfully | Happy |
| TC-EXP-009 | Update approved expense | expense_id=1, status=approved | Raises ValueError | Sad |
| TC-EXP-010 | Delete pending expense | expense_id=1, status=pending | Deletes successfully | Happy |
| TC-EXP-011 | Delete approved expense | expense_id=1, status=approved | Raises ValueError | Sad |
| TC-EXP-012 | Filter expenses by status | status="pending" | Returns filtered list | Happy |

### 1.3 Manager App (Java) - Authentication Service

| TC ID | Description | Input | Expected Result | Type |
|-------|-------------|-------|-----------------|------|
| TC-MAUTH-001 | Authenticate valid manager | username="manager1", password="password123" | Returns Optional with User | Happy |
| TC-MAUTH-002 | Authenticate employee (wrong role) | username="employee1", password="password123" | Returns Optional.empty() | Sad |
| TC-MAUTH-003 | Create JWT token | Valid User | Returns token string | Happy |
| TC-MAUTH-004 | Validate JWT token | Valid token | Returns Optional with User | Happy |
| TC-MAUTH-005 | Check isManager for manager | User with role="Manager" | Returns true | Happy |
| TC-MAUTH-006 | Check isManager for employee | User with role="Employee" | Returns false | Sad |

### 1.4 Manager App (Java) - Expense Service

| TC ID | Description | Input | Expected Result | Type |
|-------|-------------|-------|-----------------|------|
| TC-MEXP-001 | Get pending expenses | - | Returns List of ExpenseWithUser | Happy |
| TC-MEXP-002 | Approve expense | expenseId=1, managerId=2 | Returns true, status=approved | Happy |
| TC-MEXP-003 | Deny expense | expenseId=1, managerId=2 | Returns true, status=denied | Happy |
| TC-MEXP-004 | Approve with comment | expenseId=1, comment="Good" | Stores comment | Happy |
| TC-MEXP-005 | Get expenses by employee | employeeId=1 | Returns employee's expenses | Happy |
| TC-MEXP-006 | Generate CSV report | List of expenses | Returns valid CSV string | Happy |
| TC-MEXP-007 | CSV escape special characters | Description with comma | Properly escaped | Happy |
| TC-MEXP-008 | Get expenses by date range | startDate, endDate | Returns filtered list | Happy |

### 1.5 Employee App (Python) - Repository Tests

| TC ID | Description | Input | Expected Result | Type |
|-------|-------------|-------|-----------------|------|
| TC-REPO-USER-001 | Find user by username - found | username="employee1" | Returns User object | Happy |
| TC-REPO-USER-002 | Find user by username - not found | username="unknown" | Returns None | Sad |
| TC-REPO-USER-003 | Find user by ID - found | user_id=1 | Returns User object | Happy |
| TC-REPO-USER-004 | Find user by ID - not found | user_id=999 | Returns None | Sad |
| TC-REPO-USER-005 | Create new user | User object | Returns User with ID | Happy |
| TC-REPO-EXP-001 | Create expense with approval | Expense object | Creates both records | Happy |
| TC-REPO-EXP-002 | Find expense by ID - found | expense_id=1 | Returns Expense | Happy |
| TC-REPO-EXP-003 | Find expense by ID - not found | expense_id=999 | Returns None | Sad |
| TC-REPO-EXP-004 | Find expenses by user ID | user_id=1 | Returns list of Expenses | Happy |
| TC-REPO-EXP-005 | Find expenses by user - empty | user_id=999 | Returns empty list | Sad |
| TC-REPO-EXP-006 | Update expense | Expense object | Returns updated Expense | Happy |
| TC-REPO-EXP-007 | Delete expense - success | expense_id=1 | Returns True | Happy |
| TC-REPO-EXP-008 | Delete expense - not found | expense_id=999 | Returns False | Sad |
| TC-REPO-APR-001 | Find approval by expense ID - found | expense_id=1 | Returns Approval | Happy |
| TC-REPO-APR-002 | Find approval by expense ID - not found | expense_id=999 | Returns None | Sad |
| TC-REPO-APR-003 | Update approval status - success | expense_id=1, status="approved" | Returns True | Happy |
| TC-REPO-APR-004 | Update approval status - not found | expense_id=999 | Returns False | Sad |

### 1.6 Manager App (Java) - Repository Tests

| TC ID | Description | Input | Expected Result | Type |
|-------|-------------|-------|-----------------|------|
| TC-REPO-MUSER-001 | Find user by ID - found | userId=1 | Returns Optional with User | Happy |
| TC-REPO-MUSER-002 | Find user by ID - not found | userId=999 | Returns Optional.empty() | Sad |
| TC-REPO-MUSER-003 | Find user by ID - SQL exception | DB error | Throws RuntimeException | Sad |
| TC-REPO-MUSER-004 | Find user by username - found | username="manager1" | Returns Optional with User | Happy |
| TC-REPO-MUSER-005 | Find user by username - not found | username="unknown" | Returns Optional.empty() | Sad |
| TC-REPO-MUSER-006 | Find user by username - SQL exception | DB error | Throws RuntimeException | Sad |
| TC-REPO-MEXP-001 | Find expense by ID - found | expenseId=1 | Returns Optional with Expense | Happy |
| TC-REPO-MEXP-002 | Find expense by ID - not found | expenseId=999 | Returns Optional.empty() | Sad |
| TC-REPO-MEXP-003 | Find pending expenses - returns list | - | Returns List ExpenseWithUser | Happy |
| TC-REPO-MEXP-004 | Find pending expenses - empty | No pending | Returns empty list | Sad |
| TC-REPO-MEXP-005 | Find pending expenses - SQL exception | DB error | Throws RuntimeException | Sad |
| TC-REPO-MEXP-006 | Find expenses by user | userId=5 | Returns list | Happy |
| TC-REPO-MEXP-007 | Find expenses by date range | start, end | Returns filtered list | Happy |
| TC-REPO-MEXP-008 | Find expenses by category | category="Travel" | Uses LIKE query | Happy |
| TC-REPO-MEXP-009 | Find all expenses | - | Returns all expenses | Happy |
| TC-REPO-MAPR-001 | Find approval by expense ID - found | expenseId=1 | Returns Optional with Approval | Happy |
| TC-REPO-MAPR-002 | Find approval by expense ID - not found | expenseId=999 | Returns Optional.empty() | Sad |
| TC-REPO-MAPR-003 | Find approval - SQL exception | DB error | Throws RuntimeException | Sad |
| TC-REPO-MAPR-004 | Update approval status - success | expenseId=1, approved | Returns true | Happy |
| TC-REPO-MAPR-005 | Update approval status - not found | expenseId=999 | Returns false | Sad |
| TC-REPO-MAPR-006 | Update approval - deny with comment | denied, comment | Stores comment | Happy |
| TC-REPO-MAPR-007 | Update approval - SQL exception | DB error | Throws RuntimeException | Sad |
| TC-REPO-MAPR-008 | Create approval - success | expenseId=5 | Returns Approval with ID | Happy |
| TC-REPO-MAPR-009 | Create approval - no rows | Insert fails | Throws RuntimeException | Sad |
| TC-REPO-MAPR-010 | Create approval - no generated key | No key | Throws RuntimeException | Sad |

### 1.7 Employee App (Python) - Auth Controller Tests

| TC ID | Description | Input | Expected Result | Type |
|-------|-------------|-------|-----------------|------|
| TC-CTRL-AUTH-001 | Login with valid credentials | Valid JSON body | 200 + JWT cookie | Happy |
| TC-CTRL-AUTH-002 | Login with invalid credentials | Wrong password | 401 Unauthorized | Sad |
| TC-CTRL-AUTH-003 | Login with missing username | No username field | 400 Bad Request | Sad |
| TC-CTRL-AUTH-004 | Login with missing password | No password field | 400 Bad Request | Sad |
| TC-CTRL-AUTH-005 | Login with empty JSON body | {} | 400 Bad Request | Sad |
| TC-CTRL-AUTH-006 | Logout clears JWT cookie | POST /logout | 200 + expired cookie | Happy |
| TC-CTRL-AUTH-007 | Status check with valid token | Valid JWT cookie | {authenticated: true} | Happy |
| TC-CTRL-AUTH-008 | Status check without token | No cookie | {authenticated: false} | Sad |
| TC-CTRL-AUTH-009 | Status check with invalid token | Invalid JWT | {authenticated: false} | Sad |

### 1.6 Employee App (Python) - Expense Controller Tests

| TC ID | Description | Input | Expected Result | Type |
|-------|-------------|-------|-----------------|------|
| TC-CTRL-EXP-001 | Submit expense with valid data | Valid JSON + auth | 201 Created | Happy |
| TC-CTRL-EXP-002 | Submit expense without amount | Missing amount | 400 Bad Request | Sad |
| TC-CTRL-EXP-003 | Submit expense without description | Missing description | 400 Bad Request | Sad |
| TC-CTRL-EXP-004 | Submit expense with invalid amount | amount="text" | 400 Bad Request | Sad |
| TC-CTRL-EXP-005 | Submit expense unauthenticated | No JWT | 401 Unauthorized | Sad |
| TC-CTRL-EXP-006 | Get all expenses for user | GET /expenses + auth | 200 + expense list | Happy |
| TC-CTRL-EXP-007 | Get expenses with status filter | ?status=approved | 200 + filtered list | Happy |
| TC-CTRL-EXP-008 | Get single expense by ID | GET /expenses/1 | 200 + expense data | Happy |
| TC-CTRL-EXP-009 | Get non-existent expense | GET /expenses/999 | 404 Not Found | Sad |
| TC-CTRL-EXP-010 | Update pending expense | PUT /expenses/1 | 200 + updated data | Happy |
| TC-CTRL-EXP-011 | Update non-existent expense | PUT /expenses/999 | 404 Not Found | Sad |
| TC-CTRL-EXP-012 | Update with missing fields | Missing required fields | 400 Bad Request | Sad |
| TC-CTRL-EXP-013 | Delete pending expense | DELETE /expenses/1 | 200 Success | Happy |
| TC-CTRL-EXP-014 | Delete non-existent expense | DELETE /expenses/999 | 404 Not Found | Sad |

### 1.7 Manager App (Java) - Expense Controller Tests

| TC ID | Description | Input | Expected Result | Type |
|-------|-------------|-------|-----------------|------|
| TC-CTRL-001 | Get pending expenses | GET /pending + auth | 200 + {success, data, count} | Happy |
| TC-CTRL-002 | Get pending expenses empty | No pending expenses | 200 + {count: 0} | Happy |
| TC-CTRL-003 | Get pending expenses error | Service exception | 500 Internal Error | Sad |
| TC-CTRL-004 | Approve expense success | POST /1/approve | 200 + success message | Happy |
| TC-CTRL-005 | Approve non-existent expense | POST /999/approve | 404 Not Found | Sad |
| TC-CTRL-006 | Deny expense success | POST /1/deny | 200 + success message | Happy |
| TC-CTRL-007 | Deny non-existent expense | POST /999/deny | 404 Not Found | Sad |
| TC-CTRL-008 | Get all expenses | GET /expenses | 200 + {success, data, count} | Happy |
| TC-CTRL-009 | Get expenses by employee | GET /employee/1 | 200 + employee expenses | Happy |
| TC-CTRL-010 | Get expenses by employee empty | No expenses | 200 + {count: 0} | Happy |

### 1.8 Manager App (Java) - Report Controller Tests

| TC ID | Description | Input | Expected Result | Type |
|-------|-------------|-------|-----------------|------|
| TC-RPT-001 | Generate all expenses CSV | GET /reports/csv | 200 + CSV content | Happy |
| TC-RPT-002 | Generate CSV empty list | No expenses | 200 + header only | Happy |
| TC-RPT-003 | Generate employee CSV | GET /employee/1/csv | 200 + filtered CSV | Happy |
| TC-RPT-004 | Employee CSV service error | Service exception | 500 Internal Error | Sad |
| TC-RPT-005 | Generate category CSV | GET /category/Travel/csv | 200 + filtered CSV | Happy |
| TC-RPT-006 | Category CSV empty category | category="" | 400 Bad Request | Sad |
| TC-RPT-007 | Generate date range CSV | ?startDate&endDate | 200 + filtered CSV | Happy |
| TC-RPT-008 | Date range missing startDate | Missing startDate | 400 Bad Request | Sad |
| TC-RPT-009 | Date range invalid format | Wrong date format | 400 Bad Request | Sad |
| TC-RPT-010 | Generate pending CSV | GET /pending/csv | 200 + pending CSV | Happy |

### 1.9 Manager App (Java) - Authentication Middleware Tests

| TC ID | Description | Input | Expected Result | Type |
|-------|-------------|-------|-----------------|------|
| TC-AUTH-MW-001 | Valid manager JWT allows access | Valid manager token | Request proceeds | Happy |
| TC-AUTH-MW-002 | Missing JWT throws Unauthorized | No JWT cookie | 401 Unauthorized | Sad |
| TC-AUTH-MW-003 | Invalid JWT throws Unauthorized | Malformed token | 401 Unauthorized | Sad |
| TC-AUTH-MW-004 | Employee JWT throws Forbidden | Valid employee token | 403 Forbidden | Sad |
| TC-AUTH-MW-005 | Expired JWT throws Unauthorized | Expired token | 401 Unauthorized | Sad |
| TC-AUTH-MW-006 | Get authenticated manager | After successful auth | Returns manager User | Happy |
| TC-AUTH-MW-007 | Get manager when none in context | No auth | Returns null | Sad |

---

## 2. API Test Cases

### 2.1 Employee API - Authentication

| TC ID | Endpoint | Method | Input | Expected Status | Expected Response |
|-------|----------|--------|-------|-----------------|-------------------|
| TC-API-001 | /api/auth/login | POST | Valid credentials | 200 | {message, user} + cookie |
| TC-API-002 | /api/auth/login | POST | Invalid credentials | 401 | {error: "Invalid credentials"} |
| TC-API-003 | /api/auth/login | POST | Missing username | 400 | {error: "Username and password required"} |
| TC-API-004 | /api/auth/logout | POST | - | 200 | {message: "Logout successful"} |
| TC-API-005 | /api/auth/status | GET | No cookie | 200 | {authenticated: false} |
| TC-API-006 | /api/auth/status | GET | Valid cookie | 200 | {authenticated: true, user} |

### 2.2 Employee API - Expenses

| TC ID | Endpoint | Method | Auth | Input | Expected Status |
|-------|----------|--------|------|-------|-----------------|
| TC-API-007 | /api/expenses | POST | Yes | Valid expense | 201 |
| TC-API-008 | /api/expenses | POST | No | Valid expense | 401 |
| TC-API-009 | /api/expenses | POST | Yes | Invalid amount | 400 |
| TC-API-010 | /api/expenses | GET | Yes | - | 200 |
| TC-API-011 | /api/expenses | GET | No | - | 401 |
| TC-API-012 | /api/expenses?status=pending | GET | Yes | - | 200 |
| TC-API-013 | /api/expenses/{id} | GET | Yes | Own expense | 200 |
| TC-API-014 | /api/expenses/{id} | GET | Yes | Other's expense | 404 |
| TC-API-015 | /api/expenses/{id} | PUT | Yes | Pending expense | 200 |
| TC-API-016 | /api/expenses/{id} | PUT | Yes | Approved expense | 400 |
| TC-API-017 | /api/expenses/{id} | DELETE | Yes | Pending expense | 200 |
| TC-API-018 | /api/expenses/{id} | DELETE | Yes | Approved expense | 400 |

### 2.3 Manager API

| TC ID | Endpoint | Method | Auth | Expected Status |
|-------|----------|--------|------|-----------------|
| TC-MAPI-001 | /api/auth/login | POST | Manager creds | 200 |
| TC-MAPI-002 | /api/auth/login | POST | Employee creds | 401 |
| TC-MAPI-003 | /api/expenses/pending | GET | Yes | 200 |
| TC-MAPI-004 | /api/expenses/pending | GET | No | 401 |
| TC-MAPI-005 | /api/expenses/{id}/approve | POST | Yes | 200 |
| TC-MAPI-006 | /api/expenses/{id}/deny | POST | Yes | 200 |
| TC-MAPI-007 | /api/expenses/employee/{id} | GET | Yes | 200 |
| TC-MAPI-008 | /api/reports/expenses/csv | GET | Yes | 200 + CSV |

---

## 3. E2E Test Cases

### 3.1 Employee App Scenarios

| TC ID | Scenario | Steps | Expected Result |
|-------|----------|-------|-----------------|
| TC-E2E-001 | Successful login | 1. Navigate to login 2. Enter credentials 3. Click login | Redirected to dashboard |
| TC-E2E-002 | Failed login | 1. Navigate to login 2. Enter wrong password 3. Click login | Error message shown |
| TC-E2E-003 | Submit expense | 1. Login 2. Fill expense form 3. Submit | Expense appears in list |
| TC-E2E-004 | View expenses | 1. Login 2. Navigate to expense list | Expenses displayed |
| TC-E2E-005 | Edit expense | 1. Login 2. Click edit on pending 3. Modify 4. Save | Changes reflected |
| TC-E2E-006 | Delete expense | 1. Login 2. Click delete on pending 3. Confirm | Expense removed |
| TC-E2E-007 | Filter by status | 1. Login 2. Select status filter | Filtered list shown |

### 3.2 Manager App Scenarios

| TC ID | Scenario | Steps | Expected Result |
|-------|----------|-------|-----------------|
| TC-E2E-008 | Manager login | 1. Navigate to login 2. Enter manager creds | Redirected to dashboard |
| TC-E2E-009 | View pending | 1. Login as manager 2. View pending tab | Pending expenses listed |
| TC-E2E-010 | Approve expense | 1. Login 2. Click approve on expense | Status changes to approved |
| TC-E2E-011 | Deny with comment | 1. Login 2. Add comment 3. Click deny | Denied with comment |
| TC-E2E-012 | Generate report | 1. Login 2. Click export CSV | CSV file downloaded |

---

## 4. Performance Test Cases

### 4.1 Load Tests

| TC ID | Endpoint | Users | Duration | Target Response |
|-------|----------|-------|----------|-----------------|
| TC-PERF-001 | POST /api/auth/login | 50 | 60s | <500ms avg |
| TC-PERF-002 | GET /api/expenses | 50 | 60s | <300ms avg |
| TC-PERF-003 | POST /api/expenses | 50 | 60s | <500ms avg |
| TC-PERF-004 | GET /api/expenses/pending | 50 | 60s | <300ms avg |
| TC-PERF-005 | POST /api/expenses/{id}/approve | 50 | 60s | <500ms avg |

### 4.2 Success Rate Targets

| Metric | Target |
|--------|--------|
| Success Rate | >= 95% |
| Error Rate | < 5% |
| Throughput | > 10 req/sec |
