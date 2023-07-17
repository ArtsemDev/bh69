# # class SomeClass:
# #     a = 5
# #
# #     def __init__(self, pk):
# #         self.__pk = pk
# #
# #     @property
# #     def some_property(self):
# #         return self.a * self.__pk
# #
# #     @property
# #     def pk(self):
# #         return self.__pk
# #
# #     @pk.setter
# #     def pk(self, value):
# #         self.__pk = value
# #
# #     def foo(self):
# #         print('foo')
# #
# #
# # class A(SomeClass):
# #
# #     def foo(self):
# #         raise AttributeError
# #
# #
# # # a = SomeClass(1)
# # # print(a._SomeClass__pk)
# from django.views.generic import ListView
#
#
# class Engine:
#
#     def __init__(self, volume: float, name: str):
#         self.volume = volume
#         self.name = name
#
#     def __repr__(self):
#         return f'Engine: {self.name} with volume: {self.volume}'
#
#
# class Car:
#
#     def __init__(self, name: str, color: str, engine: Engine = None):
#         self.name = name
#         self.color = color
#         self.engine = engine if engine is not None else Engine(5000, 'v8')
#
#     @classmethod
#     def create(cls, names: list[str], colors: list[str], engines: list[Engine]):
#         return [cls(*args) for args in zip(names, colors, engines)]
#
#
# from abc import ABC, abstractmethod
#
#
# class AbstractUser(ABC):
#
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#     @classmethod
#     @abstractmethod
#     def get(cls):
#         pass
#
#
# class User(AbstractUser):
#
#     @classmethod
#     def get(cls):
#         pass
#
#
# vasya = User('vasya', 'vasya@gmail.com')
from abc import ABC, abstractmethod


class AbstractCategory(ABC):

    @classmethod
    @abstractmethod
    def get(cls, pk: int) -> str:
        pass


class AbstractMenu(ABC):

    @abstractmethod
    def get(self, item: AbstractCategory, pk: int) -> str:
        pass


class Category(AbstractCategory):

    __categories = ('Coffee', 'Pancake', 'Sandwich')

    @classmethod
    def get(cls, pk) -> str:
        return cls.__categories[pk]


class Menu(AbstractMenu):

    def get(self, item, pk) -> str:
        return item.get(pk)


class A:

    def __init__(self, n):
        self.numbers = [i for i in range(n)]

    def __len__(self):
        return len(self.numbers)

    def __getitem__(self, item):
        return self.numbers[item]

    def __contains__(self, item):
        return item in self.numbers


# TODO Написать класс ConfigParser, конструктор класса принимает строку в формате:
text = '''


[Section1]
key1=value1
key2=value2


[Section2]
key3=value3

key4=value4
'''
# TODO написать метод класса loads, который будет вызываться в конструкторе, данный метод
#  принимает данную строку и преобразовывает в словарь словарей
#  результат метода после вызова в конструкторе, помещается в атрибут объекта data
data = {
    'Section1': {
        'key1': 'value1',
        'key2': 'value2',
    },
    'Section2': {
        'key3': 'value3',
        'key4': 'value4'
    }
}


class ConfigParser:

    def __init__(self, text: str) -> None:
        self.data = self.loads(text)

    @classmethod
    def loads(cls, text: str) -> dict[str, dict[str, str]]:
        lines = [line for line in text.split('\n') if line]
        data = {}
        current_section = ''
        for line in lines:
            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1]
                data[current_section] = {}
            else:
                key, value = line.split('=')
                data[current_section][key] = value
        return data

    def has_section(self, section: str) -> bool:
        return section in self.data

    def has_param(self, section: str, param: str) -> bool:
        try:
            return param in self.data[section]
        except KeyError:
            raise ValueError

    def add_section(self, section: str) -> None:
        if self.has_section(section):
            raise ValueError
        self.data[section] = {}


# TODO
#  1. объявить метод has_section принимающий название секции и возвращающий
#  True - если такая секция есть, в противном случае False
#  2. объявить метод has_param принимающий название секции и название параметра
#  если указанной секции нет - ValueError
#  True - если есть указанный параметр в указанной секции иначе False
#  3. объявить метод add_section принимающий название новой секции и объявляющий ее
#  в случае отсутствия, если такая секция уже есть, вызвать исключение ValueError
#  4. объявить метод add_param принимающий название секции, название параметра и значение
#  если нет указанной секции - ValueError
#  если в секции нет указанного параметра - объявить параметр с указанным значением
#  если в секции есть указанный параметр - заменить его значение на новое
#  5. объявить метод del_section - принимающий название секции и удаляющий ее, если секции
#  нет, ничего происходить не должно
#  6. объявить метод del_param - принимающий название секции и название параметра
#  если данной секции нет - ValueError
#  если параметра в секции нет - ничего не происходит
#  если параметр в секции есть - удалить его
#  7. объявить метод dumps превращающий словарь в строку согласно формату
#  и возвращающий данную строку
