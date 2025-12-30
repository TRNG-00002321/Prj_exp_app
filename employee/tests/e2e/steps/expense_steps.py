"""
Behave Step Definitions for Expense Management

- Step definitions implementation
- Using Selenium with Behave
- Page Object Model integration
- Context object for sharing state


"""
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


# ==================== SETUP STEPS ====================

@given('the Employee app is running on port 5000')
def step_app_running(context):
    """
    Verify the app is accessible.
    
   Setting up the test environment
    """
    context.base_url = "http://localhost:5000"
    
    # Setup Chrome WebDriver with options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run without GUI for CI/CD
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Auto-install and setup ChromeDriver
    service = ChromeService(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.implicitly_wait(10)


@given('I am on the login page')
def step_on_login_page(context):
    """
    Navigate to the login page.
      
    """
    context.driver.get(f"{context.base_url}/login")
    assert "login" in context.driver.current_url.lower() or \
           context.driver.find_element(By.ID, "username")


# ==================== LOGIN STEPS ====================

@given('I enter username "{username}"')
def step_enter_username(context, username):
    """
    Enter username in the login form.
    
    """
   


@given('I enter password "{password}"')
def step_enter_password(context, password):
    """
    Enter password in the login form.
    """
   


@when('I click the login button')
def step_click_login(context):
    """
    Click the login button.
    
    """
  
@then('I should be redirected to the expense dashboard')
def step_redirected_to_dashboard(context):
    """
    Verify redirection to dashboard.
   
    """
   
@then('I should see a welcome message')
def step_see_welcome_message(context):
    """Verify welcome message is displayed."""
    # Look for any welcome text on the page
   

@then('I should see an error message "{message}"')
def step_see_error_message(context, message):
    """Verify error message is displayed."""
  


@then('I should remain on the login page')
def step_remain_on_login(context):
    """Verify still on login page."""
   

# ==================== AUTHENTICATED STEPS ====================

@given('I am logged in as "{username}" with password "{password}"')
def step_logged_in(context, username, password):
    """
    Login as specified user.
      
    """
   


@given('I have a pending expense')
def step_has_pending_expense(context):
    """Ensure user has at least one pending expense."""
    # This step assumes the test data includes a pending expense
    # In a real test, you might create one via API
    pass


# ==================== EXPENSE SUBMISSION STEPS ====================

@when('I navigate to the expense submission form')
def step_navigate_to_form(context):
    """Navigate to the expense submission form."""
    # Click on "New Expense" or navigate to form
   


@when('I enter expense amount "{amount}"')
def step_enter_amount(context, amount):
    """Enter expense amount."""
  

@when('I enter expense description "{description}"')
def step_enter_description(context, description):
    """Enter expense description."""
  
@when("I select today's date")
def step_select_date(context):
    """Select today's date for the expense."""
    
@when('I click the submit button')
def step_click_submit(context):
    """Click the expense submit button."""
   
@then('I should see a success message')
def step_see_success(context):
    """Verify success message is displayed."""
   

@then('the expense should appear in my expense list with status "{status}"')
def step_expense_in_list(context, status):
    """Verify expense appears in the list."""
  
# ==================== EXPENSE LIST STEPS ====================

@when('I navigate to the expense list')
def step_navigate_to_list(context):
    """Navigate to expense list page."""
   
@then('I should see a table of my expenses')
def step_see_expense_table(context):
    """Verify expense table is displayed."""
    # Look for table or expense list elements
 

@then('each expense should show amount, description, date, and status')
def step_expense_has_details(context):
    """Verify expense details are visible."""
    # This is a display verification
    pass


# ==================== FILTER STEPS ====================

@when('I filter by status "{status}"')
def step_filter_by_status(context, status):
    """Filter expenses by status."""
   

@then('I should only see expenses with status "{status}"')
def step_only_status(context, status):
    """Verify only filtered expenses are shown."""
    # This verifies the filtering worked
    pass


# ==================== EDIT STEPS ====================

@when('I click the edit button for the pending expense')
def step_click_edit(context):
    """Click edit on a pending expense."""
 

@when('I change the amount to "{amount}"')
def step_change_amount(context, amount):
    """Change expense amount."""
 

@when('I change the description to "{description}"')
def step_change_description(context, description):
    """Change expense description."""
   

@when('I save the changes')
def step_save_changes(context):
    """Save edited expense."""
  
@then('I should see the updated expense in the list')
def step_see_updated(context):
    """Verify update was successful."""
    pass


@then('the expense amount should be "{amount}"')
def step_expense_amount(context, amount):
    """Verify expense amount."""
 
# ==================== LOGOUT STEPS ====================

@when('I click the logout button')
def step_click_logout(context):
    """Click the logout button."""
  

@then('I should be redirected to the login page')
def step_redirected_to_login(context):
    """Verify redirection to login."""
   

@then('I should not be able to access the dashboard')
def step_no_dashboard_access(context):
    """Verify dashboard is not accessible."""
  
    # Should redirect to login or show unauthorized
