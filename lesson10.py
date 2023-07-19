# # from pathlib import Path
# #
# #
# # BASE_DIR = Path(__file__).resolve().parent
# #
# #
# # # file = open(BASE_DIR / 'input.txt', 'r', encoding='utf-8')
# # # # print(file.read())
# # # # print(file.readline())
# # # # print(file.readlines())
# # # lines = [line.strip() for line in file if line.strip()]
# # #
# # # file.close()
# # # with open() as file, open() as file2, open() as file3:
# # #     pass
# #
# # # with (
# # #     open(BASE_DIR / 'input.txt', 'r', encoding='utf-8') as file,
# # #     open('output.txt', 'w', encoding='utf-8') as file2
# # # ):
# # #     print(file.read())
# #
# # # with open('output.txt', 'w', encoding='utf-8') as file:
# # #     from time import sleep
# # #     for _ in range(100):
# # #         file.write('hello\n')
# # #         file.flush()
# # #         sleep(3)
# #
# #
# # # TODO дан текстовый многострочный файл, в каждой строке написаны числа через пробел
# # #  необходимо найти сумму чисел в каждой строки и результаты записать в новый файл
# # with (
# #     open(BASE_DIR / 'input.txt', 'r', encoding='utf-8') as input_file,
# #     open(BASE_DIR / 'output.txt', 'w', encoding='utf-8') as output_file
# # ):
# #     output_file.writelines(
# #             f'{sum(int(number) for number in line.strip().split())}\n'
# #             for line in input_file if line.strip()
# #     )
# #     # result = []
# #     # for line in input_file:
# #     #     line = line.strip().split()
# #     #     line = [int(i) for i in line]
# #     #     result.append(f'{sum(line)}\n')
# #     # output_file.writelines(result)
#
#
# # with open('output.txt', 'w', encoding='utf-8') as file:
# #     line = '*' * 100 + '\n'
# #     while True:
# #         file.write(line)
#
#
# from csv import reader, DictReader, writer, DictWriter
#
#
# # with open('input.csv', 'r', encoding='utf-8') as csv_file:
#     # r = (line.strip().split(',') for line in csv_file)
#     # for line in r:
#     #     print(line)
#     # r = reader(csv_file)
#     # for line in r:
#     #     print(line)
#     # r = DictReader(csv_file, fieldnames=('name', 'email', 'age'), delimiter=';')
#     # for line in r:
#     #     print(line)
#
#
# line = [
#     {'name': 'vasya', 'email': 'vasya@gmail'},
#     {'name': 'petya', 'email': 'petya@gmail'},
# ]
#
# with open('output.csv', 'w', encoding='utf-8') as csv_file:
#     # w = writer(csv_file)
#     # w.writerows(line)
#     w = DictWriter(csv_file, fieldnames=('name', 'email'))
#     w.writerows(line)
#     w.writeheader()


from json import load, loads, dump, dumps


# with open('input.json', 'r', encoding='utf-8') as file:
    # data = loads(file.read())


# data = {
#     'name': 'Алекс',
#     'city': 'Minsk'
# }
#
# with open('output.json', 'w', encoding='utf-8') as file:
#     dump(data, file, indent=2, ensure_ascii=False)


# from datetime import datetime
#
# print(datetime.utcnow().isoformat())
# print(datetime.utcnow().timestamp())

# from yaml import safe_load
#
# with open('input.yaml', 'r', encoding='utf-8') as file:
#     data = safe_load(file)
# print(data)


# from configparser import ConfigParser


# with open('config.ini', 'r', encoding='utf-8') as file:
#     parser = ConfigParser()
#     parser.read_file(file)


from pydantic import (
    BaseModel,
    EmailStr,
    PostgresDsn,
    Field,
    field_validator,
    model_validator,
    validate_call, ValidationError
)
from pydantic.types import Decimal


# class User(BaseModel):
#     name: str
#     email: EmailStr
#     age: int
#     languages: list[int]
#
#
# vasya = User(
#     name='Vasya',
#     email='vasyagmail.com',
#     age='23ee',
#     languages=[2, 3, 4, 'ert']
# )
# print(vasya)
from typing import Optional, List, Literal


class SomeModel(BaseModel):
    key: str | None
    key2: str = None
    key3: Optional[str]
    key4: str = Field(default=None)
    key5: str = Field(...)
    price: Decimal = Field(max_digits=8, decimal_places=2)


class Product(BaseModel):
    name: str
    price: Decimal = Field(max_digits=8, decimal_places=2)


class Category(BaseModel):
    name: str
    products: List[Product]
    parent: Optional["Category"]


class Schema(BaseModel):
    key1: str
    key2: str
    key3: Literal['value1', 'value2']

    @field_validator('key1')
    def key1_validator(cls, value: str):
        return value

    @model_validator(mode='after')
    def validator(cls, values: dict):
        return values


@validate_call()
def is_palindrome(text: str) -> bool:
    return text.lower() == text.lower()[::-1]



db = ('vasya@gmail.com', 'petya@gmail.com')


class Person(BaseModel):
    email: EmailStr

    @field_validator('email')
    def email_validator(cls, email: str):
        if email in db:
            raise ValueError('email is not unique')
        return email


user = Person(email='qwer@gmail.com')
try:
    user2 = Person(email='vasya@gmail.com')
except ValidationError as e:
    print(e.errors())
