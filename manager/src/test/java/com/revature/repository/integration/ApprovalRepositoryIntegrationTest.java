package com.revature.repository.integration;

import com.revature.repository.Approval;
import com.revature.repository.ApprovalRepository;
import com.revature.repository.DatabaseConnection;
import io.qameta.allure.*;
import org.junit.jupiter.api.*;

import java.io.IOException;
import java.sql.SQLException;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Integration Tests for ApprovalRepository
 * 
 * 
 * Tests ApprovalRepository with a REAL SQLite database.
 * Uses separate test database path from production.
 */
@Epic("Manager App")
@Feature("Approval Repository Integration")
@Tag("integration")
public class ApprovalRepositoryIntegrationTest {

    private static DatabaseConnection testDbConnection;
    private static ApprovalRepository approvalRepository;

    @BeforeAll
    static void setUpDatabase() throws SQLException, IOException {
        testDbConnection = TestDatabaseSetup.initializeTestDatabase();
        approvalRepository = new ApprovalRepository(testDbConnection);
    }

    @AfterAll
    static void tearDownDatabase() {
        TestDatabaseSetup.cleanup();
    }

    @Test
    @Story("Find Approval")
    @Description("Find approval by expense ID from real database")
    @Severity(SeverityLevel.CRITICAL)
    void testFindByExpenseIdFromRealDatabase() {
        // Act
        Optional<Approval> result = approvalRepository.findByExpenseId(2);

        // Assert
        assertTrue(result.isPresent(), "Approval should be found");
        assertEquals("approved", result.get().getStatus());
        assertEquals(3, result.get().getReviewer()); // manager1
        assertEquals("Approved for travel", result.get().getComment());
    }

    @Test
    @Story("Find Approval")
    @Description("Find pending approval from real database")
    @Severity(SeverityLevel.NORMAL)
    void testFindPendingApproval() {
        // Act
       

        // Assert
       
    }

    @Test
    @Story("Find Approval")
    @Description("Find denied approval from real database")
    @Severity(SeverityLevel.NORMAL)
    void testFindDeniedApproval() {
        // Act
        

        // Assert
       
    }

    @Test
    @Story("Update Approval")
    @Description("Update approval status in real database")
    @Severity(SeverityLevel.CRITICAL)
    void testUpdateApprovalStatus() {
        // Arrange - expense 4 is pending
       

        // Act
       

        // Assert
       

        // Verify the update
       
    }

    @Test
    @Story("Create Approval")
    @Description("Create new approval record in real database")
    @Severity(SeverityLevel.CRITICAL)
    void testCreateApproval() {
        // Act - create approval for a new expense (we'll use ID 100)
       

        // Assert
        

        // Verify by finding it
       
    }

    @Test
    @Story("Find Approval")
    @Description("Find non-existent approval returns empty")
    @Severity(SeverityLevel.MINOR)
    void testFindNonExistentApproval() {
        // Act
     

        // Assert
       
    }

    @Test
    @Story("Update Approval")
    @Description("Update non-existent approval returns false")
    @Severity(SeverityLevel.MINOR)
    void testUpdateNonExistentApproval() {
        // Act
     

        // Assert
        
    }
}
