import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait # The Watchman
from selenium.webdriver.support import expected_conditions as EC # The Conditions
from webdriver_manager.chrome import ChromeDriverManager

def test_explicit_wait():
    service_obj = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    
    print("🚀 Opening Dynamic Loading Page...")
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    
    # 1. Click the Start Button
    # It exists immediately, so no need to wait long
    driver.find_element(By.XPATH, "//div[@id='start']/button").click()
    print("🖱️ Clicked Start. Waiting for loading to finish...")
    
    # --- THE CRITICAL PART ---
    # The text "Hello World!" is HIDDEN. It takes 5 seconds to show up.
    # If we do driver.find_element... right now, it will crash.
    
    try:
        # Define the Wait (Max 10 seconds)
        wait = WebDriverWait(driver, 10)
        
        # Wait until the element with ID 'finish' is VISIBLE
        # This checks every 500ms. If it appears in 2s, it proceeds immediately.
        finish_element = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
        
        print(f"✅ Text Appeared: {finish_element.text}")
        assert finish_element.text == "Hello World!", "Text mismatch!"
        
    except Exception as e:
        print(f"❌ Test Failed: Element never appeared! {e}")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_explicit_wait()