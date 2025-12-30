package com.revature.repository.integration;

import com.revature.repository.DatabaseConnection;
import com.revature.repository.User;
import com.revature.repository.UserRepository;
import io.qameta.allure.*;
import org.junit.jupiter.api.*;

import java.io.IOException;
import java.sql.SQLException;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Integration Tests for UserRepository
 * 
 * 
 * Tests UserRepository with a REAL SQLite database.
 * Uses separate test database path from production.
 */
@Epic("Manager App")
@Feature("User Repository Integration")
@Tag("integration")
public class UserRepositoryIntegrationTest {

    private static DatabaseConnection testDbConnection;
    private static UserRepository userRepository;

    @BeforeAll
    static void setUpDatabase() throws SQLException, IOException {
        testDbConnection = TestDatabaseSetup.initializeTestDatabase();
        userRepository = new UserRepository(testDbConnection);
    }

    @AfterAll
    static void tearDownDatabase() {
        TestDatabaseSetup.cleanup();
    }

    @Test
    @Story("Find User")
    @Description("Find user by ID from real database")
    @Severity(SeverityLevel.CRITICAL)
    void testFindByIdFromRealDatabase() {
        // Act
        Optional<User> result = userRepository.findById(1);

        // Assert
        assertTrue(result.isPresent(), "User should be found");
        assertEquals("employee1", result.get().getUsername());
        assertEquals("Employee", result.get().getRole());
    }

    @Test
    @Story("Find User")
    @Description("Find user by username from real database")
    @Severity(SeverityLevel.CRITICAL)
    void testFindByUsernameFromRealDatabase() {
        // Act
        

        // Assert
       
    }

    @Test
    @Story("Find User")
    @Description("Find non-existent user returns empty")
    @Severity(SeverityLevel.NORMAL)
    void testFindNonExistentUser() {
        // Act
      

        // Assert
       
    }

    @Test
    @Story("Find User")
    @Description("Find manager user from real database")
    @Severity(SeverityLevel.NORMAL)
    void testFindManagerUser() {
        // Act
        

        // Assert
       
    }

    @Test
    @Story("Find User")
    @Description("Verify all seeded users exist")
    @Severity(SeverityLevel.MINOR)
    void testAllSeededUsersExist() {
        // Verify all 5 users from seed data exist
      

        // ID 6 should not exist
        
    }
}
