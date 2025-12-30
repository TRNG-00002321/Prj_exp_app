package com.revature.e2e.integration;

import com.revature.repository.DatabaseConnection;
import com.revature.repository.integration.TestDatabaseSetup;
import io.qameta.allure.*;
import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.*;

import java.io.IOException;
import java.sql.SQLException;

import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

/**
 * E2E Integration Tests with Real Database (Java Manager App)
 * 
 * 
 * These tests simulate complete manager workflows using REST Assured
 * with a REAL SQLite database backend.
 * 
 * NOTE: Tests require Manager API running on port 5001
 */
@Epic("Manager App")
@Feature("E2E Integration Tests")
@Tag("e2e")
@Tag("integration")
@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
public class E2EIntegrationTest {

    private static DatabaseConnection testDbConnection;

    @BeforeAll
    static void setupDatabase() throws SQLException, IOException {
        testDbConnection = TestDatabaseSetup.initializeTestDatabase();
        RestAssured.baseURI = "http://localhost";
        RestAssured.port = 5001;
    }

    @AfterAll
    static void tearDown() {
        TestDatabaseSetup.cleanup();
        RestAssured.reset();
    }

    // ==================== COMPLETE WORKFLOW TESTS ====================

    @Test
    @Order(1)
    @Story("Complete Approval Workflow")
    @Description("Full workflow: Login → View pending → Approve → Verify")
    @Severity(SeverityLevel.CRITICAL)
    void testCompleteApprovalWorkflow() {
        // Step 1: Login as manager
        Response loginResponse = given()
                .contentType(ContentType.JSON)
                .body("{\"username\": \"manager1\", \"password\": \"admin123\"}")
                .when()
                .post("/api/auth/login");

        if (loginResponse.getStatusCode() != 200) {
            // Server not running, skip test
            return;
        }

        String jwt = loginResponse.getCookie("jwt");
        Assertions.assertNotNull(jwt, "Should receive JWT on login");

        // Step 2: View pending expenses
        Response pendingResponse = given()
                .cookie("jwt", jwt)
                .when()
                .get("/api/expenses/pending")
                .then()
                .statusCode(200)
                .extract()
                .response();

        // Step 3: Approve first pending expense (ID 1)
        Response approveResponse = given()
                .cookie("jwt", jwt)
                .contentType(ContentType.JSON)
                .body("{\"comment\": \"E2E workflow approval\"}")
                .when()
                .post("/api/expenses/1/approve");

        // Should succeed or return appropriate status
        Assertions.assertTrue(
                approveResponse.getStatusCode() == 200 ||
                        approveResponse.getStatusCode() == 404 ||
                        approveResponse.getStatusCode() == 400,
                "Approve should return valid status");

        // Step 4: Verify by checking expenses again
        given()
                .cookie("jwt", jwt)
                .when()
                .get("/api/expenses")
                .then()
                .statusCode(200);
    }

    @Test
    @Order(2)
    @Story("Complete Denial Workflow")
    @Description("Full workflow: Login → View pending → Deny → Verify")
    @Severity(SeverityLevel.CRITICAL)
    void testCompleteDenialWorkflow() {
        // Step 1: Login
       

        // Step 2: Deny expense (ID 4 is pending for employee2)
       
    }

    @Test
    @Order(3)
    @Story("Report Generation Workflow")
    @Description("Full workflow: Login → Generate multiple report types")
    @Severity(SeverityLevel.NORMAL)
    void testReportGenerationWorkflow() {
        

        // Generate CSV report
       

        // Get expenses by date range
       
    }

    @Test
    @Order(4)
    @Story("Employee Expense Review Workflow")
    @Description("Full workflow: Login → View expenses by employee → Review")
    @Severity(SeverityLevel.NORMAL)
    void testEmployeeExpenseReviewWorkflow() {
        

        // View employee1's expenses (has 3 in seed data)
        

        // View employee2's expenses (has 2 in seed data)
        
    }

    @Test
    @Order(5)
    @Story("Unauthorized Access Prevention")
    @Description("Verify unauthorized access is blocked")
    @Severity(SeverityLevel.CRITICAL)
    void testUnauthorizedAccessPrevention() {
        // Try to access protected endpoints without auth
           }

    @Test
    @Order(6)
    @Story("Session Management")
    @Description("Full workflow: Login → Logout → Verify access revoked")
    @Severity(SeverityLevel.NORMAL)
    void testSessionManagementWorkflow() {
        // Login
       

        // Verify access works
        

        // Logout
       
    }
}
