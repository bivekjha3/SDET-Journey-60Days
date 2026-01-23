import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_iframes():
    service_obj = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    
    print("🚀 Opening iFrame Page...")
    driver.get("https://the-internet.herokuapp.com/iframe")
    
    # Verify we are on the page
    print("👀 Looking for header...")
    header = driver.find_element(By.TAG_NAME, "h3").text
    print(f"✅ Header Found: {header}")

    # --- THE TRAP ---