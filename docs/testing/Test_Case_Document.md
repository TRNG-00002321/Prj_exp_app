# Test Case Document - Revature Expense Manager P1

## Document Information
| Item | Details |
|------|---------|
| Project | Revature Expense Manager |
| Test Phase | Phase 2 Testing |
| Date | December 2024 |

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
