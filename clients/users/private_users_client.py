from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class PatchUserRequestDict(TypedDict):
    """
    Описание структуры запроса для частичного обновления данных пользователя.
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class GetUserResponseDict(TypedDict):
    """
    Описание структуры ответа получения пользователя.
    """
    user: User



class PrivateUsersClient(APIClient):

    def get_user_me_api(self) -> Response:
        """
        Метод выполняет GET-запрос к эндпоинту /api/v1/users/me для получении данных о текущем пользователе.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Метод выполняет GET-запрос к эндпоинту /api/v1/users/{user_id} для получения данных о пользователе по его user id.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request:PatchUserRequestDict) -> Response:
        """
        Метод выполняет PATCH-запрос к эндпоинту /api/v1/users/{user_id} для частичного обновления данных пользователя.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод выполняет DELETE-запрос к эндпоинту /api/v1/users/{user_id} для удаления пользователя.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseDict:
        response = self.get_user_api(user_id)
        return response.json()


def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))