import pytest

"""
Флаг -m позволяет запускать тесты по определенным маркерам, например запустить только тесты с маркировкой smoke
python -m pytest -s -v -m "smoke"  запустятся только тесты с маркировкой smoke 


Оператор OR
Так же можно запускать одновременно тесты нескольких маркировок с помощью оператора OR
python -m pytest -s -v -m "smoke or regression"

Оператор AND
Позволяет запустить те тесты которые содержат и одну маркировку и вторую одновременно. Например одновременно имеют маркировки smoke и regression
python -m pytest -s -v -m "smoke and regression"


Оператор NOT
Позволяет НЕ запускать определенные тесты. Нарпимер не запустить smoke тесты и запустить все остальные:
python -m pytest -s -v -m "not smoke"



"""
#
# #Данные маркировки незарезервированные, мы можем написать там что угодно, хоть sadsadasdsad
# @pytest.mark.smoke
# def test_smoke_case():
#     assert 1 + 1 == 2
#
# @pytest.mark.regression
# def test_regression_case():
#     assert 2 * 2 == 4
#
# @pytest.mark.fast
# def test_fast():
#     ...
#
# @pytest.mark.slow
# def test_slow():
#     ...
#
#
# #При запуске данной маркировки, будут запущенные все тесты этого класа
# @pytest.mark.smoke
# class TestSuite:
#
#     def test_case1(self):
#         ...
#
#     def test_case2(self):
#         ...

# @pytest.mark.regression
# class TestUserAuthetication:
#     @pytest.mark.smoke
#     def test_login(self):
#         ...
#
#     @pytest.mark.slow
#     def test_password(self):
#         ...
#
#     def test_logout(self):
#         ...
#

# @pytest.mark.regression
# @pytest.mark.smoke
# @pytest.mark.critical
# def test_critical_login():
#     ...

# @pytest.mark.api
# class TestUserInterface:
#     @pytest.mark.smoke
#     @pytest.mark.critical
#     def test_login_critical(self):
#         ...
#
#     @pytest.mark.regression
#     def test_forgot_password(self):
#         ...
#
#     @pytest.mark.smoke
#     def test_signup(self):
#         ...

# @pytest.mark.slow
# def test_heavy_calculation():
#     pass
#
# @pytest.mark.integration
# def test_integration_with_external_api():
#     pass
#
# @pytest.mark.smoke
# def test_quick_check():
#     pass