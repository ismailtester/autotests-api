import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int):
    """
    Название аргумента в параметризации и в принимающем тесте должны совпадать. Если в параметризации указано numbers то и в тест функции numbers
    """
    assert number > 0

@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
@pytest.mark.parametrize("host", ["http://dev.com/", "http://dev.com/", "http://prod.com/"])
def test_miltiplication_of_numbers(os: str, host: str):
    """
    Тест будет запущен 12 раз из-за того что каждый параметр os, будет запущен с каждым параметром host
    """
    ...

#Параметризация фикстуры
#Производится без участия parametrize в фикстуре указываетсч params в которую передается список с параметрами
@pytest.fixture(params=[
    "http://dev.com/",
    "http://dev.com/",
    "http://prod.com/"
])
#Что бы params работал с params нужно использовать SubRequest и импортировать его  from _pytest.fixtures import SubRequest
def host(request: SubRequest) -> str:
     return request.param

def test_host(host: str):
    print(f"Running test on host {host}")


@pytest.mark.parametrize("user", ["Alice", "Sady"])
class TestOperations:
    """
    Паметризация тестового класса.
    Нужно указать параметризацию над тестовым классом.
    Нужн оуказать параметр в каждой тест функции
    """
    def test_user_with_operation(self, user: str):
        print(f"Test with operation {user}")

    def test_user_without_operation(self, user: str):
        print(f"Test without operation {user}")




@pytest.mark.parametrize("phone_number",
                         ["+70000111", "+70000112", "+70000113"],
                         ids=[
                             "User with money on account",
                             "User without money on account",
                             "User with operation on account"
                         ]
                         )
def test_identifiers(phone_number: str):
    """
    Для более понятной отчетности параметризации используется параметр ids
    Он принимает список названий которые будут у каждого параметра в parametrize
    Результаты тестов будут такими
    tests/test_parametrization.py::test_identifiers[User with money on account] PASSED
    tests/test_parametrization.py::test_identifiers[User without money on account] PASSED
    tests/test_parametrization.py::test_identifiers[User with operation on account] PASSED

    КОЛИЧЕСТВО идентификаторов должно равнятся количеству параметров

    """
    ...


users = {
    "+700001": "User with money on account",
    "+700002": "User without money on account",
    "+700003": "User with operation on account",
}



@pytest.mark.parametrize("phone_number",
                         users.keys(),
                         ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
                         )
def test_identifiers_with_ids(phone_number: str):
    """
    Тут мы делаем динамически создаваемый id
    ВААЖНО!!!
    Его НЕ обязательно делать через лямбду. Можно сделать функцию внешне и затем запихнуть её после ids
    Тут сделано для краткости

    """
    ...
