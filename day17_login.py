import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # IMPORT THIS! (Critical)
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_swag_labs_login():
    # 1. Setup
    service_obj = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    
    print("🚀 Opening Swag Labs...")
    driver.get("https://www.saucedemo.com/")
    
    # 2. LOCATORS STRATEGY
    # We use 'By.ID' because it is unique and fast.
    
    # Find Username box and Type
    # <input id="user-name" ... >
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    
    # Find Password box and Type
    # <input id="password" ... >
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    # Find Login Button and Click
    # <input id="login-button" ... >
    print("🖱️ Clicking Login...")
    driver.find_element(By.ID, "login-button").click()
    
    # 3. Verification
    # After login, we should see the text "Products"
    # Here we use By.CLASS_NAME just to learn a new one
    time.sleep(2) # Wait for page to load
    
    try:
        page_title = driver.find_element(By.CLASS_NAME, "title").text
        print(f"✅ Page Text Found: {page_title}")
        
        if page_title == "Products":
            print("🎉 Login Successful!")
        else:
            print("❌ Login Failed.")
            
    except Exception as e:
        print(f"❌ Error: Could not find 'Products' title. Login failed? {e}")

    # 4. Cleanup
    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    test_swag_labs_login()