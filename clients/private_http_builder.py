from httpx import Client
from pydantic import BaseModel, ConfigDict
from clients.authentication.authentication_client import get_authentification_client
from clients.authentication.authentication_schema import LoginRequestSchema
from cachetools import TTLCache, cached
from datetime import timedelta

#ТУТ НУЖЕН РЕФАКТОРИНГ


class AuthenticationUserSchema(BaseModel):  # Структура данных пользователя для авторизации
    model_config = ConfigDict(frozen=True)
    email: str
    password: str

cache = TTLCache(maxsize=128, ttl=timedelta(minutes=30).total_seconds())


@cached(cache)
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создает экземпляр httpx.Client с аутентификацией пользователя.
    :param user: Объект AuthenticationUserSchema с email и паролем пользователя
    :return: Готовый к использованию объект httpx.Client c установленным заголовком Authorization.
    """

    authentication_client = get_authentification_client()
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )
