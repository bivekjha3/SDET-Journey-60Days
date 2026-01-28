import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    # This allows you to pass --browser_mode=headless in the terminal
    parser.addoption("--browser_mode", action="store", default="headed")

@pytest.fixture(scope="function")
def setup_browser(request):
    browser_mode = request.config.getoption("--browser_mode")
    
    chrome_options = Options()
    
    if browser_mode == "headless":
        print("\n👻 Running in HEADLESS mode (No Window)...")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
    else:
        print("\n🖥️ Running in HEADED mode (Window Visible)...")

    service_obj = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    driver.maximize_window()
    
    yield driver
    driver.quit()