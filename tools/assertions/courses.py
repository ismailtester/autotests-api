from clients.courses.courses_schema import UpdateCourseResponseSchema, UpdateCourseRequestSchema, \
     CourseSchema, GetCoursesResponseSchema, CreateCourseResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user


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

    assert_file(actual.preview_file, expected.preview_file),
    assert_user(actual.created_by_user, expected.created_by_user),

def assert_get_courses_response(get_course_response: GetCoursesResponseSchema, create_course_responses: list[CreateCourseResponseSchema]):


    assert_length(get_course_response.courses, create_course_responses, name="courses")

    for index, course_course_response in enumerate(create_course_responses):
        assert_course(get_course_response.courses[index], course_course_response.course)
