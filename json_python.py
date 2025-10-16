import json


json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)
print(type(parsed_data)) #<class 'dict'>


#Преобразование из словаря питона в жсон

data = {
    "name": "Мария",
    "age": 25,
    "is_student": True
}

json_data = json.dumps(data, indent=4) #indent добавляет отступы, что бы было красивее
print(json_data) #<class 'str'>


with open("json_example.json", "r", encoding="utf-8") as file:
    read_data = json.load(file)
    print(data, type(data))

with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)