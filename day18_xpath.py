import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_xpath_login():
    # 1. Setup
    service_obj = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    
    print("🚀 Opening The Internet HerokuApp...")
    driver.get("https://the-internet.herokuapp.com/login")
    
    # 2. XPATH STRATEGY
    # Formula: //tag[@attribute='value']
    
    # Username: We use the 'name' attribute
    # <input type="text" name="username" ...>
    print("✍️ Typing Username using XPath...")
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("tomsmith")
    
    # Password: We use the 'name' attribute again
    # <input type="password" name="password" ...>
    print("✍️ Typing Password using XPath...")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("SuperSecretPassword!")
    
    # Login Button: It uses a slightly advanced trick (Contains Class)
    # <button class="radius" type="submit">
    print("🖱️ Clicking Login using XPath...")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    # 3. Verification using XPath Text Match
    # We look for the green success message
    time.sleep(2)
    try:
        # This checks if there is a 'div' containing the text "You logged into"
        success_msg = driver.find_element(By.XPATH, "//div[contains(text(), 'You logged into')]").text
        print(f"✅ Success Message Found: {success_msg}")
        
    except Exception as e:
        print(f"❌ Login Failed! Error: {e}")

    # 4. Cleanup
    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    test_xpath_login()