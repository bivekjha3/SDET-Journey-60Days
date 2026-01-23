import pytest
from selenium.webdriver.common.by import By

# We pass 'setup_browser' as an argument.
# Pytest automatically runs the code in conftest.py first.
def test_swag_labs_login(setup_browser):
    driver = setup_browser  # Get the driver from the fixture
    
    print("🧪 Test Started: Login check")
    driver.get("https://www.saucedemo.com/")
    
    # Perform Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Verify
    title_element = driver.find_element(By.CLASS_NAME, "title")
    print(f"✅ Found Page Title: {title_element.text}")
    assert title_element.text == "Products"

def test_swag_labs_invalid_login(setup_browser):
    driver = setup_browser
    
    print("🧪 Test Started: Invalid Login check")
    driver.get("https://www.saucedemo.com/")
    
    # Wrong Password
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()
    
    # Verify Error Message
    error_msg = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    print(f"⚠️ Found Error: {error_msg}")
    assert "Username and password do not match" in error_msg