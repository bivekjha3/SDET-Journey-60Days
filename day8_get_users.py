import requests  # This is the "Waiter"
import json

def get_user_list():
    # 1. The URL (The Kitchen Address)
    url = "https://reqres.in/api/users?page=2"
    
    print(f"🚀 Sending GET Request to: {url}")
    
    # 2. Sending the Request (Waiter goes to kitchen)
    response = requests.get(url)
    
    # 3. Validating the Status Code (Did the food arrive?)
    status_code = response.status_code
    print(f"📡 Status Code Received: {status_code}")
    
    # SDET Check: If it's not 200, stop the test!
    assert status_code == 200, f"❌ Failed! Expected 200 but got {status_code}"
    print("✅ Status Check Passed: Server is happy.")

    # 4. Parsing the Data (Reading the Menu)
    # The server sends data as TEXT. We convert it to JSON (Dictionary).
    data = response.json()
    
    # Pretty print the data so we can read it
    print("\n📦 Response Data:")
    # json.dumps makes it look pretty (indent=4)
    print(json.dumps(data, indent=4)) 
    
    # 5. Extracting Specific Data (Senior Level)
    # Let's verify if the first user's email exists
    first_user = data['data'][0]
    email = first_user['email']
    print(f"\n👤 First User Email: {email}")

if __name__ == "__main__":
    get_user_list()