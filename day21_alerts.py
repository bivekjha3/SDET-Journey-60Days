import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_alerts():
    service_obj = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    
    print("🚀 Opening Practice Page...")
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    
    name = "Manjhi"
    
    # --- SCENARIO 1: Simple Alert (Just OK) ---
    print("\n⚠️  Testing Simple Alert...")
    driver.find_element(By.ID, "name").send_keys(name)
    driver.find_element(By.ID, "alertbtn").click()
    
    # 1. Switch to Alert Mode
    alert = driver.switch_to.alert
    
    # 2. Grab the Text
    alert_text = alert.text
    print(f"📜 Alert Text: {alert_text}")
    
    assert name in alert_text, "❌ Name not found in alert!"
    
    # 3. Click OK (Accept)
    alert.accept()
    print("✅ Accepted Alert.")
    
    
    # --- SCENARIO 2: Confirm Alert (OK or Cancel) ---
    print("\n⚠️  Testing Confirm Alert...")
    driver.find_element(By.ID, "name").send_keys(name)
    driver.find_element(By.ID, "confirmbtn").click()
    
    # Switch again
    confirm_alert = driver.switch_to.alert
    print(f"📜 Confirm Text: {confirm_alert.text}")
    
    # 4. Click Cancel (Dismiss)
    confirm_alert.dismiss()
    print("✅ Dismissed (Clicked Cancel).")

    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    test_alerts()