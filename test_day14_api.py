import pytest
import requests

# CONSTANTS (The URL shouldn't be hardcoded everywhere)
BASE_URL = "https://reqres.in/api"

# Test Case 1: Verify we can get list of users
def test_get_users_list():
    print("\n🚀 Testing GET /users ...")
    
    response = requests.get(f"{BASE_URL}/users?page=2")
    
    # 1. Check Status Code
    assert response.status_code == 200, "❌ API is down! Status not 200"
    
    # 2. Check Data
    data = response.json()
    total_pages = data['total_pages']
    assert total_pages > 0, "❌ No pages found in response"
    
    # 3. Check Performance (Bonus Senior Check)
    # Fail if api takes more than 1 second (1000ms)
    time_taken = response.elapsed.total_seconds()
    assert time_taken < 2.0, f"❌ API is too slow! Took {time_taken}s"

# Test Case 2: Verify creating a user works
def test_create_user():
    print("\n🚀 Testing POST /users ...")
    
    payload = {
        "name": "Manjhi",
        "job": "Automation Hero"
    }
    
    response = requests.post(f"{BASE_URL}/users", json=payload)
    
    # 1. Check Status Code (POST should be 201)
    assert response.status_code == 201, f"❌ Expected 201 but got {response.status_code}"
    
    # 2. Verify Body
    data = response.json()
    assert data['name'] == "Manjhi", "❌ Name mismatch!"
    assert "id" in data, "❌ ID not generated!"

# Note: We do NOT need 'if __name__ == "__main__"' anymore. 
# Pytest handles execution.