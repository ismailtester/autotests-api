import pytest
from pydantic import BaseModel

from clients.courses.courses_client import get_courses_client, CoursesClient
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from clients.files.files_client import FilesClient
from clients.users.private_users_client import PrivateUsersClient
from clients.users.users_schema import GetUserResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

    @property
    def course_id(self) -> str:
        return self.response.course.id

@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)

@pytest.fixture
def function_course(
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_file: FileFixture,
        files_client: FilesClient,
        private_users_client: PrivateUsersClient,
) -> CourseFixture:
    # 1) кто мы по токену
    me_resp = private_users_client.get_user_me_api()
    print("me:", me_resp.status_code, me_resp.text)
    me_id = GetUserResponseSchema.model_validate_json(me_resp.text).user.id

    # 2) существование file_id
    file_resp = files_client.get_file_api(function_file.file_id)
    print("file:", file_resp.status_code, file_resp.text)

    # 3) что реально уходит в /courses
    request = CreateCourseRequestSchema(
        preview_file_id=function_file.file_id,
        created_by_user_id=function_user.user_id,
    )
    print("created_by_user_id:", function_user.user_id, "me_id:", me_id)
    print("payload:", request.model_dump(by_alias=True))

    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)

