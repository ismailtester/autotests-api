"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}
"""



from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel
import uuid



class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl #Данный класс проверяет дейсвительно ли строка похожа не url

class UserSchema(BaseModel):
    id: str
    email: EmailStr #Данный класс проверяет дейсвительно ли строка похожа не email
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


    @computed_field #По факту это такое же поле как выше, но динамически сформированное (можно что угодно в нем создать). Ему можно задать aliace и при создании объекта (сериализации) на основе модели, оно может туда залетать
    def username(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True) #populate_by_name позволяет коду не падать если создается (сериализуется) модель со снейк кейс полями указанными в само модели например max_score вместо maxScore
    #вариант конфига пойдет, только если поля всегда будут в камел кейсе maxScore, если нет, то лучше не юзать
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")




course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore= 10,
    description="Playwright",
    previewFile= FileSchema(
        id="file-id",
        filename="file.png",
        directory="courses",
        url="http://localhost:8000"
    ),
    estimatedTime="1 hour",
    createdByUser= UserSchema(
        id= "user-id",
        email="user@gmail.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Ellis"

    )
)

print(course_default_model, type(course_default_model))

course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "previewFile": {
        "id": "file-id",
        "filename": "file.png",
        "directory": "courses",
        "url": "http://localhost:8000"
    },
    "description": "Playwright",
    "estimatedTime": "1 hour",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Ellis"
    }
}

course_dict_model = CourseSchema(**course_dict) #Делаем из словаря нашу модель

print("course dict:", course_dict_model)


course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "previewFile": {
        "id": "file-id",
        "filename": "file.png",
        "directory": "courses",
        "url": "http://localhost:8000"
    },
    "description": "Playwright",
    "estimatedTime": "1 hour",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Ellis"
    }
}
"""

course_json_model = CourseSchema.model_validate_json(course_json)  #Делаем из json строки модель
print("Course JSON model:", course_json_model)

#КОГДА МЫ ИЗ JSON строки получаем модель, это десериализация
#Если мы из модели получаем json строку, мы значит её сереализуем модель


print("Делам из модели словарь: ", course_json_model.model_dump()) #Делам из модели словарь
print("Делаем из модели json: ", course_json_model.model_dump_json()) #Делам из модели json
print("Делаем из модели json: ", course_json_model.model_dump_json(by_alias=True)) #Что бы десериализовать модель в json или словарь с алиасами

# course = CourseSchema()
# print("Модель с дефолтными полями: ",course)


user = UserSchema(
    id = "user-id",
    email = "user@gmail.com",
    lastName = "Bond",
    firstName = "Zara",
    middleName = "Ellis"
)

print(user.get_username(), user.username)

try:
    file_with_error = FileSchema(
        id="file-id",
        filename="file.png",
        directory="courses",
        url="t:8000"
    )
except ValidationError as error:
    print(error)
    print(error.errors())