import pytest


from clients.authentication.authentication_client import get_authentification_client, AuthenticationClient
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from pydantic import BaseModel, EmailStr

"""
Фикстуры обычно создаются в файле conftest и тогда они будут доступны во всех файлах с той же директории что этот файл и ниже
pytest автоматически обнаруживает файлы conftest и загружает из них фикстуры 
"""

class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema
    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def authentication_user(self):
        return AuthenticationUserSchema(email=self.request.email, password=self.request.password)

@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentification_client()


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()


@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    """
    Название фикстуры скоуп + название функции сделанно на будущее, если потенциально понадобится использовать фикстуру на каждый тестовый класс или другой скоуп.
    Это правила для всех будущих фикстур
    """
    request = CreateUserRequestSchema() #Создание юзер схемы для будущего запроса
    response = public_users_client.create_user(request) #Ответ на запрос
    return UserFixture(request=request, response=response)

@pytest.fixture
def private_users_client(function_user) -> PrivateUsersClient:
    return get_private_users_client(function_user.authentication_user)
