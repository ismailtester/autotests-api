import httpx
import random

# response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
#
# print(response.json())
# print(response.status_code)
#
# data = {
#     "userId": 1,
#     "title": "Ismail tester",
#     "body": "testing body",
#     "completed": True
# }
#
# response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)
# print(response.json())
# print(response.status_code)
# print(response.headers)
#
#
# print('_______________________________Формат application/x-www-form-urlencoded________________________________________________')
#
#
# data = {
#     "username": "Ismail tester",
#     "password": "testingbody"
# }
#
# response = httpx.post('https://httpbin.org/post', data=data)
#
# print(response.json())
# print(response.status_code)
# print(response.headers)
#
# print('_______________________________HEADERS________________________________________________')
#
# headers = {'Authorization': 'Bearer my_secret_token'}
# response = httpx.post('https://httpbin.org/post', headers=headers)
# print(response.request.headers)

#
# print('_______________________________query параметры________________________________________________')
#
# rand_num = random.randint(1,10)
# params = {'userId': rand_num}
# response = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)
# print(response.json())
#

#
# print('_______________________________ОТПРАВКА ФАЙЛОВ________________________________________________')
#
# file = {"file": ("example.txt", open("example.txt", "rb"))}
# response = httpx.post('https://postman-echo.com/post', files=file)
#
# print(response.json())


# print('_______________________________РАБОТА С СЕССИЯМИ________________________________________________')

# with httpx.Client() as client:
#     response_1 = client.get('https://jsonplaceholder.typicode.com/todos/1')
#     response_2 = client.get('https://jsonplaceholder.typicode.com/todos/2')
#
# print(response_1.json())
# print(response_2.json())
#
# ######################Добавление хедеров клиенту и добавление хедеров к уже существующим
# client = httpx.Client(headers={'Authorization': 'Bearer my_secret_token'})
# client.headers.update({'X-test': '123'})
# response_1 = client.get('https://httpbin.org/get')
# print(response_1.json())



# print('_______________________________РАБОТА С ОШИБКАМИ________________________________________________')
# try:
#     response = httpx.get('https://jsonplaceholder.typicode.com/invalid-url')
#     print(response.status_code)
#     response.raise_for_status()
# except httpx.HTTPStatusError as error:
#     print(f'Ошибка запроса: {error}')


print('_______________________________ТАЙМАУТЫ________________________________________________')

try:
    response = httpx.get('https://postman-echo.com/delay/5', timeout=2)
except httpx.ReadTimeout as error:
    print(f'Запрос превысил задержку 2 секунды')