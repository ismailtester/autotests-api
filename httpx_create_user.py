import httpx
from tools.fakers import get_random_email

base_url = 'http://localhost:8000/api/v1/'
user_endpoint = 'users'


payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post(base_url+user_endpoint, json=payload)
print(create_user_response.json())
print(create_user_response.status_code)