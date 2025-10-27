from httpx import Response
from clients.api_client import APIClient
from typing import TypedDict

from clients.private_http_builder import AutheticationUserDict, get_private_http_client


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений определенного курса.
    """
    courseId: str

class CreateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса для создания упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int | None
    description: str
    estimatedTime: str




class UpdateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления информации об упражнении.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None



class ExercisesClient(APIClient):
    """
    Клиент для работы с методами упражнений
    """


    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения по exercise_id.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Метод выполняет POST-запрос к эндпоинту /api/v1/exercises для создания нового упражнения.

        :param request: Словарь с полями: title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
        """
        Метод выполняет PATCH-запрос к эндпоинту /api/v1/exercises/{exercise_id} для обновления информации об упражнении.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с полями: title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод выполняет DELETE-запрос к эндпоинту /api/v1/exercises/{exercise_id} для удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

def get_exercises_client(user: AutheticationUserDict) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))
