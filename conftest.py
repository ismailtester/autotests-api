
"""
Подключение фикстур как плагинов.
В корневом conftest файле указываем списком как ниже, путь до папок с плагинами.

Теперь фикстуры из этих плагинов будут доступны по всему проекту.

"""
pytest_plugins = [
    "fixtures.users",
    "fixtures.authentication",
    "fixtures.courses",
    "fixtures.files",
    "fixtures.exercises",

    "fixtures.allure"
]