from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.files.files_client import get_files_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from tools.fakers import get_random_email
from clients.users.users_schema import CreateUserRequestSchema
from clients.files.files_schema import CreateFileRequestSchema


public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

create_user_response = public_users_client.create_user(create_user_request)
print(f"\nCreated user data: \n{create_user_response}")

authetication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(authetication_user)


create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory = "courses",
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)
print(f"\nCreated file data:\n {create_file_response}")

courses_client = get_courses_client(authetication_user)

create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id)

create_course_response = courses_client.create_course(create_course_request)
print(f"\nCreated course data: \n {create_course_response}")