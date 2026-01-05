import allure

from clients.courses.courses_schema import UpdateCourseResponseSchema, UpdateCourseRequestSchema, \
    CourseSchema, GetCoursesResponseSchema, CreateCourseResponseSchema, CreateCourseRequestSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user

@allure.step("Check update course response")
def assert_update_course_response(request: UpdateCourseRequestSchema, response: UpdateCourseResponseSchema):
    """
    Проверяет, что ответ на обновление курса соответствует данным из запроса.

    :param request: Исходный запрос на обновление курса.
    :param response: Ответ API с обновленными данными курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.title, response.course.title, name="title")
    assert_equal(request.max_score, response.course.max_score, name="max_score")
    assert_equal(request.min_score, response.course.min_score, name="min_score")
    assert_equal(request.description, response.course.description, name="description")
    assert_equal(request.estimated_time, response.course.estimated_time, name="estimated_time")


@allure.step("Check course")
def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Проверяет, что фактические данные курса соответствуют ожидаемым.

    :param actual: Фактические данные курса.
    :param expected: Ожидаемые данные курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, name="id")
    assert_equal(actual.title, expected.title, name="title")
    assert_equal(actual.max_score, expected.max_score, name="max_score")
    assert_equal(actual.min_score, expected.min_score, name="min_score")
    assert_equal(actual.description, expected.description, name="description")
    assert_equal(actual.estimated_time, expected.estimated_time, name="estimated_time")

    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)

@allure.step("Check get courses response")
def assert_get_courses_response(get_course_response: GetCoursesResponseSchema, create_course_responses: list[CreateCourseResponseSchema]):

    """
    Проверяет, что ответ на получение списка курсов соответствует ответам на их создание.

    :param get_courses_response: Ответ API при запросе списка курсов.
    :param create_course_responses: Список API ответов при создании курсов.
    :raises AssertionError: Если данные курсов не совпадают.
    """

    assert_length(get_course_response.courses, create_course_responses, name="courses")

    for index, course_course_response in enumerate(create_course_responses):
        assert_course(get_course_response.courses[index], course_course_response.course)

@allure.step("Check create course response")
def assert_create_course_response(response: CreateCourseResponseSchema, request: CreateCourseRequestSchema):
    """
    Проверяет, что ответ на создание курса соответствует запросу.
    :param response: ответ на запрос создания курса
    :param request: запрос на создание курса
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.course.title,request.title, name="title")
    assert_equal(response.course.max_score, request.max_score, name="max_score")
    assert_equal(response.course.min_score, request.min_score, name="min_score")
    assert_equal(response.course.description, request.description, name="description")
    assert_equal(response.course.estimated_time, request.estimated_time, name="estimated_time")

    assert_equal(response.course.preview_file.id, request.preview_file_id, name="preview_file_id")
    assert_equal(response.course.created_by_user.id, request.created_by_user_id, name="created_by_user_id")
