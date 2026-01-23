import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_window_switching():
    service_obj = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    
    print("🚀 Opening Main Page...")
    driver.get("https://the-internet.herokuapp.com/windows")
    
    # 1. Click the link that opens a new tab
    driver.find_element(By.LINK_TEXT, "Click Here").click()
    print("🖱️ Clicked Link. New Tab opened.")
    
    # --- CRITICAL PART: SWITCHING ---
    
    # Get all Window IDs (Returns a List)
    # index 0 = Parent (Main Page)
    # index 1 = Child (New Tab)
    windows = driver.window_handles
    parent_id = windows[0]
    child_id = windows[1]
    
    print(f"🆔 Parent ID: {parent_id}")
    print(f"🆔 Child ID: {child_id}")
    
    # Switch to Child Window
    driver.switch_to.window(child_id)
    print("🔀 Switched to Child Tab.")
    
    # Verify we are on the new page
    text = driver.find_element(By.TAG_NAME, "h3").text
    print(f"✅ Text on New Tab: {text}")
    assert text == "New Window", "Wrong Tab!"
    
    # Close ONLY the child tab (Not the whole browser)
    driver.close() 
    print("🚪 Closed Child Tab.")
    
    # Switch back to Parent
    driver.switch_to.window(parent_id)
    print("🔀 Switched back to Parent.")
    
    # Verify we are back
    main_text = driver.find_element(By.TAG_NAME, "h3").text
    print(f"✅ Text on Main Page: {main_text}")
    assert "Opening a new window" in main_text
    
    time.sleep(2)
    driver.quit() # Closes everything

if __name__ == "__main__":
    test_window_switching()