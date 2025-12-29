from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExercisesRequestSchema, Exercise, \
    GetExerciseResponseSchema
from tools.assertions.base import assert_equal


def assert_create_exercise_response(actual: CreateExerciseResponseSchema, expected: CreateExercisesRequestSchema):
    """
    Проверяет, что ответ на создание упражнения соответствует данным запроса.

    :param actual: Ответ API на создание упражнения (CreateExerciseResponseSchema).
    :param expected: Запрос на создание упражнения (CreateExercisesRequestSchema).
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.exercise.title, expected.title, name="title")
    assert_equal(actual.exercise.course_id, expected.course_id, name="course_id")
    assert_equal(actual.exercise.max_score, expected.max_score, name="max_score")
    assert_equal(actual.exercise.min_score, expected.min_score, name="min_score")
    assert_equal(actual.exercise.order_index, expected.order_index, name="order_index")
    assert_equal(actual.exercise.description, expected.description, name="description")
    assert_equal(actual.exercise.estimated_time, expected.estimated_time, name="estimated_time")

def assert_exercise(actual: Exercise, expected: Exercise):
    """
    Проверяет, что фактические данные пользователя соответствуют ожидаемым.

    :param actual: Фактическая информация по упражнению.
    :param expected: Ожидаемые информация по упражнению.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, name="id")
    assert_equal(actual.title, expected.title, name="title")
    assert_equal(actual.course_id, expected.course_id, name="course_id")
    assert_equal(actual.max_score, expected.max_score, name="max_score")
    assert_equal(actual.min_score, expected.min_score, name="min_score")
    assert_equal(actual.order_index, expected.order_index, name="order_index")
    assert_equal(actual.description, expected.description, name="description")
    assert_equal(actual.estimated_time, expected.estimated_time, name="estimated_time")


def assert_get_exercise_response(get_exercise_response: GetExerciseResponseSchema, create_exercise_response: CreateExerciseResponseSchema):
    """
    Проверяет, что данные в ответе на получение данных об упражнении, совпадают с данными в ответе на создание упражнения
    :param get_exercise_response: Ответ на запрос о получении данных об упражнении
    :param create_exercise_response: Ответ от API при создании упражнении
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)