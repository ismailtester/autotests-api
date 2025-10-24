from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient

class PatchUserRequestDict(TypedDict):
    """
    Описание структуры запроса для частичного обновления данных пользователя.
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None





class PrivateUsersClient(APIClient):

    def get_get_user_me_api(self) -> Response:
        """
        Метод выполняет GET-запрос к эндпоинту /api/v1/users/me для получении данных о текущем пользователе.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/users/me")

    def get_get_user_api(self, user_id: str) -> Response:
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