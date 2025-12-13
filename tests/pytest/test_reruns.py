import random
import pytest



@pytest.mark.flaky(reruns=3, reruns_delay=2)
#Для использования плагина pip install pytest-rerunfailures нужно юзать @pytest.mark.flaky
#reruns=3 указывает сколько раз тест будет перезапущен после падения
#ВАЖНО!!! в reruns указывается число реранов, а не того сколько раз будет выполнить тест
#Если ты указал 3 рерана. То например если тест невыполнился один раз, он будет запущен еще 3 раза. Всего будет 4 запуска
#reruns_delay=3 отвечает за ожидание между перезапусками тестов в секундах
def test_reruns():
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_reruns_1(self):
        assert random.choice([True, False])

    def test_reruns_2(self):
        assert random.choice([True, False])


PLATFORM = "Linux" #Константа
#Тест который реранится при определенном условии задается с помощью параметра condition=
#Например тут тест будет реранится только если константа равно Windows. То есть этот тест не будет реранится
@pytest.mark.flaky(reruns=3, reruns_delay=2, condition= PLATFORM == "Windows")
def test_rerun_with_condition():
    assert random.choice([True, False])