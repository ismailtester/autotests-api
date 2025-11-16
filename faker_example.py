from faker import Faker


fake = Faker("ru_RU") #ru_RU нужен для локализации фейковых данных под русский регион

print(fake.name()) #Печатает не просто имя, а ФИО
print(fake.address())
print(fake.email())


data = {
    "name": fake.name(),
    "email": fake.email(),
    "age": fake.random_int(min=18, max=100)
}

print(data)
