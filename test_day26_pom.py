import pytest
from pages.login_page import LoginPage # Import our blueprint

def test_valid_login_pom(setup_browser):
    driver = setup_browser
    driver.get("https://www.saucedemo.com/")
    
    # Initialize the Page Object
    login = LoginPage(driver)
    
    # Use the Page Object methods
    print("🧪 Executing Login via POM...")
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    
    # Verification
    assert "inventory.html" in driver.current_url
    print("✅ POM Login Successful!")