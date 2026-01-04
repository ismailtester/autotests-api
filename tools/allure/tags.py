from enum import Enum

#Если передавать enum как Tags.TAG он и передается как Tags.TAG
#Если передать enum как Tags.TAG.value тогда нам отдас строку ключ этого енама
#Что бы получить список всех значений енама, нужно сделать print(list(Tags))
#Так же через енамы есть возможность работать с методами как у строк (или у того что ты закинешь вместе с енамом
#(Enum, str)
#Например сделать TAG = "SMOKE-{name}" и при вызове енама сделать .format("то что нужно")
#Для статусов, тегов, статусной модели, настроек, типов браузеров и т.д.


class AllureTag(str, Enum):
    USERS = "USERS"
    FILES = "FILES"
    COURSES = "COURSES"
    EXERCISES = "EXERCISES"
    REGRESSION = "REGRESSION"
    AUTHENTICATION = "AUTHENTICATION"

    GET_ENTITY = "GET_ENTITY"
    GET_ENTITIES = "GET_ENTITIES"
    CREATE_ENTITY = "CREATE_ENTITY"
    UPDATE_ENTITY = "UPDATE_ENTITY"
    DELETE_ENTITY = "DELETE_ENTITY"
    VALIDATE_ENTITY = "VALIDATE_ENTITY"