import pytest

"""
scope фикстуры по умолчанию function 

function - значит что фикстура выполняется на каждый тест (функцию)

"""


@pytest.fixture
def users_client():
    ...


class TestUserFlow:
    def test_user_and_login(self, users_client):
        ...

    def test_user_can_create_course(self, users_client):
        ...

class TestAccountFlow:
    def test_user_account(self, users_client):
        ...

