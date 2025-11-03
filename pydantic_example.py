from pydantic import BaseModel, Field


# В Pydantic типизация по умолчанию не строгая —
# если указано id: int, и передать id="12",
# то значение автоматически приведётся к числу 12.
# Для строгой проверки без автоприведения типов
# нужно использовать StrictInt, StrictStr, StrictBool и т.д.

class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    # address: Address
    is_active: bool = Field(alias="isActive")


user_data = {
    'id': 1,
    'name': 'Alice',
    'email': 'alice@example.com',
    'isActive': True
}

user = User(**user_data)
print(user.model_dump())
print(user.model_dump_json(by_alias=True))

# user = User(id=1,
#             name="Alice",
#             email="alice@mail.ru",
#             is_active=False,
#             #address={"city": "Moscow", "zip_code":"111111"} Первый способ
#             address=Address(city="Moscow", zip_code="2213123")
#             )
# # print(user)
# print(user.model_dump()) #Преобразование из модели в словарь
# print(user.model_dump_json()) #Преобразование из модели в json


