from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    print("★")
    print(response.json())
    print(response.json()['message'])
    print("★★")
    assert response.json() == {"message":"Hello"}
    
def test_read_zipcode():
    response = client.get(f'/zipcode?zipcode=9012303')
    print("test_read_zipcode")
    assert response.status_code == 200
    print(response.json()['results'])
    
    assert response.json()['results'][0]['address1'] == '沖縄県'
    
    #assert response.json() == {"message":"Hello"}