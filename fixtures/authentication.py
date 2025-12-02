import pytest
from clients.authentication.authentication_client import get_authentification_client, AuthenticationClient



@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentification_client()