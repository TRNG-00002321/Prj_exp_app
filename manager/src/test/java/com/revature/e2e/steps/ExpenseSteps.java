package com.revature.e2e.steps;

import io.cucumber.java.After;
import io.cucumber.java.Before;
import io.cucumber.java.en.*;
import io.github.bonigarcia.wdm.WebDriverManager;
import io.qameta.allure.Allure;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Cucumber Step Definitions for Manager E2E Tests
 * 

 * 
 * This class implements the step definitions for our Cucumber scenarios.
 */
public class ExpenseSteps {

    private WebDriver driver;
    private WebDriverWait wait;
    private static final String BASE_URL = "http://localhost:5001";

    // ==================== HOOKS ====================

    @Before
    public void setUp() {
        // Automated Driver Setup using WebDriverManager (Week 7, Thu)
        WebDriverManager.chromedriver().setup();

        // Configure Chrome options
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless"); // Run without GUI for CI/CD
        options.addArguments("--no-sandbox");
        options.addArguments("--disable-dev-shm-usage");

        driver = new ChromeDriver(options);
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));

        // Explicit wait for dynamic elements
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    @After
    public void tearDown() {
        if (driver != null) {
            // Take screenshot on failure
            try {
                byte[] screenshot = ((TakesScreenshot) driver).getScreenshotAs(OutputType.BYTES);
                Allure.getLifecycle().addAttachment(
                        "Screenshot", "image/png", "png", screenshot);
            } catch (Exception e) {
                // Ignore screenshot errors
            }
            driver.quit();
        }
    }

    // ==================== GIVEN STEPS ====================

    @Given("the Manager app is running on port 5001")
    public void theManagerAppIsRunningOnPort() {
        // Navigate to base URL to verify app is running
        driver.get(BASE_URL + "/health");
        String pageSource = driver.getPageSource();
        assertTrue(pageSource.contains("healthy"), "App should be running");
    }

    @Given("I am on the manager login page")
    public void iAmOnTheManagerLoginPage() {
        driver.get(BASE_URL + "/login.html");
    }

    @Given("I enter manager username {string}")
    public void iEnterManagerUsername(String username) {
        WebElement usernameField = driver.findElement(By.id("username"));
        usernameField.clear();
        usernameField.sendKeys(username);
    }

    @Given("I enter manager password {string}")
    public void iEnterManagerPassword(String password) {
        
    }

    @Given("I am logged in as manager {string} with password {string}")
    public void iAmLoggedInAsManager(String username, String password) {
      

        // Wait for redirect to dashboard
       
    }

    @Given("there is a pending expense to review")
    public void thereIsAPendingExpenseToReview() {
        // Assumes test data exists - in real scenario, might create via API
    }

    @Given("there is a pending expense with ID {string}")
    public void thereIsAPendingExpenseWithId(String expenseId) {
        // Store expense ID for later use
    }

    // ==================== WHEN STEPS ====================

    @When("I click the manager login button")
    public void iClickTheManagerLoginButton() {
       

        // Wait for response
       
    }

    @When("I navigate to the pending expenses tab")
    public void iNavigateToThePendingExpensesTab() {
        // Click on pending tab or navigate
       
            // Tab might already be selected or different UI
       
    }

    @When("I click the approve button for the expense")
    public void iClickTheApproveButton() {
       
    }

    @When("I enter denial reason {string}")
    public void iEnterDenialReason(String reason) {
    
    }

    @When("I click the deny button for the expense")
    public void iClickTheDenyButton() {
      
    }

    @When("I navigate to the reports section")
    public void iNavigateToTheReportsSection() {
       
            // Reports might be on same page
       
    }

    @When("I click the export CSV button")
    public void iClickTheExportCsvButton() {
      
    }

    @When("I click the manager logout button")
    public void iClickTheManagerLogoutButton() {
       
    }

    @When("I navigate to the all expenses view")
    public void iNavigateToTheAllExpensesView() {
     
            // Already on the view
       
    }

    @When("I select decision {string} with comment {string}")
    public void iSelectDecisionWithComment(String decision, String comment) {
        // Enter comment if provided
     
    }

    @When("I submit the decision")
    public void iSubmitTheDecision() {
        // Submit the decision form
      
            // Button might have different ID
        
    }

    // ==================== THEN STEPS ====================

    @Then("I should be redirected to the manager dashboard")
    public void iShouldBeRedirectedToTheManagerDashboard() {
        
    }

    @Then("I should see the expense management panel")
    public void iShouldSeeTheExpenseManagementPanel() {
        // Verify dashboard elements are visible
       
    }

    @Then("I should see a list of pending expenses")
    public void iShouldSeeAListOfPendingExpenses() {
        // Verify expenses are displayed
       
    }

    @Then("each expense should show employee name and amount and status")
    public void eachExpenseShouldShowDetails() {
        // Verify expense details are visible
    }

    @Then("the expense status should change to {string}")
    public void theExpenseStatusShouldChangeTo(String status) {
        // Wait for status update
       
    }

    @Then("I should see a success message")
    public void iShouldSeeASuccessMessage() {
       
    }

    @Then("the denial reason should be recorded")
    public void theDenialReasonShouldBeRecorded() {
        // Verify reason is saved
    }

    @Then("a CSV file should be downloaded")
    public void aCsvFileShouldBeDownloaded() {
        // Note: File download verification is complex in Selenium
        // In real tests, check download directory or response headers
    }

    @Then("the CSV should contain expense data")
    public void theCsvShouldContainExpenseData() {
        // Verify CSV content
    }

    @Then("I should be redirected to the login page")
    public void iShouldBeRedirectedToTheLoginPage() {
        
    }

    @Then("attempting to access the dashboard should redirect to login")
    public void attemptingToAccessTheDashboardShouldRedirectToLogin() {
     
        // Should be redirected or show unauthorized
    }

    @Then("the expense should have status {string}")
    public void theExpenseShouldHaveStatus(String status) {
       
    }

    @Then("I should see expenses with all statuses")
    public void iShouldSeeExpensesWithAllStatuses() {
        // Verify all statuses are visible
    }

    @Then("I should be able to filter by status")
    public void iShouldBeAbleToFilterByStatus() {
        // Verify filter is available
    }
}
