# Requirements Traceability Matrix (RTM)

## Document Information
| Item | Details |
|------|---------|
| Project | Revature Expense Manager P1 |
| Date | December 2024 |

---

## Traceability Matrix

| Requirement ID | Requirement Description | Test Case IDs | Test Type | Status |
|----------------|------------------------|---------------|-----------|--------|
| **Authentication Module** |||||
| FR-AUTH-001 | Authenticate with username/password | TC-AUTH-001, TC-AUTH-002, TC-AUTH-003, TC-API-001, TC-API-002 | Unit, API | Planned |
| FR-AUTH-002 | Generate JWT tokens | TC-AUTH-004, TC-MAUTH-003 | Unit | Planned |
| FR-AUTH-003 | Store JWT in HTTP-only cookies | TC-API-001, TC-E2E-001 | API, E2E | Planned |
| FR-AUTH-004 | Validate user role | TC-MAUTH-002, TC-MAUTH-005, TC-MAUTH-006 | Unit | Planned |
| FR-AUTH-005 | Invalidate sessions on logout | TC-API-004 | API | Planned |
| FR-AUTH-006 | JWT expiry after 24 hours | TC-AUTH-006 | Unit | Planned |
| **Employee Expense Module** |||||
| FR-EXP-001 | Submit expense with amount, description, date | TC-EXP-001, TC-API-007 | Unit, API | Planned |
| FR-EXP-002 | Validate amount > 0 | TC-EXP-002, TC-EXP-003, TC-API-009 | Unit, API | Planned |
| FR-EXP-003 | Auto-assign pending status | TC-EXP-001 | Unit | Planned |
| FR-EXP-004 | View list of expenses | TC-EXP-005, TC-API-010, TC-E2E-004 | Unit, API, E2E | Planned |
| FR-EXP-005 | Filter expenses by status | TC-EXP-012, TC-API-012, TC-E2E-007 | Unit, API, E2E | Planned |
| FR-EXP-006 | Edit pending expenses only | TC-EXP-008, TC-EXP-009, TC-API-015, TC-API-016, TC-E2E-005 | Unit, API, E2E | Planned |
| FR-EXP-007 | Delete pending expenses only | TC-EXP-010, TC-EXP-011, TC-API-017, TC-API-018, TC-E2E-006 | Unit, API, E2E | Planned |
| FR-EXP-008 | View expense history with comments | TC-EXP-005, TC-API-010 | Unit, API | Planned |
| **Manager Approval Module** |||||
| FR-MGR-001 | View all pending expenses | TC-MEXP-001, TC-MAPI-003, TC-E2E-009 | Unit, API, E2E | Planned |
| FR-MGR-002 | Approve pending expenses | TC-MEXP-002, TC-MAPI-005, TC-E2E-010 | Unit, API, E2E | Planned |
| FR-MGR-003 | Deny pending expenses | TC-MEXP-003, TC-MAPI-006, TC-E2E-011 | Unit, API, E2E | Planned |
| FR-MGR-004 | Add comments to decisions | TC-MEXP-004, TC-E2E-011 | Unit, E2E | Planned |
| FR-MGR-005 | Record reviewer ID and date | TC-MEXP-002, TC-MEXP-003 | Unit | Planned |
| FR-MGR-006 | View expenses by employee | TC-MEXP-005, TC-MAPI-007 | Unit, API | Planned |
| FR-MGR-007 | Generate CSV reports | TC-MEXP-006, TC-MAPI-008, TC-E2E-012 | Unit, API, E2E | Planned |
| FR-MGR-008 | Filter reports by date range | TC-MEXP-008 | Unit | Planned |
| FR-MGR-009 | Filter reports by category | TC-MEXP-007 | Unit | Planned |
| **Data Persistence Module** |||||
| FR-DATA-001 | Persist users in SQLite | TC-AUTH-001 | Unit | Planned |
| FR-DATA-002 | Persist expenses in SQLite | TC-EXP-001 | Unit | Planned |
| FR-DATA-003 | Persist approvals in SQLite | TC-EXP-001, TC-MEXP-002 | Unit | Planned |
| FR-DATA-004 | Maintain referential integrity | TC-EXP-010 | Unit | Planned |
| **Non-Functional Requirements** |||||
| NFR-PERF-001 | API response < 500ms | TC-PERF-001 through TC-PERF-005 | Performance | Planned |
| NFR-PERF-002 | Handle 50 concurrent users | TC-PERF-001 through TC-PERF-005 | Performance | Planned |
| NFR-SEC-002 | JWT in HTTP-only cookies | TC-API-001 | API | Planned |
| NFR-SEC-003 | Validate authentication | TC-API-008, TC-API-011, TC-MAPI-004 | API | Planned |
| NFR-TEST-001 | 70% code coverage | Coverage Reports | Unit | Planned |
| NFR-TEST-002 | All endpoints tested | TC-API-*, TC-MAPI-* | API | Planned |
| NFR-TEST-003 | E2E critical flows | TC-E2E-001 through TC-E2E-012 | E2E | Planned |
| NFR-TEST-004 | Performance validation | TC-PERF-* | Performance | Planned |

---

## Coverage Summary

| Requirement Category | Total | Covered | Coverage % |
|---------------------|-------|---------|------------|
| Authentication | 6 | 6 | 100% |
| Employee Expense | 8 | 8 | 100% |
| Manager Approval | 9 | 9 | 100% |
| Data Persistence | 4 | 4 | 100% |
| Non-Functional | 8 | 8 | 100% |
| **Total** | **35** | **35** | **100%** |

---

## Test Type Distribution

| Test Type | Count | Percentage |
|-----------|-------|------------|
| Unit Tests | 26 | 45% |
| API Tests | 20 | 34% |
| E2E Tests | 12 | 21% |

---

## Notes
- All test cases are mapped to Week 5-9 training schedule concepts
- Unit tests use pytest-mock (Python) and Mockito (Java)
- API tests use requests module (Python) and REST Assured (Java)
- E2E tests use Behave+Selenium (Python) and Cucumber+Selenium (Java)
- Performance tests use JMeter for both applications
