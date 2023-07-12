# # """
# # Some module
# # """
# #
# #
# # class Person:
# #     """
# #
# #     """
# #     role = 'user'
# #
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     def birthday(self):
# #         self.age += 1
# #
# #     @classmethod
# #     def from_list(cls, objs: list):
# #         return [cls(**obj) for obj in objs]
# #
# #     @staticmethod
# #     def foo():
# #         print('foo')
# #
# #
# # # print(Person.from_list([{'name': 'Alex', 'age': 24}, {'name': 'Pavel', 'age': 34}]))
# # # __new__ __init__
# # # person1 = Person(name='Alex', age=24)
# # # person2 = Person(name='Pavel', age=34)
# # # person1.birthday()
# # # print(person1.age)
# # # Person.birthday(person1)
# #
# #
# # # TODO написать класс Category
# # #  1. Объявить атрибут класса categories со значением пустой список
# # #  2. Написать метод класса add принимающий на вход название новой категории
# # #  если такая категория есть в атрибуте класса categories, то вызвать исключение
# # #  ValueError, в противном случае добавить новую категорию в атрибут класса categories
# # #  и вернуть индекс вхождения новой категории в список categories
# #
# # class Category:
# #     categories = []
# #
# #     @classmethod
# #     def add(cls, new_category):
# #         if new_category.title() in cls.categories:
# #             raise ValueError('new category is not unique')
# #         else:
# #             cls.categories.append(new_category.title())
# #             return len(cls.categories) - 1
# #
# #     @classmethod
# #     def get(cls, pk):
# #         return cls.categories[pk]
# #
# #     @classmethod
# #     def remove(cls, pk):
# #         try:
# #             del cls.categories[pk]
# #         except IndexError:
# #             pass
# #
# # # TODO написать метод класса get принимающий номер категории и возвращающий соответствующую
# # #  категорию из списка categories, если категории нет, вызывать исключение IndexError
# #
# # # TODO написать метод класса remove принимающий номер категории и удаляющий соответствующую
# # #  категорию из списка categories, если категории нет, ничего не должно происходить
# #
# #
# # class User:
# #
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #         self.i = -1
# #         self.is_active = True
# #
# #     # def __str__(self):
# #     #     return f'User: name={self.name}'
# #
# #     def __repr__(self):
# #         return f'User: name={self.name}'
# #
# #     def __len__(self):
# #         return len(self.name)
# #
# #     def disable(self):
# #         self.is_active = False
# #
# #     def __getitem__(self, item):
# #         return self.name[item]
# #
# #     def __enter__(self):
# #         return self
# #
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         self.disable()
# #
# #     def __add__(self, other):
# #         if isinstance(other, int):
# #             return self.age + other
# #         elif isinstance(other, User):
# #             return self.age + other.age
# #         else:
# #             raise ValueError
# #
# #     def __radd__(self, other):
# #         return self.__add__(other)
# #
# #     def __iadd__(self, other):
# #         if isinstance(other, int):
# #             self.age += other
# #             return self
# #         else:
# #             raise TypeError
# #
# #     # def __iter__(self):
# #     #     return self
# #     #
# #     # def __next__(self):
# #     #     self.i += 1
# #     #     try:
# #     #         return self.name[self.i]
# #     #     except IndexError:
# #     #         self.i = -1
# #     #         raise StopIteration
# #
# #
# # from typing import List, Dict, Union, Sequence, Optional, Sized
# #
# #
# # def is_palindrome(text: str) -> bool:
# #     """Проверка строки на палиндром
# #
# #     >>> res = is_palindrome('Hello')
# #     >>> print(res)  # False
# #
# #     :param text: Строка для проверки на палиндром
# #     :return: True - если строка палиндром, иначе False
# #     """
# #     text = text.lower()
# #     return text == text[::-1]
# #
# #
# # def bar(objs: Sequence):
# #     print(objs)
# #
# #
# # def foo(numbers: List[Union[int, float]], a: Optional[int] = None) -> None:
# #     print(numbers)
# #
# #
# # numbers = [1, 2, 3, 4]
# #
# #
# # def bar1(numbers: list):
# #     for number in numbers:  # type: int
# #         pass
# from django.views.generic import ListView
#
#
# class User:
#
#     def __init__(self, name: str, email: str) -> None:
#         self.name = name
#         self.email = email
#         self.is_active = True
#
#     def __repr__(self):
#         return f'User name={self.name} email={self.email}'
#
#     def __bool__(self):
#         return self.is_active
#
#
# class Manager(User):
#
#     def __init__(self, name: str, email: str, salary: int):
#         super().__init__(name, email)
#         self.salary = salary
#
#     def foo(self):
#         print('foo')
#
#
# class A:
#     name = 'a'
#
#
# class B:
#     name = 'B'
#
#
# class C(A, B):
#     pass
#
#
# # print(C.mro())
# # print(ListView.mro())


class Transport:

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def work(self, time):
        return time * self.power


class BeepMixin:

    def beep(self):
        return 'Beep-beep'


class Car(BeepMixin, Transport):

    def __init__(self, name, power, passenger_seat, wheel_count):
        super().__init__(name, power)
        self.passenger_set = passenger_seat
        self.wheel_count = wheel_count

    def work(self, time):
        w = super().work(time)
        return round(w, 2)


class User:

    def __init__(self, email, password):
        self.email = email
        self.__password = password

    @property
    def upper_email(self):
        return self.email.upper()

    @property
    def password(self):
        return self.__password[:4] + '*' * len(self.__password[4:])

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError

        if len(value) < 8 or len(value) > 64:
            raise ValueError

        self.__password = value


class Duck:

    def swim(self):
        print('swim duck')


class Fish:

    def swim(self):
        print('swim fish')


def foo(obj: Duck | Fish):
    if isinstance(obj, Duck | Fish):
        obj.swim()
    else:
        raise TypeError
