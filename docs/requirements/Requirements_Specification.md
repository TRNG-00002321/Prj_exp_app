# Requirements Specification - Revature Expense Manager P1

## Document Information
| Item | Details |
|------|---------|
| Project | Revature Expense Manager |
| Version | 1.0 (Phase 2) |
| Date | December 2024 |

---

## 1. Introduction

### 1.1 Purpose
This document specifies the functional and non-functional requirements for the Revature Expense Manager Phase 2, a web-based expense tracking system with comprehensive testing infrastructure.

### 1.2 Scope
The system consists of:
- **Employee Web App** (Python/Flask): Expense submission and tracking
- **Manager Web App** (Java/Javalin): Expense approval and reporting
- **Shared SQLite Database**: Persistent storage

---

## 2. Functional Requirements

### 2.1 Authentication Module

| Req ID | Requirement | Priority | App |
|--------|-------------|----------|-----|
| FR-AUTH-001 | System shall authenticate users with username and password | High | Both |
| FR-AUTH-002 | System shall generate JWT tokens for authenticated sessions | High | Both |
| FR-AUTH-003 | System shall store JWT tokens in HTTP-only cookies | High | Both |
| FR-AUTH-004 | System shall validate user role (Employee/Manager) | High | Both |
| FR-AUTH-005 | System shall invalidate sessions on logout | Medium | Both |
| FR-AUTH-006 | JWT tokens shall expire after 24 hours | Medium | Both |

### 2.2 Employee Expense Module

| Req ID | Requirement | Priority | App |
|--------|-------------|----------|-----|
| FR-EXP-001 | Employees shall submit expenses with amount, description, date | High | Employee |
| FR-EXP-002 | System shall validate amount is greater than 0 | High | Employee |
| FR-EXP-003 | System shall auto-assign "pending" status to new expenses | High | Employee |
| FR-EXP-004 | Employees shall view list of their expenses | High | Employee |
| FR-EXP-005 | Employees shall filter expenses by status | Medium | Employee |
| FR-EXP-006 | Employees shall edit pending expenses only | Medium | Employee |
| FR-EXP-007 | Employees shall delete pending expenses only | Low | Employee |
| FR-EXP-008 | Employees shall view expense history with approval comments | Medium | Employee |

### 2.3 Manager Approval Module

| Req ID | Requirement | Priority | App |
|--------|-------------|----------|-----|
| FR-MGR-001 | Managers shall view all pending expenses | High | Manager |
| FR-MGR-002 | Managers shall approve pending expenses | High | Manager |
| FR-MGR-003 | Managers shall deny pending expenses | High | Manager |
| FR-MGR-004 | Managers shall add comments to approval decisions | Medium | Manager |
| FR-MGR-005 | System shall record reviewer ID and date on decisions | High | Manager |
| FR-MGR-006 | Managers shall view expenses by employee | Medium | Manager |
| FR-MGR-007 | Managers shall generate CSV expense reports | Medium | Manager |
| FR-MGR-008 | Managers shall filter reports by date range | Low | Manager |
| FR-MGR-009 | Managers shall filter reports by category | Low | Manager |

### 2.4 Data Persistence Module

| Req ID | Requirement | Priority | App |
|--------|-------------|----------|-----|
| FR-DATA-001 | System shall persist users in SQLite database | High | Both |
| FR-DATA-002 | System shall persist expenses in SQLite database | High | Both |
| FR-DATA-003 | System shall persist approvals in SQLite database | High | Both |
| FR-DATA-004 | System shall maintain referential integrity | High | Both |

---

## 3. Non-Functional Requirements

### 3.1 Performance Requirements

| Req ID | Requirement | Target |
|--------|-------------|--------|
| NFR-PERF-001 | API response time under normal load | < 500ms |
| NFR-PERF-002 | System shall handle 50 concurrent users | 95% success rate |
| NFR-PERF-003 | Database queries shall complete | < 100ms |

### 3.2 Security Requirements

| Req ID | Requirement |
|--------|-------------|
| NFR-SEC-001 | Passwords shall not be transmitted in plain text (use HTTPS in production) |
| NFR-SEC-002 | JWT tokens shall be stored in HTTP-only cookies |
| NFR-SEC-003 | API endpoints shall validate authentication |
| NFR-SEC-004 | Cross-site request forgery protection via SameSite cookies |

### 3.3 Testing Requirements

| Req ID | Requirement |
|--------|-------------|
| NFR-TEST-001 | Unit test coverage shall be minimum 70% |
| NFR-TEST-002 | All API endpoints shall have automated tests |
| NFR-TEST-003 | E2E tests shall cover critical user flows |
| NFR-TEST-004 | Performance tests shall validate concurrent user handling |

### 3.4 Maintainability Requirements

| Req ID | Requirement |
|--------|-------------|
| NFR-MAINT-001 | Code shall follow layered architecture (API/Service/Repository) |
| NFR-MAINT-002 | Tests shall generate Allure reports |
| NFR-MAINT-003 | Code coverage reports shall be generated |

---

## 4. Database Schema

### 4.1 Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('Employee', 'Manager'))
);
```

### 4.2 Expenses Table
```sql
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    amount REAL NOT NULL CHECK(amount > 0),
    description TEXT NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### 4.3 Approvals Table
```sql
CREATE TABLE approvals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expense_id INTEGER UNIQUE NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('pending', 'approved', 'denied')),
    reviewer INTEGER,
    comment TEXT,
    review_date TEXT,
    FOREIGN KEY (expense_id) REFERENCES expenses(id),
    FOREIGN KEY (reviewer) REFERENCES users(id)
);
```

---

## 5. API Endpoints

### 5.1 Employee API (Port 5000)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/auth/login | Employee login |
| POST | /api/auth/logout | Employee logout |
| GET | /api/auth/status | Check auth status |
| POST | /api/expenses | Submit new expense |
| GET | /api/expenses | Get all user expenses |
| GET | /api/expenses/{id} | Get specific expense |
| PUT | /api/expenses/{id} | Update expense |
| DELETE | /api/expenses/{id} | Delete expense |
| GET | /health | Health check |

### 5.2 Manager API (Port 5001)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/auth/login | Manager login |
| POST | /api/auth/logout | Manager logout |
| GET | /api/auth/status | Check auth status |
| GET | /api/expenses | Get all expenses |
| GET | /api/expenses/pending | Get pending expenses |
| GET | /api/expenses/employee/{id} | Get employee's expenses |
| POST | /api/expenses/{id}/approve | Approve expense |
| POST | /api/expenses/{id}/deny | Deny expense |
| GET | /api/reports/expenses/csv | Generate CSV report |
| GET | /health | Health check |
