from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, HttpUrl, FilePath


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
        env_file=".env", #Название файла откуда берем переменные окружения
        env_file_encoding="utf-8", #Кодировку файла с переменными окружения
        env_nested_delimiter="." #Данный разделитель нужен для правильного создания модели с вложенными моделями пример ниже
    )
    test_data: TestDataConfig
    http_client: HTTPClientConfig


"""
HTTP_CLIENT.URL = "URL"
HTTP_CLIENT.TIMEOUT = 100 
Благодаря env_nested_delimiter со значением точка, у нас будет правильно создана модель и пайдентик распознает что:

url: HTTP_CLIENT.URL
timeout: HTTP_CLIENT.TIMEOUT
"""

settings = Settings()