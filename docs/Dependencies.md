# Project Dependencies - Revature Expense Manager P1

## Employee App (Python)

### Core Dependencies
| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 3.0.0+ | Web framework |
| PyJWT | 2.8.0+ | JWT token handling |

### Testing Dependencies
| Package | Version | Purpose |
|---------|---------|---------|
| pytest | 7.4.0+ | Unit testing framework |
| pytest-mock | 3.12.0+ | Mocking support for pytest |
| coverage | 7.3.0+ | Code coverage reporting |
| allure-pytest | 2.13.0+ | Allure test reporter |
| requests | 2.31.0+ | API testing HTTP client |
| behave | 1.2.6+ | BDD testing framework |
| selenium | 4.15.0+ | Browser automation | 
| webdriver-manager | 4.0.0+ | Browser driver management | 
| allure-behave | 2.13.0+ | Allure for Behave |

### requirements.txt (Testing)
```
# Core
Flask>=3.0.0
PyJWT>=2.8.0

# Testing - Unit
pytest>=7.4.0
pytest-mock>=3.12.0
coverage>=7.3.0
allure-pytest>=2.13.0

# Testing - API 
requests>=2.31.0

# Testing - E2E 
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
| GroupId | ArtifactId | Version | Purpose | 
|---------|------------|---------|---------|
| org.junit.jupiter | junit-jupiter | 5.10.0 | Unit testing ||
| org.mockito | mockito-core | 5.7.0 | Mocking framework |
| org.mockito | mockito-junit-jupiter | 5.7.0 | Mockito-JUnit integration |
| io.rest-assured | rest-assured | 5.4.0 | API testing |
| org.seleniumhq.selenium | selenium-java | 4.15.0 | Browser automation |
| io.github.bonigarcia | webdrivermanager | 5.6.0 | Driver management |
| io.cucumber | cucumber-java | 7.14.0 | BDD framework |
| io.cucumber | cucumber-junit-platform-engine | 7.14.0 | Cucumber-JUnit |
| io.qameta.allure | allure-junit5 | 2.25.0 | Allure reporting | 
| io.qameta.allure | allure-cucumber7-jvm | 2.25.0 | Allure for Cucumber |
| org.jacoco | jacoco-maven-plugin | 0.8.11 | Code coverage |

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
