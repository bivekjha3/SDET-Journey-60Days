import requests

def delete_user():
    user_id = 2
    url = f"https://reqres.in/api/users/{user_id}"
    
    print(f"🔥 Sending DELETE Request for User {user_id}...")
    
    # Sending the DELETE request
    response = requests.delete(url)
    
    # Validation
    status_code = response.status_code
    print(f"📡 Status Code: {status_code}")
    
    # CRITICAL SDET KNOWLEDGE:
    # 204 means "No Content" (Success, but nothing to show).
    # Some APIs return 200, but standard REST is 204.
    assert status_code == 204, f"❌ Failed! Expected 204 but got {status_code}"
    
    print("✅ Success! User deleted. Server sent 204 No Content.")
    print("🗑️ Cleanup complete.")

if __name__ == "__main__":
    delete_user()