# # numbers = [5, 4, 6, 3, 4, 1, 4, 3]
# # print(numbers[0])
# #
# #
# # data = {'a': 5, 'b': 4}
# # print(data['a'])
#
# # user = {'name': 'Vasya', 'email': 'vasya@gmail.com'}
# # user['city'] = 'Minsk'
# # user['age'] = 34
# # user['name'] = 'Petya'
# # data = ('vasya', 'vasya@gmail.com')
#
# # data = [
# #     {'id': 5, 'name': 'Coffee', 'price': 5.5},
# #     {'id': 5, 'name': 'Latte'},
# # ]
# # for inner_dict in data:
# #     if 'price' in inner_dict:
# #         print(inner_dict['price'])
#
#
# def is_palindrome(text):
#     text = text.lower()
#     return text == text[::-1]
#
#
# def foo(a, b=None, c=34):
#     print(a, b, c)
#
#
# def bar(*args):
#     print(args)
#
#
# def baz(a, b, c=45, *args, d=None, **kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(d)
#     print(kwargs)
#
#
# def func(a, b=None):
#     if b is None:
#         b = []
#     b.append(a)
#     print(b)
#
#
# # TODO Написать функцию, принимающую 3 целочисленных аргумента (a, b, c)
# #  и возвращающая список чисел геометрической прогрессии
# #  от a до b с множителем c
# #  a=2, b=100, c=2
# #  [2, 4, 8, 16, 32, 64]
#
#
# def geom_range(a, b, c):
#     numbers = []
#     while a < b:
#         numbers.append(a)
#         a *= c
#     return numbers
#
#
# # TODO Написать функцию average, принимающая неопределенное количество
# #  чисел и возвращающая среднее значение с точностью 2
#
#
# def average(*numbers):
#     return round(sum(numbers) / len(numbers), 2)
#
#
# # LEGB
#
# # Local
# # Enclosing
# # Global
# # BuiltIt
#
# a = 5
#
#
# def func1():
#     a = 4
#
#     def func2():
#         global a
#         print(a)
#
#     print(locals())
#
#
# multiply = lambda x, y: x * y
#
#


# numbers = [2, 3, 2, 4, '6', '4', '3', 7, 6]
# # ['2', '3', '2', '4', '6', '4', '3', '7', '6']
# numbers.sort(key=lambda x: str(x))
# print(numbers)

# data = [
#     {'name': 'Vasya', 'age': 45},
#     {'name': 'Petya', 'age': 23},
#     {'name': 'Masha', 'age': 18},
#     {'name': 'Masha', 'age': 28},
# ]
# data.sort(key=lambda user: user.get('age', 0))
# print(data)
# print(max(data, key=lambda user: user.get('age')))


# numbers = ['1', '2', '3', '4', '5']
# numbers = [int(number) ** 2 for number in numbers]
# numbers = [number for number in numbers if number % 2]
# numbers = list(map(lambda x: int(x) ** 2, numbers))
# numbers = list(filter(lambda x: x % 2, numbers))
# print(numbers)
# from itertools import zip_longest
#
# text = 'hello'
# numbers = [1, 2, 3, 4]
# t = (True, False, None)
#
# z = list(zip_longest(text, numbers, t, fillvalue='Н/У'))
# print(z)


# TODO Написать функцию, принимающую список чисел и возвращающая аккумулятивную сумму
#  пример: [1, 2, 3, 4, 5]
#  ответ: [1, 3, 6, 10, 15]


def accumulate_sum(numbers):
    s = 0
    res = []
    for number in numbers:
        s += number
        res.append(s)
    return res


# TODO Написать функцию is_pangram принимающая строку и возвращающая:
#  True - если строка является панграммой
#  False - если строка не является панграммой
#  Панграмма - строка (предложение) содержащая все буквы алфавита
from string import ascii_lowercase


def is_pangram(text):
    text = text.lower()
    for letter in ascii_lowercase:
        if letter not in text:
            return False
    return True


def is_pangram2(text):
    return not set(ascii_lowercase) - set(text.lower())


# from functools import reduce
#
# numbers = [1, 2, 3, 4, 5, 6]
# print(reduce(lambda x, y: x * y, numbers))


# TODO Написать функцию paginator принимающая
#  список значений,
#  аргумент paginate_by - положительное число
#  и аргумент page - положительное число
#  функция должна возвращать список значений из исходного, длинной paginate_by
#  для страницы page
#  example:
#  objs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#  paginate_by = 3
#  page = 2
#  result = [4, 5, 6]
# objs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# paginate_by = 3
# page = 2
# objs_iter = iter(objs)
# result = tuple(zip(*[objs_iter] * paginate_by))[page - 1]
# print(result)


numbers = [1, 2, 3, 4, [4, 5, 6, 4, 3, [5, 4, 5, 3, 4, 2, ], [5, 6, 3, 5, 2, 4, 2], [6, 5, 6, 3, 4, 2, 5, 4, [6, 7, 8, 6, 5, 6, ]]]]


def recursive_multiply(numbers):
    m = 1
    for number in numbers:
        if isinstance(number, int | float):
            m *= number
        elif isinstance(number, list | tuple | set):
            m *= recursive_multiply(number)
    return m


# LIFO - Last In First Out
# FIFO - First In First Out
