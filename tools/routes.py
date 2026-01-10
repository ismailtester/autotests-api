from enum import Enum

class APIRoutes(str, Enum):
    USERS = "/api/v1/users"
    FILES = "/api/v1/files"
    COURSES = "/api/v1/courses"
    EXERCISES = "/api/v1/exercises"
    AUTHENTICATION = "/api/v1/authentication"

    #Данным кодом мы переопределяем метод самого класса енум __str__ который при обычном использование при вызывое
    #APIRoutes.USERS нам бы выдавал APIRoutes.USERS, а теперь после переопределения выдаст /api/v1/users
    #Это удобнее чем вызывать APIRoutes.USERS.value
    def __str__(self):
        return self.value
