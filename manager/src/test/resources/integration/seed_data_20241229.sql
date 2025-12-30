-- Seed Data for Java Manager App Integration Tests
-- Database: test_expense_manager.db
-- Created: 2024-12-29T19:10:00-06:00
-- Purpose: Populate test database with sample data for integration testing

-- Clear existing data (in reverse order due to foreign key constraints)
DELETE FROM approvals;
DELETE FROM expenses;
DELETE FROM users;

-- Insert test users
INSERT INTO users (id, username, password, role) VALUES 
    (1, 'employee1', 'password123', 'Employee'),
    (2, 'employee2', 'password456', 'Employee'),
    (3, 'manager1', 'admin123', 'Manager'),
    (4, 'manager2', 'admin456', 'Manager'),
    (5, 'testuser', 'testpass', 'Employee');

-- Insert test expenses
INSERT INTO expenses (id, user_id, amount, description, date) VALUES 
    (1, 1, 150.00, 'Business lunch', '2024-12-01'),
    (2, 1, 250.50, 'Travel expense', '2024-12-05'),
    (3, 1, 75.00, 'Office supplies', '2024-12-10'),
    (4, 2, 120.00, 'Client meeting', '2024-12-03'),
    (5, 2, 500.00, 'Conference registration', '2024-12-08'),
    (6, 5, 200.00, 'Team dinner', '2024-12-15'),
    (7, 5, 80.00, 'Parking fees', '2024-12-20');

-- Insert test approvals (matching expense IDs)
INSERT INTO approvals (id, expense_id, status, reviewer, comment, review_date) VALUES 
    (1, 1, 'pending', NULL, NULL, NULL),
    (2, 2, 'approved', 3, 'Approved for travel', '2024-12-06'),
    (3, 3, 'denied', 3, 'Exceeds budget limit', '2024-12-11'),
    (4, 4, 'pending', NULL, NULL, NULL),
    (5, 5, 'approved', 3, 'Conference approved', '2024-12-09'),
    (6, 6, 'pending', NULL, NULL, NULL),
    (7, 7, 'approved', 4, 'Approved by manager2', '2024-12-21');
