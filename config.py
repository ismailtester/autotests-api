from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, HttpUrl, FilePath, DirectoryPath
from typing import Self


#Вложенные модели настроек наследуются от BaseModel а не BaseSettings
class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        return str(self.url)

class TestDataConfig(BaseModel):
    image_png_file: FilePath


#Модель настроек наследуется от BaseSettings
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="allow", #Настройка нужна для CI - так как будет дополнительный файл .env самого сервера в папке с проектом
        env_file=".env", #Название файла откуда берем переменные окружения
        env_file_encoding="utf-8", #Кодировку файла с переменными окружения
        env_nested_delimiter="." #Данный разделитель нужен для правильного создания модели с вложенными моделями пример ниже
    )
    test_data: TestDataConfig
    http_client: HTTPClientConfig
    allure_results_dir: DirectoryPath  # Добавили новое поле

    # Добавили метод initialize
    @classmethod
    def initialize(cls) -> Self:  # Возвращает экземпляр класса Settings
        allure_results_dir = DirectoryPath("./allure-results")  # Создаем объект пути к папке
        allure_results_dir.mkdir(exist_ok=True)  # Создаем папку allure-results, если она не существует

        # Передаем allure_results_dir в инициализацию настроек
        return Settings(allure_results_dir=allure_results_dir)


# Теперь вызываем метод initialize
settings = Settings.initialize()

"""
HTTP_CLIENT.URL = "URL"
HTTP_CLIENT.TIMEOUT = 100 
Благодаря env_nested_delimiter со значением точка, у нас будет правильно создана модель и пайдентик распознает что:

url: HTTP_CLIENT.URL
timeout: HTTP_CLIENT.TIMEOUT
"""
