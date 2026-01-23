import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select # The Specialist
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_forms():
    service_obj = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    
    print("🚀 Opening Practice Page...")
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    
    # --- PART 1: STATIC DROPDOWN (<select> tag) ---
    print("\n🔽 Handling Dropdown...")
    
    # 1. Find the dropdown element first
    dropdown_element = driver.find_element(By.ID, "dropdown-class-example")
    
    # 2. Wrap it inside the Select class
    sel = Select(dropdown_element)
    
    # 3. Choose an option (3 Ways to do it)
    # sel.select_by_index(1)        # 2nd item (Index starts at 0)
    # sel.select_by_value("option2") # value="option2" in HTML
    sel.select_by_visible_text("Option2") # The text user sees
    
    print("✅ Selected: Option2")
    
    # --- PART 2: CHECKBOXES ---
    print("\n☑️ Handling Checkbox...")
    
    # 1. Find the checkbox (Option 1)
    checkbox = driver.find_element(By.ID, "checkBoxOption1")
    
    # 2. Check if it is already selected?
    is_checked = checkbox.is_selected()
    print(f"🧐 Is Checkbox selected initially? {is_checked}")
    
    if not is_checked:
        checkbox.click() # Click to check it
        print("🖱️ Clicked Checkbox!")
    
    # 3. Verify
    assert checkbox.is_selected() == True, "❌ Checkbox failed to select!"
    print("🎉 Verification Passed: Checkbox is ON.")

    time.sleep(3) # Just to see the result
    driver.quit()

if __name__ == "__main__":
    test_forms()