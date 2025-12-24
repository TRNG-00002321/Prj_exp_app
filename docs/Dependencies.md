# Project Dependencies - Revature Expense Manager P1

## Employee App (Python)

### Core Dependencies
| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 3.0.0+ | Web framework |
| PyJWT | 2.8.0+ | JWT token handling |

### Testing Dependencies
| Package | Version | Purpose | Test Layer |
|---------|---------|---------|------------|
| pytest | 7.4.0+ | Unit testing framework | All |
| pytest-mock | 3.12.0+ | Mocking support for pytest | Unit |
| coverage | 7.3.0+ | Code coverage reporting | All |
| allure-pytest | 2.13.0+ | Allure test reporter | All |
| requests | 2.31.0+ | API testing HTTP client | API |
| behave | 1.2.6+ | BDD testing framework | E2E |
| selenium | 4.15.0+ | Browser automation | E2E |
| webdriver-manager | 4.0.0+ | Browser driver management | E2E |
| allure-behave | 2.13.0+ | Allure for Behave | E2E |

### Test Files Summary (76 Unit Tests)
| Layer | Test File | Tests |
|-------|-----------|-------|
| Service | test_authentication_service.py | 13 |
| Service | test_expense_service.py | 13 |
| Controller | test_auth_controller.py | 11 |
| Controller | test_expense_controller.py | 21 |
| Repository | test_repositories.py | 17 |

### requirements.txt (Testing)
```
# Core
Flask>=3.0.0
PyJWT>=2.8.0

# Testing - Unit (Week 6)
pytest>=7.4.0
pytest-mock>=3.12.0
coverage>=7.3.0
allure-pytest>=2.13.0

# Testing - API (Week 7)
requests>=2.31.0

# Testing - E2E (Week 8)
behave>=1.2.6
selenium>=4.15.0
webdriver-manager>=4.0.0
allure-behave>=2.13.0
```

---

## Manager App (Java)

### Core Dependencies (pom.xml)
| GroupId | ArtifactId | Version | Purpose |
|---------|------------|---------|---------|
| io.javalin | javalin | 6.7.0 | Web framework |
| org.xerial | sqlite-jdbc | 3.50.3.0 | SQLite database |
| com.fasterxml.jackson.core | jackson-databind | 2.18.2 | JSON serialization |
| org.slf4j | slf4j-simple | 2.0.16 | Logging |
| com.auth0 | java-jwt | 4.5.0 | JWT token handling |

### Testing Dependencies
| GroupId | ArtifactId | Version | Purpose | Test Layer |
|---------|------------|---------|---------|------|
| org.junit.jupiter | junit-jupiter | 5.10.0 | Unit testing | All |
| org.mockito | mockito-core | 5.7.0 | Mocking framework | Unit |
| org.mockito | mockito-junit-jupiter | 5.7.0 | Mockito-JUnit integration | Unit |
| io.rest-assured | rest-assured | 5.4.0 | API testing | API |
| org.seleniumhq.selenium | selenium-java | 4.15.0 | Browser automation | E2E |
| io.github.bonigarcia | webdrivermanager | 5.6.0 | Driver management | E2E |
| io.cucumber | cucumber-java | 7.14.0 | BDD framework | E2E |
| io.cucumber | cucumber-junit-platform-engine | 7.14.0 | Cucumber-JUnit | E2E |
| io.qameta.allure | allure-junit5 | 2.25.0 | Allure reporting | All |
| io.qameta.allure | allure-cucumber7-jvm | 2.25.0 | Allure for Cucumber | E2E |
| org.jacoco | jacoco-maven-plugin | 0.8.11 | Code coverage | All |

### Test Files Summary (83 Unit Tests)
| Layer | Test File | Tests |
|-------|-----------|-------|
| Service | AuthenticationServiceTest.java | 10 |
| Service | ExpenseServiceTest.java | 17 |
| Controller | ExpenseControllerTest.java | 12 |
| Controller | ReportControllerTest.java | 12 |
| Controller | AuthenticationMiddlewareTest.java | 7 |
| Repository | UserRepositoryTest.java | 6 |
| Repository | ExpenseRepositoryTest.java | 9 |
| Repository | ApprovalRepositoryTest.java | 10 |

---

## Performance Testing Tools

| Tool | Version | Purpose |
|------|---------|---------|
| Apache JMeter | 5.6+ | Performance/load testing |
| Allure | 2.25.0+ | Test report generation |

---

## Browser Requirements

| Browser | Version | Purpose |
|---------|---------|---------|
| Google Chrome | Latest | Selenium E2E testing |
| ChromeDriver | Auto-managed | Chrome automation |

---

## Test Coverage Summary

| App | Total Unit Tests | Pass Rate | Coverage |
|-----|------------------|-----------|----------|
| Employee (Python) | 76 | 98.7% | 85% |
| Manager (Java) | 83 | 100% | 83% |
| **Total** | **159** | **99.4%** | **84%** |

---

## Installation Commands

### Python
```bash
pip install -r requirements.txt
```

### Java
```bash
mvn clean install
```

### JMeter
```bash
# Download from https://jmeter.apache.org/download_jmeter.cgi
# Or use Chocolatey on Windows:
choco install jmeter
```

### Allure CLI
```bash
# Windows (Scoop)
scoop install allure

# Windows (Chocolatey)
choco install allure
```

---

## Test Execution Commands

### Python Unit Tests
```bash
cd employee
python -m pytest tests/unit/ -v --alluredir=allure-results
```

### Java Unit Tests
```bash
cd manager
mvn test
mvn allure:report
```

