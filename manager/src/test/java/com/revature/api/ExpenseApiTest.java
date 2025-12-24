package com.revature.api;

import io.qameta.allure.*;
import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;
import org.junit.jupiter.api.*;

import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

/**
 * API Tests using REST Assured
 * 
 * Test Cases Covered: TC-MAPI-001 through TC-MAPI-008
 * 
 * IMPORTANT: Manager API must be running on port 5001
 */
@Epic("Manager App")
@Feature("Manager API")
@DisplayName("Manager API Tests (REST Assured)")
@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
class ExpenseApiTest {

    private static String managerJwtCookie;

    @BeforeAll
    static void setupBaseUri() {
        // Configure REST Assured base URI
        RestAssured.baseURI = "http://localhost";
        RestAssured.port = 5001;
    }

    @AfterAll
    static void cleanup() {
        RestAssured.reset();
    }

    // ==================== AUTHENTICATION TESTS ====================

    @Test
    @Order(1)
    @Story("Manager Authentication")
    @DisplayName("TC-MAPI-001: Manager login with valid credentials")
    @Description("Test that a manager can login successfully")
    @Severity(SeverityLevel.BLOCKER)
    void testManagerLogin_ValidCredentials_Returns200() {
        // Arrange: Login credentials
        String requestBody = """
                {
                    "username": "manager1",
                    "password": "password123"
                }
                """;

        // Act & Assert using REST Assured fluent API
        Response response = given()
                .contentType(ContentType.JSON)
                .body(requestBody)
                .when()
                .post("/api/auth/login")
                .then()
                .statusCode(200)
                .body("success", equalTo(true))
                .body("message", containsString("successful"))
                .body("user.role", equalTo("Manager"))
                .extract()
                .response();

        // Store cookie for subsequent requests
        managerJwtCookie = response.getCookie("jwt");
    }

    @Test
    @Order(2)
    @Story("Manager Authentication")
    @DisplayName("TC-MAPI-002: Employee cannot login to manager app")
    @Description("Test that an employee is rejected from manager app")
    @Severity(SeverityLevel.CRITICAL)
    void testEmployeeLogin_ToManagerApp_Returns401() {
       
    }

    // ==================== EXPENSE ENDPOINT TESTS ====================

    @Test
    @Order(3)
    @Story("View Pending Expenses")
    @DisplayName("TC-MAPI-003: Get pending expenses when authenticated")
    @Description("Test retrieving pending expenses as authenticated manager")
    @Severity(SeverityLevel.CRITICAL)
    void testGetPendingExpenses_Authenticated_Returns200() {
        // First login to get cookie
        

        // Now access protected endpoint
       
    }

    @Test
    @Order(4)
    @Story("View Pending Expenses")
    @DisplayName("TC-MAPI-004: Get pending expenses without auth returns 401")
    @Description("Test that unauthenticated access is rejected")
    @Severity(SeverityLevel.CRITICAL)
    void testGetPendingExpenses_Unauthenticated_Returns401() {
      
    }

    @Test
    @Order(5)
    @Story("Expense Approval")
    @DisplayName("TC-MAPI-005: Approve expense")
    @Description("Test approving an expense as manager")
    @Severity(SeverityLevel.CRITICAL)
    void testApproveExpense_AsManager_Returns200() {
        // Login first
       

        // Approve expense ID 1 (if exists)
       

        // This may return 200 or 404 depending on data
       

        // Accept either success or not found (if expense doesn't exist)
       
    }

    @Test
    @Order(6)
    @Story("Expense Denial")
    @DisplayName("TC-MAPI-006: Deny expense")
    @Description("Test denying an expense with a reason")
    @Severity(SeverityLevel.CRITICAL)
    void testDenyExpense_AsManager_Returns200() {
       
    }

    @Test
    @Order(7)
    @Story("Employee Expenses")
    @DisplayName("TC-MAPI-007: Get expenses for employee")
    @Description("Test retrieving expenses for a specific employee ID")
    @Severity(SeverityLevel.NORMAL)
    void testGetExpensesByEmployee_Returns200() {
       
    }

    @Test
    @Order(8)
    @Story("Report Generation")
    @DisplayName("TC-MAPI-008: Generate CSV report")
    @Description("Test generating a CSV expense report")
    @Severity(SeverityLevel.NORMAL)
    void testGenerateCsvReport_ReturnsCSV() {
       
    }

    // ==================== HEALTH CHECK ====================

    @Test
    @Order(0)
    @Story("Health Check")
    @DisplayName("Health check endpoint")
    @Severity(SeverityLevel.NORMAL)
    void testHealthCheck_Returns200() {
     
    }
}
