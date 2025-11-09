

from pydantic import BaseModel, Field, ConfigDict


class Exercise(BaseModel):
    """
    Описание структуры запроса упражнения.
    """
    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)  #Позволяет при создании модели использовать как snake_case так и camelCase
    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int | None  = Field(alias="orderIndex")
    description: str
    estimated_time: str  = Field(alias="estimatedTime")


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры запроса на получение информации об определенном упражнении.
    """
    exercise: Exercise

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры запроса на получение информации об упражнениях определенного курса.
    """
    exercises: list[Exercise]


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    exercise: Exercise

class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    exercise: Exercise



class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений определенного курса.
    """
    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)
    course_id: str = Field(alias="courseId")

class CreateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса для создания упражнения.
    """
    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class UpdateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления информации об упражнении.
    """
    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")
