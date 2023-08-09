from io import TextIOWrapper
from abc import ABC, abstractmethod

from sqlalchemy import Column, INT, VARCHAR, BOOLEAN, create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from pydantic import BaseModel, ConfigDict, PositiveInt, Field


class Base(DeclarativeBase):
    engine = create_engine(url='sqlite:///db.sqlite3')
    session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'user'

    id = Column(INT, primary_key=True)
    username = Column(VARCHAR(32), nullable=False, unique=True)
    is_active = Column(BOOLEAN, default=True, nullable=False)


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: PositiveInt
    username: str = Field(min_length=4, max_length=32)
    is_active: bool = Field(default=True)


class UserParser:

    @classmethod
    def parse(cls, file: TextIOWrapper, delimiter: str = ';') -> list["UserSchema"]:
        keys = file.readline().strip().split(delimiter)
        values = [line.strip().split(delimiter) for line in file]
        return [UserSchema(**dict(zip(keys, value))) for value in values]

    @classmethod
    def dump(cls, objs: list[UserSchema], file: TextIOWrapper, delimiter: str = ';') -> None:
        objs = [obj.model_dump() for obj in objs]
        keys = delimiter.join(objs[0].keys()) + '\n'
        values = []
        for obj in objs:
            values.append(delimiter.join(obj.values()) + '\n')
        values.insert(0, keys)
        file.writelines(values)


def load_user_to_db(objs: list[UserSchema]):
    objs = [User(**obj.model_dump()) for obj in objs]
    with User.session() as session:
        session.add_all(objs)
        try:
            session.commit()
        except IntegrityError:
            pass


def dump_user() -> list[UserSchema]:
    with User.session() as session:
        objs = session.scalars(select(User))
        return [UserSchema.model_validate(obj, from_attributes=True) for obj in objs]


# class Singleton:
#     _register = None
#
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         if cls._register is None:
#             obj = type(cls.__name__, args, kwargs)
#             cls._register = obj
#             return obj
#         else:
#             return cls._register
#
#     def __init__(self, name):
#         self.name = name
#
#
# a = Singleton(name='A')


class A:

    name: str = 'A'

    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        print(A.__dict__)
        return type(cls.__name__, args, kwargs)


class YandexMusic:

    @classmethod
    def get_music(cls, name: str) -> str:
        return name


class Spotify:

    @classmethod
    def get_by_name(cls, name: str) -> str:
        return name


class YandexAdapter(YandexMusic):

    @classmethod
    def get(cls, name: str) -> str:
        return cls.get_music(name)


class SpotifyAdapter(Spotify):

    @classmethod
    def get(cls, name: str) -> str:
        return cls.get_by_name(name)


class Music:

    @classmethod
    def get(cls, streaming, name: str):
        return streaming.get(name)


class AbstractObject(ABC):

    @abstractmethod
    def __getitem__(self, item):
        pass

    @abstractmethod
    def __len__(self):
        pass


class AbstractFabric(ABC):

    @abstractmethod
    def create(self, n: int) -> list[AbstractObject]:
        pass


class Product1(AbstractObject):

    def __getitem__(self, item):
        pass

    def __len__(self):
        pass


class Product2(AbstractObject):

    def __len__(self):
        pass

    def __getitem__(self, item):
        pass


class Fabric1(AbstractFabric):

    def create(self, n: int) -> list[AbstractObject]:
        return [Product1() for _ in range(n)]


class Fabric2(AbstractFabric):

    def create(self, n: int) -> list[AbstractObject]:
        return [Product2() for _ in range(n)]
