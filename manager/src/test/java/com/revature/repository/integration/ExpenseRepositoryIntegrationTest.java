package com.revature.repository.integration;

import com.revature.repository.DatabaseConnection;
import com.revature.repository.Expense;
import com.revature.repository.ExpenseRepository;
import com.revature.repository.ExpenseWithUser;
import io.qameta.allure.*;
import org.junit.jupiter.api.*;

import java.io.IOException;
import java.sql.SQLException;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Integration Tests for ExpenseRepository
 * 
 * 
 * Tests ExpenseRepository with a REAL SQLite database.
 * Uses separate test database path from production.
 */
@Epic("Manager App")
@Feature("Expense Repository Integration")
@Tag("integration")
public class ExpenseRepositoryIntegrationTest {

    private static DatabaseConnection testDbConnection;
    private static ExpenseRepository expenseRepository;

    @BeforeAll
    static void setUpDatabase() throws SQLException, IOException {
        testDbConnection = TestDatabaseSetup.initializeTestDatabase();
        expenseRepository = new ExpenseRepository(testDbConnection);
    }

    @AfterAll
    static void tearDownDatabase() {
        TestDatabaseSetup.cleanup();
    }

    @Test
    @Story("Find Expense")
    @Description("Find expense by ID from real database")
    @Severity(SeverityLevel.CRITICAL)
    void testFindByIdFromRealDatabase() {
        // Act
        Optional<Expense> result = expenseRepository.findById(1);

        // Assert
        assertTrue(result.isPresent(), "Expense should be found");
        assertEquals(150.00, result.get().getAmount(), 0.01);
        assertEquals("Business lunch", result.get().getDescription());
        assertEquals(1, result.get().getUserId());
    }

    @Test
    @Story("Find Pending Expenses")
    @Description("Find all pending expenses with user info from real database")
    @Severity(SeverityLevel.CRITICAL)
    void testFindPendingExpensesWithUsers() {
        // Act
        

        // Assert
        

        // All returned expenses should have 'pending' status
       
    }

    @Test
    @Story("Find Expenses by User")
    @Description("Find all expenses for a specific user from real database")
    @Severity(SeverityLevel.NORMAL)
    void testFindExpensesByUser() {
        // Act - employee1 (id=1) has 3 expenses in seed data
      

        // Assert
       

        // Verify all belong to user 1
        
    }

    @Test
    @Story("Find Expenses by Date Range")
    @Description("Find expenses by date range from real database")
    @Severity(SeverityLevel.NORMAL)
    void testFindExpensesByDateRange() {
        // Act - find expenses between Dec 1-10
      

        // Assert
       

        // All should be within the date range
       
    }

    @Test
    @Story("Find Expenses by Category")
    @Description("Find expenses by description/category from real database")
    @Severity(SeverityLevel.NORMAL)
    void testFindExpensesByCategory() {
        // Act - find expenses with "lunch" in description
      

        // Assert
        

        // All should contain 'lunch' in description (case-insensitive from SQL LIKE)
        
    }

    @Test
    @Story("Find All Expenses")
    @Description("Find all expenses with users from real database")
    @Severity(SeverityLevel.NORMAL)
    void testFindAllExpensesWithUsers() {
        // Act
        

        // Assert - should have 7 expenses from seed data
     

        // Each should have complete data
        
    }

    @Test
    @Story("Find Expense")
    @Description("Find non-existent expense returns empty")
    @Severity(SeverityLevel.MINOR)
    void testFindNonExistentExpense() {
        // Act
       

        // Assert
       
    }
}
