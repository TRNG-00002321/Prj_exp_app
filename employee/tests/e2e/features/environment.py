"""
Behave Environment Configuration


- before_all: Setup once before all tests
- after_all: Cleanup after all tests
- before_scenario: Setup before each scenario
- after_scenario: Cleanup after each scenario
"""
import allure


def before_all(context):
    """
    Setup that runs once before all tests.
    """
    context.base_url = "http://localhost:5000"


def after_scenario(context, scenario):
    """
    Cleanup after each scenario.
    
    This ensures the browser is closed even if tests fail.
    """
    if hasattr(context, 'driver') and context.driver:
        # Take screenshot on failure for debugging
        if scenario.status == "failed":
            try:
                screenshot = context.driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name="failure_screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception:
                pass
        
        context.driver.quit()


def after_all(context):
    """
    Final cleanup after all tests complete.
    """
    pass
