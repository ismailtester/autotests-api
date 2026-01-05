import allure



@allure.step("Building api client") #Декоратор юзается для атомарных функций который выполяют одно действие
#Плюс если нужны две вложенные друг в друга тесты, мы не можем этого сделать, два декоратора повешенные не сработают так
def build_api_client():
    with allure.step("Get user authentication token"):
        assert True
    with allure.step("Create new API client"):
        assert False
    with allure.step("Create new good API client"):
        assert True

@allure.step("Creating course with title: '{title}'") #Способ добавить динамический параметр в декоратор степ
#Добавляем в описание декоратора название параметра в кавычка '{название параметра}'
def create_course(title: str):
    ...

@allure.step("Deleting course")
def delete_course():
    ...



def test_feature():

    build_api_client()

    create_course(title="Pytest")
    create_course(title="Python")
    create_course(title="GoLang")

    delete_course()

    # with allure.step("Building API client"):
    #    ...
    # with allure.step("Create course"):
    #     ...
    #
    # with allure.step("Deleting course"):
    #     ...