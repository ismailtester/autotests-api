
"""
Команда для запуска всех тестов в проекте
python -m pytest

По дефолту pytest ищет тестовые файлы в любых папках, но принято тесты скалдывать в папку tests

Флаг -s нужен для того что бы в отчете о результатах тестов выводились print()
python -m pytest -s


Флаг -v (verbose) нужен для более подробного вывода результиатов теста, например напротив пройденного теста будет написанно PASSED
python -m pytest -s -v


Флаг -k нужен для селективного запуска по названию класса или функции, например:
python -m pytest -s -v -k "test_first_try" - запустит тест в названии которого есть test_first_try
Если к примеру нам нужно запустить тест в названии которого есть слово second то пишем python -m pytest -s -v -k "second"

Так же флаг -k дает следующие возможности:
Запуск по содержанию нескольких слов, например нужно запустить тесты в названии которых есть два слова first и try
python -m pytest -s -v -k "first and try"

Запуск по содержанию одного из двух слов, например first или one
python -m pytest -s -v -k "first or one"

НЕ запуск по содержанию одного слов, например мы хотим запустить все названии чего есть test, но нет слова two
python -m pytest -s -v -k "test and not two"



"""



class TestUserAuthentication:

    """
    Тестовый класс по умолчанию должен начинаться с Test

    В тестовом классе нельзя использовать конструктор __init__

    """

    def test_first_try(self):
        """
        Тестовая функция по умолчанию должна начинаться с test_
        """
        print("Hello World!")

    def test_second_try(self):
        pass



class TestUserLogin:
    def test_one(self):
        pass

    def test_two(self):
        pass

class TestAssertions:
    def test_assert_positive_case(self):
        assert 2 + 2 == 4

    def test_assert_negative_case(self):
        x = 5
        y = 2
        assert y + y == x, f"2 + 2 is not equals 5"

