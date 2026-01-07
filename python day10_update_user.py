import requests
import json

def update_user():
    # Notice the URL: We must specify WHICH user to update (/2)
    # Unlike POST, where we just sent to /users
    user_id = 2
    url = f"https://reqres.in/api/users/{user_id}"
    
    # The New Data (We are changing the job)
    updated_payload = {
        "name": "Manjhi",
        "job": "Senior SDET Product Company"
    }
    
    print(f"🚀 Sending PUT Request to update User {user_id}...")
    
    # Sending the PUT request
    response = requests.put(url, json=updated_payload)
    
    # Validation
    status_code = response.status_code
    print(f"📡 Status Code: {status_code}")
    
    # PUT requests usually return 200 OK (Success)
    assert status_code == 200, f"❌ Failed! Expected 200 but got {status_code}"
    
    # Parse the response
    data = response.json()
    print("\n✅ Server Response:")
    print(json.dumps(data, indent=4))
    
    # Verification
    # The server should tell us WHEN it was updated ('updatedAt')
    assert data['job'] == "Senior SDET Product Company", "❌ Job was not updated!"
    print(f"\n🎉 Success! User promoted to: {data['job']}")
    print(f"🕒 Time of Update: {data['updatedAt']}")

if __name__ == "__main__":
    update_user()
    