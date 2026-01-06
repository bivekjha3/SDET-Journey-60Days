import requests
import json

def create_new_user():
    url = "https://reqres.in/api/users"
    
    # 1. The Payload (Data we are sending TO the server)
    # This acts like the Python Dictionary you learned on Day 2
    my_payload = {
        "name": "Manjhi",
        "job": "Mountain Breaker"
    }
    
    print(f"🚀 Sending POST Request to: {url}")
    print(f"📦 With Payload: {my_payload}")
    
    # 2. Sending the POST Request
    # Notice: We pass 'json=my_payload' so Python converts Dict to JSON automatically
    response = requests.post(url, json=my_payload)
    
    # 3. Validation
    status_code = response.status_code
    print(f"📡 Status Code: {status_code}")
    
    # CRITICAL SDET CHECK:
    # POST requests usually return 201 (Created), not 200.
    assert status_code == 201, f"❌ Failed! Expected 201 but got {status_code}"
    
    # 4. Verify the Response
    # The server should send back the ID of the new user and a timestamp
    data = response.json()
    print("\n✅ Server Response:")
    print(json.dumps(data, indent=4))
    
    # Check if the name matches what we sent
    assert data['name'] == "Manjhi", "❌ Name mismatch in response!"
    assert data['job'] == "Mountain Breaker", "❌ Job mismatch in response!"
    
    print("\n🎉 Success: User 'Manjhi' created with ID: " + data['id'])

if __name__ == "__main__":
    create_new_user()