import requests
import json

def login_and_get_token():
    url = "https://reqres.in/api/login"
    
    # 1. The Credentials (Must be correct!)
    # In a real company, you hide these in a config file, not hardcode them.
    creds = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    
    print(f"🔐 Attempting Login with: {creds['email']}...")
    
    # 2. Send POST Request (Login is always POST)
    response = requests.post(url, json=creds)
    
    # 3. Validate Response
    status_code = response.status_code
    print(f"📡 Status Code: {status_code}")
    
    assert status_code == 200, f"❌ Login Failed! Status: {status_code}"
    
    # 4. Extract the Token (The "VIP Stamp")
    data = response.json()
    token = data.get("token")
    
    if token:
        print(f"🎉 Login Successful!")
        print(f"🔑 Your Access Token: {token}")
        print("⚠️  Save this token! You need it for future requests.")
    else:
        print("❌ Error: Token not found in response!")

if __name__ == "__main__":
    login_and_get_token()