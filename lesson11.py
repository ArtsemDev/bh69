from abc import ABC, abstractmethod
from io import TextIOWrapper
from typing import Type, List, TypeVar

from pydantic import BaseModel, Field, PositiveInt
from pydantic.types import Decimal
from pydantic_core import ValidationError
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from lesson13 import Category

Schema = TypeVar('Schema', bound=BaseModel)


class Parser(ABC):
    schema: Type[BaseModel]

    @classmethod
    @abstractmethod
    def parse(cls, file: TextIOWrapper, delimiter: str) -> List[Schema]:
        ...

    @classmethod
    @abstractmethod
    def dump(cls, objs: List[Schema], file: TextIOWrapper, delimiter: str) -> None:
        ...



class ProductDetail(BaseModel):
    title: str = Field(..., max_length=128)
    descr: str = Field(..., max_length=4096)
    price: Decimal = Field(..., max_digits=8, decimal_places=2)
    count: PositiveInt


class ProductParser(Parser):
    schema = ProductDetail

    @classmethod
    def dump(cls, objs: List[Schema], file: TextIOWrapper, delimiter: str) -> None:
        objs = [obj.model_dump() for obj in objs]
        fieldnames = delimiter.join(objs[0].keys())
        objs = [delimiter.join(f'{value}' for value in obj.values()) for obj in objs]
        objs.insert(0, fieldnames)
        file.write('\n'.join(objs))

    @classmethod
    def parse(cls, file: TextIOWrapper, delimiter: str) -> List[Schema]:
        fieldnames = file.readline().strip().split(delimiter)
        values = [line.strip().split(delimiter) for line in file]
        values = [dict(zip(fieldnames, value)) for value in values]
        data = []
        for value in values:
            try:
                data.append(cls.schema(**value))
            except ValidationError:
                pass
        return data


def load_to_db(file, delimiter):
    objs = ProductParser.parse(file=file, delimiter=delimiter)
    objs = [Category(**obj.model_dump()) for obj in objs]
    with Category.session() as session:
        session.add_all(objs)
        try:
            session.commit()
        except IntegrityError:
            pass


def dump_from_db(file, delimiter):
    with Category.session() as session:
        objs = session.scalars(select(Category))
        data = []
        for obj in objs:
            data.append(ProductDetail.model_validate(obj, from_attributes=True))

        ProductParser.dump(data, file, delimiter)

# a = 'abcd'
# b = 'efgh'
#
# print(list(product(a, a)))

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(dropwhile(lambda x: x != 4, number)))
# print(list(takewhile(lambda x: x != 4, number)))

# t = 'wertyui'
# for i in islice(t, 2, 6, 1):
#     print(i)


# print(list(accumulate([1, 2, 3, 4, 5, 6, 7, 8, 9], func=lambda x, y: x * y)))


from enum import Enum
from dataclasses import dataclass


class Role(int, Enum):
    USER: int = 1
    MANAGER: int = 2
    ADMIN: int = 3


@dataclass(frozen=True)
class User:
    name: str
    role_id: int


class MyUser:

    def __init__(self, name, role_id):
        self.name = name
        self.role_id = role_id


# 1 - user
# 2 - manager
# 3 - admin


# user = User(name='Vasya', role_id=3)

# if user.role_id == Role.ADMIN:
#     pass

from functools import *

from time import sleep


@lru_cache()
def foo(a, b):
    sleep(3)
    return a * b


@total_ordering
class A:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @cached_property
    def c(self):
        sleep(3)
        return self.a * self.b

    def __eq__(self, other):
        return self.c == other.c

    def __ge__(self, other):
        return self.c >= other.c


def bar(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper doc

        :param args:
        :param kwargs:
        :return:
        """
        return func(*args, **kwargs)

    return wrapper


@bar
def baz():
    """BAZ DOC

    :return:
    """
    print('baz')


from requests import Session


def get():
    with Session() as session:  # type: Session
        response = session.get(
            url='https://sputnik.by/economy/'
        )
        print(response.status_code)
    # soup = bs(response.text, 'lxml')
    # print(soup.find_all('div', {'class': 'schema-product__title'}))
    # tags_a = soup.find_all('a', {'class': 'list__title'})
    # for tag_a in tags_a:
    #     print(tag_a.text)
    #     print(tag_a['href'])
