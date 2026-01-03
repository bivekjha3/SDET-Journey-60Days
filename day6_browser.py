# 1. PARENT CLASS (Generic)
class GenericBrowser:
    def open_website(self):
        print("🌐 Opening website...")

    # The Standard Click
    def click_button(self):
        print("🖱️ Clicked the button.")

# 2. CHILD CLASS (Specific - Chrome)
class ChromeBrowser(GenericBrowser):
    # We don't change 'open_website', so it uses the Parent's version.
    
    # BUT, we want to change how 'click' works.
    # This is METHOD OVERRIDING.
    def click_button(self):
        print("🔥 [Chrome Special] Highlighting button in RED color...")
        print("🖱️ Clicked the button nicely.")

# 3. CHILD CLASS (Specific - Firefox)
class FirefoxBrowser(GenericBrowser):
    def click_button(self):
        print("🦊 [Firefox Special] Checking security before clicking...")
        print("🖱️ Clicked the button securely.")

# --- Main Execution ---
if __name__ == "__main__":
    print("--- 1. Using Generic Browser ---")
    b1 = GenericBrowser()
    b1.click_button() 
    # Output: Simple click

    print("\n--- 2. Using Chrome (The Override) ---")
    b2 = ChromeBrowser()
    b2.click_button() 
    # Output: Highlight + Click (Modified!)

    print("\n--- 3. Using Firefox (The Override) ---")
    b3 = FirefoxBrowser()
    b3.click_button() 
    # Output: Security + Click (Modified!)