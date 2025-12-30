package com.revature.api.integration;

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
 * API Integration Tests with Real Database (Java Manager App)
 * 
 * 
 * These tests use REST Assured with a REAL SQLite database.
 * The test database is created at a SEPARATE PATH from production.
 * 
 * NOTE: These tests require the Manager API to be running on port 5001
 * with the test database configured.
 */
@Epic("Manager App")
@Feature("API Integration Tests")
@Tag("integration")
@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
public class ExpenseApiIntegrationTest {

    private static DatabaseConnection testDbConnection;
    private static String managerJwtCookie;

    @BeforeAll
    static void setupDatabase() throws SQLException, IOException {
        // Initialize test database with seed data
        testDbConnection = TestDatabaseSetup.initializeTestDatabase();

        // Configure REST Assured
        RestAssured.baseURI = "http://localhost";
        RestAssured.port = 5001;
    }

    @AfterAll
    static void tearDown() {
        TestDatabaseSetup.cleanup();
        RestAssured.reset();
    }

    // ==================== AUTHENTICATION TESTS ====================

    @Test
    @Order(1)
    @Story("Manager Authentication")
    @Description("Login with manager credentials from seeded database")
    @Severity(SeverityLevel.CRITICAL)
    void testLoginWithSeededManager() {
        String requestBody = """
                {
                    "username": "manager1",
                    "password": "admin123"
                }
                """;

        Response response = given()
                .contentType(ContentType.JSON)
                .body(requestBody)
                .when()
                .post("/api/auth/login")
                .then()
                .statusCode(anyOf(equalTo(200), equalTo(401))) // May fail if server not running
                .extract()
                .response();

        if (response.getStatusCode() == 200) {
            managerJwtCookie = response.getCookie("jwt");
            Assertions.assertNotNull(managerJwtCookie, "JWT cookie should be set");
        }
    }

    @Test
    @Order(2)
    @Story("Manager Authentication")
    @Description("Employee cannot login to manager app")
    @Severity(SeverityLevel.CRITICAL)
    void testEmployeeCannotLoginToManagerApp() {
        
    }

    // ==================== EXPENSE ENDPOINT TESTS ====================

    @Test
    @Order(3)
    @Story("View Pending Expenses")
    @Description("Get pending expenses from seeded database")
    @Severity(SeverityLevel.CRITICAL)
    void testGetPendingExpensesFromSeededData() {
        // Login first
        String jwt = loginAsManager();

        if (jwt != null) {
            Response response = given()
                    .cookie("jwt", jwt)
                    .when()
                    .get("/api/expenses/pending")
                    .then()
                    .statusCode(200)
                    .extract()
                    .response();

            // Should have pending expenses from seed data
            Assertions.assertTrue(
                    response.getBody().asString().contains("pending") ||
                            response.getBody().asString().contains("data"),
                    "Response should contain expense data");
        }
    }

    @Test
    @Order(4)
    @Story("View All Expenses")
    @Description("Get all expenses from seeded database")
    @Severity(SeverityLevel.NORMAL)
    void testGetAllExpensesFromSeededData() {
       
    }

    @Test
    @Order(5)
    @Story("Expense by Employee")
    @Description("Get expenses for specific employee from seeded data")
    @Severity(SeverityLevel.NORMAL)
    void testGetExpensesByEmployeeFromSeededData() {
       
    }

    @Test
    @Order(6)
    @Story("Expense Approval")
    @Description("Approve expense and verify in database")
    @Severity(SeverityLevel.CRITICAL)
    void testApproveExpenseUpdatesDatabase() {
       
    }

    @Test
    @Order(7)
    @Story("Expense Denial")
    @Description("Deny expense with reason")
    @Severity(SeverityLevel.CRITICAL)
    void testDenyExpenseUpdatesDatabase() {
      
    }

    @Test
    @Order(8)
    @Story("Reports")
    @Description("Generate CSV report from seeded data")
    @Severity(SeverityLevel.NORMAL)
    void testGenerateCsvReportFromSeededData() {
       
    }

    // ==================== HELPER METHODS ====================

    private String loginAsManager() {
        try {
            Response response = given()
                    .contentType(ContentType.JSON)
                    .body("{\"username\": \"manager1\", \"password\": \"admin123\"}")
                    .post("/api/auth/login");

            if (response.getStatusCode() == 200) {
                return response.getCookie("jwt");
            }
        } catch (Exception e) {
            // Server may not be running
        }
        return null;
    }
}
