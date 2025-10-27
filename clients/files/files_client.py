from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.private_http_builder import get_private_http_client, AuthenticationUserDict

class File(TypedDict):
    """
    Описание структуры файла.
    """
    id: str
    filename: str
    directory:str
    url:str

class CreateFileResponseDict(TypedDict):
    """
    Описание структуры ответа создания файла.
    """
    file: File

class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла.
    """
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


    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"/api/v1/files",
                         data=request,
                         files={"upload_file": open(request["upload_file"], "rb")}
                         )




    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод выполняет GET-запрос к эндпоинту /api/v1/files  для удаления файла по его file id.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")


    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponseDict:
        response = self.create_file_api(request)
        return response.json()



def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))
