from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class CreateFileRequestDict(TypedDict):
    filename: str
    directory: str
    upload_file: str


class FilesClient(APIClient):


    def get_file_api(self, file_id: str) -> Response:
        """
        Метод выполняет GET-запрос к эндпоинту /api/v1/files  для получении данных файле по его file id.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")


    def create_file_api(self, file_id: str, request: CreateFileRequestDict) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"/api/v1/files/{file_id}",
                         data=request,
                         files={"upload_file": open(request["upload_file"], "rb")}
                         )





    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод выполняет GET-запрос к эндпоинту /api/v1/files  для удаления файла по его file id.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")
