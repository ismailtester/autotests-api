import time
from faker import Faker

def get_random_email() -> str:
    return f"test.{time.time()}@example.com"


