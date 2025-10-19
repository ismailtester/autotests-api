import httpx


from tools.fakers import get_random_email

base_url = 'http://localhost:8000/api/v1/'
user_endpoint = 'users'
login_endpoint = 'authentication/login'


# Создаем пользователя
create_user_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post(base_url+user_endpoint, json=create_user_payload)
create_user_response_data = create_user_response.json()


print(create_user_response_data)
print(create_user_response.status_code)

# Проходим аутентификацию
login_payload = {
      "email": create_user_payload['email'],
      "password": create_user_payload['password']
    }

login_response = httpx.post(base_url+login_endpoint, json=login_payload)
login_response_data = login_response.json()
print(f"Login response data: {login_response_data}")

#Находим пользователя по айди
user_id = f"/{create_user_response_data['user']['id']}"
get_user_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"} #Формируем хедеры с access токеном
get_user_response = httpx.get(base_url+user_endpoint+user_id, headers=get_user_headers)
get_user_response_data = get_user_response.json()
print(f"Get user data:{get_user_response_data}")