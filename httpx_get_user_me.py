import httpx

with httpx.Client() as client:  # Привыкаю юзать клиента на будущее

    login_payload = {
      "email": "user11@example.com",
      "password": "123321"
    }
    login_response = client.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
    access_token = login_response.json()['token']['accessToken']

    client.headers.update({"Authorization": f"Bearer {access_token}"}) #Обновляю хедер клиента
    response_users_me = client.get('http://localhost:8000/api/v1/users/me')
    print(f"""USER INFO 
{response_users_me.json()}""")

    print(f"Response status code: {response_users_me.status_code}")
