# objs = [2, 3, 4, 'hello', 'world', True, None]
#
# for i in range(len(objs) - 1, -1, -1):
#     if not isinstance(objs[i], str):
#         del objs[i]
#
# # objs = list(filter(lambda x: isinstance(x, str), objs))
# # objs = [obj for obj in objs if isinstance(obj, str)]
# print(objs)
from datetime import datetime
from functools import wraps


def my_range(start, stop, step):
    for i in range(start, stop, step):
        yield i ** 2


# c = 0
# m = my_range(2, 200, 2)
# for i in m:
#     print(f'first loop: {i}')
#     c += 1
#     if c == 10:
#         break
#
# for i in m:
#     print(f'second loop: {i}')

# TODO написать генератор геометрической прогрессии от start до stop с множителем multiplier


def grange(start, stop, multiplier):
    if (start < stop) and (multiplier > 1):
        while start < stop:
            yield start
            start *= multiplier
    elif (start > stop) and (multiplier < 1):
        while start > stop:
            yield start
            start *= multiplier
    else:
        raise ValueError


def infinity_range(start, step):
    while True:
        yield start
        start += step


def foo1():
    print('foo1')


def foo2():
    print('foo2')


def foo3():
    print('foo3')


def error():
    print('error')


# a = 'fgyihuojk'
#
# data = {
#     'first': foo1,
#     'second': foo2,
#     'third': foo3
# }
# data.get(a, error)()


def bar():
    print('bar')


def baz(func):
    func()


# def wrapper(a):
#
#     def wrapped(b):
#         print(a * b)
#
#     return wrapped


def is_digit_args(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError

        res = func(*args)
        return f'{res=}'

    return wrapper


# @is_digit_args
def multiply(*args):
    from functools import reduce
    return reduce(lambda x, y: x * y, args)


# wrapped_multiply = is_digit_args(multiply)
# print(wrapped_multiply(3, 4, 5, 6))

def log(func):

    def wrapper(*args, **kwargs):
        with open('log.log', 'a', encoding='utf-8') as file:
            file.write(f'{func.__name__} {datetime.now()} {args} {kwargs}')
        return func(*args, **kwargs)

    return wrapper


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        res = func(*args, **kwargs)
        end_time = datetime.now()
        print(end_time - start_time)
        return res

    return wrapper


@log
@timeit
def some_function(a, b):
    from time import sleep
    sleep(3)
    return a * b


data = {}


def dispatcher(text):
    def wrapper(func):
        data[text] = func

        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapped

    return wrapper


@dispatcher('hello')
def func1():
    print('func1')


@dispatcher('googdbye')
def func2():
    print('func2')


def is_instance(*decorator_args, **decorator_kwargs):
    def wrapper(func):
        def wrapped(*args, **kwargs):
            for i in range(len(decorator_args)):
                if not isinstance(args[i], decorator_args[i]):
                    raise TypeError

            for key, val in decorator_kwargs.items():

                if not isinstance(kwargs.get(key), val):
                    raise TypeError

            return func(*args, **kwargs)

        return wrapped

    return wrapper


@is_instance(int, text=str)
def is_palindrome(a, text):
    text = text.lower()
    return text == text[::-1]


# TODO Функция принимает на вход строку и подсчитывает количество
#  гласных и согласных букв в данной строке
#  {'vowels': 5, 'consonants': 12}


def letter_analyzer(text):
    text = text.lower()
    vowels = 'eyuioa'
    consonants = 'qwrtpsdfghjklzxcvbnm'

    data = {'vowels': 0, 'consonants': 0}
    for char in text:
        if char in vowels:
            data['vowels'] += 1
        elif char in consonants:
            data['consonants'] += 1
        # if char.isalpha():
            # if char in vowels:
            #     data['vowels'] += 1
            # else:
            #     data['consonants'] += 1
    return data


# print(False or None)  # возвращает левый операнд если он True иначе правый
# print(False and 8)  # возвращает правый операнд если левый True иначе левый


# TODO написать функцию validate_email
#  принимающую строку с почтой и проверяющая ее на валидность (возвращать должна true/false)
#  наличие строго 1 символа @ (не в начале)
#  наличие 1 точки после символа @
#  до символа @ могут использоваться буквы, цифры и точки

def validate_email(email):
    if '@' not in email or email.find('@') == 0:
        return False

    if email.rfind('.') < email.find('@'):
        return False

    for char in email[:email.find('@')]:
        if not char.isalnum() and char != '.':
            return False

    return True


# TODO написать функцию is_leap_year - проверяющая является ли переданный год високосным
#  1. Високосный год должен делиться без остатка на 4
#  2. Если год делиться без остатка на 100, он так же должен делиться на 400
#  чтобы считаться високосным
#  В противном случае год не является високосным

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)


# TODO возвести число А в степень Б используя рекурсию

def recursive(base, exp):
    if exp > 1:
        base *= recursive(base, exp-1)
    return base


# print(recursive(2, 4))


# TODO Написать функцию, генерирующая двумерную матрицу размером n*n, заполненную по спирали
#  [
#    [1, 2, 3],
#    [8, 9, 4],
#    [7, 6, 5]
#  ]
