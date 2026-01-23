import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# The @pytest.fixture decorator makes this available to all tests
# scope="function" means "Run this for EVERY test case"
@pytest.fixture(scope="function")
def setup_browser():
    print("\n🚀 -- SETUP: Opening Browser --")
    
    # 1. Initialize Driver
    service_obj = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    
    # 2. Yield (Give the driver to the test)
    # The code pauses here while the test runs
    yield driver
    
    # 3. Teardown (Run this AFTER the test finishes)
    print("\n🚪 -- TEARDOWN: Closing Browser --")
    driver.quit()