import pytest
from selenium.webdriver.common.by import By
import os

def test_sauce_demo_screenshot(setup_browser):
    driver = setup_browser
    driver.get("https://www.saucedemo.com/")
    
    print("🧪 Attempting login...")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # --- INTENTIONAL FAILURE ---
    # We are looking for a title that DOES NOT EXIST to force a failure
    try:
        print("🧐 Verifying page title...")
        title = driver.find_element(By.CLASS_NAME, "title").text
        
        # This will fail because 'WRONG TITLE' != 'Products'
        assert title == "WRONG TITLE"
        
    except AssertionError as e:
        print(f"❌ Assertion Failed! Capturing screenshot...")
        
        # Create a folder for screenshots if it doesn't exist
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
            
        # Save the screenshot
        driver.save_screenshot("screenshots/failure_day25.png")
        raise e # Still throw the error so Pytest knows it failed

    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        driver.save_screenshot("screenshots/error_day25.png")
        raise e