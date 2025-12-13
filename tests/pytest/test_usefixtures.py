import pytest

"""
декоратор pytest.mark.usefixtures - позволяет нам использовать фикстуры без необходимости их явной передачи в аргументы тестового метода
ВАЖНО!!!!
Эта фикстура не работает в передачей данных в сами тесты, без явного указания в аргументах самого теста. 
То есть ей лучше использовать, для предварительных каких-то действий, очистка базы данных и т.п. (того что ничего не должно возвращать в тест)

ПОЧЕМУ НЕ ИСПОЛЬЗОВАТЬ autouse = True
Потому что при автоюзе, фикстура будет использоваться на все тесты которые находятся в файле, на все тестовые классы, а если нам этого не нужно?
pytest.mark.usefixtures может применятся по всем тестам определенного класса
"""

@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Удаляем все данные из базы данных")

@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Создаем новые данные к базе данных")

@pytest.mark.usefixtures('clear_books_database', 'fill_books_database')
class TestLibrary:
    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...
