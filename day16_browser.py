import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def start_browser():
    print("🚀 Initializing the Browser...")

    # 1. Setup the Chrome Driver (The Translator)
    # This automatically downloads the correct driver for your laptop
    service_obj = Service(ChromeDriverManager().install())
    
    # 2. Launch Chrome
    driver = webdriver.Chrome(service=service_obj)
    
    # 3. Maximize the Window (So we can see everything)
    driver.maximize_window()
    
    # 4. Navigate to a Website
    print("🌐 Going to Google...")
    driver.get("https://www.google.com")
    
    # 5. Check the Title (Verification)
    title = driver.title
    print(f"✅ Page Title is: {title}")
    
    if "Google" in title:
        print("🎉 Test Passed: We are on Google!")
    else:
        print("❌ Test Failed: Where are we?")

    # 6. Wait for 5 seconds (So you can see it with your eyes)
    time.sleep(5)
    
    # 7. Close the Browser (Cleanup)
    print("🚪 Closing Browser...")
    driver.quit()

if __name__ == "__main__":
    start_browser()