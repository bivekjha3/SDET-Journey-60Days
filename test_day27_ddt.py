import pytest
from pages.login_page import LoginPage

# 1. The Data List (Username, Password, Expected outcome)
test_data = [
    ("standard_user", "secret_sauce", "pass"),
    ("locked_out_user", "secret_sauce", "fail"),
    ("problem_user", "secret_sauce", "pass"),
    ("invalid_user", "wrong_password", "fail")
]

# 2. Use the @pytest.mark.parametrize decorator
@pytest.mark.parametrize("user, pwd, expected", test_data)
def test_login_scenarios(setup_browser, user, pwd, expected):
    driver = setup_browser
    driver.get("https://www.saucedemo.com/")
    
    login = LoginPage(driver)
    
    print(f"🧪 Testing with User: {user}")
    login.enter_username(user)
    login.enter_password(pwd)
    login.click_login()
    
    # 3. Logic to handle different expectations
    if expected == "pass":
        # Check if we landed on the inventory page
        assert "inventory.html" in driver.current_url
        print(f"✅ {user} logged in as expected.")
    else:
        # Check if an error message appeared
        error_exists = driver.find_element("css selector", "h3[data-test='error']").is_displayed()
        assert error_exists
        print(f"✅ {user} failed to login as expected.")