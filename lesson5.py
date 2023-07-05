# # a = 0
# #
# # if a > 0:
# #     print('a is positive')
# # elif a == 0:
# #     print('a is zero')
# # else:
# #     print('a is not positive')
# from typing import Union
#
# # a = 45
#
# # is_even = 'No' if a % 2 else 'Yes'
# # print(sep='-' if a % 2 else '|')
#
# # a = (5, 6)
# # match a:
# #     case 5, 6:
# #         print('')
# #     case 4, 3:
# #         print()
# #     case _:
# #         print()
#
#
# # if not condition1 and condition2:
#
# # if cond1 or cond2 and cond3:
# #     pass
#
# # a = '5'
# # if isinstance(a, int) and a > 0:
# #     pass
#
#
# # x = True
# # y = False
# # z = False
# # if not x or y:
# #     print(1)  #
# # elif not x or not y and z:
# #     print(2)  #
# # elif not x or y or not y and x:
# #     print(3)  # +++++
# # else:
# #     print(4)  #
#
# # GOOD
# # print(isinstance(12, (int, float))
#
# # BAD
# # print(type(5) is int or type(5) is float)
#
#
# # for i in range(1, 10, 2):  # 1 3 5 7 9
# #     i **= 2
# #     print(i)
#
# # str list tuple set frozenset
# text = 'hello'
# # for i in text:
# #     print(i)
#
# # for i in range(len(text)):
# #     print(text[i])
#
# for i, j in enumerate(text):
#     print(i)


# l = [
#     (1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9),
#     (10, 11, 12),
# ]
# for i, j, k in l:
#     print(f'{i=}', f'{j=}', f'{k=}')

# data = [
#     ('Cappuccino', 'Good', 5.5),
#     ('Latte', 'Bad', 6.2),
# ]
# for product in data:
#     print(product[0], product[1], product[2])

# s = set('hello')
# for i, j in enumerate(s):
#     print(i, j)
#
# for i, j in enumerate(s):
#     print(i, j)


# data = {
#     'key1': 'value1',
#     'key2': 'value2',
#     'key3': 'value3',
#     'key4': 'value4',
# }
# for key, val in data.items():
#     print(key, val)
# is_break = False
# for i in range(10):
#     if i == 10:
#         is_break = True
#         break

#     print(i)
# # else:
# #     print('finish')
# if not is_break:
#     print()

# a = 5
# while a > 0:
#     a -= 1

# TODO Заполнить список квадратами четных чисел кратных 6 в диапазоне от 0 до 100
# numbers = [i ** 2 for i in range(0, 101, 2) if i % 6 == 0]
#
# for i in range(0, 101, 2):
#     if i % 6 == 0:
#         numbers.append(i ** 2)
# print(numbers)

# for _ in range(5):
#     print('Hello world')


# TODO Пользователь вводит сумму депозита и процентную ставку по вкладу капитализации
#  необходимо высчитать через сколько лет вклад удвоится
# deposit = int(input('enter deposit: '))
# percent = int(input('enter percent: '))
# percent = percent / 100 + 1
# target = deposit * 2
# year = 0
# while deposit < target:
#     year += 1
#     deposit *= percent
# print(year)

# TODO Есть монеты номиналом 1 5 10 25
#  Пользователь вводит сумму в копейках
#  Необходимо подсчитать минимальное количество монет для представления данной суммы
#  пример: 49 -> 25 + 10 + 10 + 1 + 1 + 1 + 1 -> 7

# coins = (25, 10, 5, 1)
# amount = int(input('enter amount: '))
# coins_count = 0
# for coin in coins:
#     coins_count += amount // coin
#     amount -= (amount // coin) * coin
# print(coins_count)

# TODO Дан список чисел, необходимо отфильтровать список оставив только четные числа
#  использовать дополнительный список незаконно
# numbers = [3, 1, 2, 2, 5, 7]
# for number in numbers:
#     if number % 2:
#         numbers.remove(number)

# При удалении элементов из списка при его переборе, учитывайте смещение
# for i in range(len(numbers) - 1, -1, -1):
#     if numbers[i] % 2:
#         del numbers[i]

# нельзя расширять список каждую итерацию (получите вечный цикл)
# for number in numbers:
#     numbers.append(number)
#
# print(numbers)

# words = ('hello', 'python', 'world')
#
# for word in words:
#     for letter in word:
#         print(letter)


# try:
#     a = int(input('a: '))
#     b = int(input('b: '))
#     c = a / b
# except ValueError as e:
#     print('введено не число')
# except ZeroDivisionError as e:
#     print('на 0 делить нельзя')
# except Exception as e:
#     print(e)
#     print('все остальные ошибки')
# else:
#     print('ошибок не было')
# finally:
#     print('в любом случае')

# try:
#     a = 4 / 0
# finally:
#     print('OK')


# raise ValueError('моя ошибка')


# TODO Пользователь вводит число, необходимо вывести максимальную цифру данного числа
# number = input('enter number: ')
# max_num = 0
# for num in number:
#     if int(num) > max_num:
#         max_num = int(num)
# print(max_num)

# TODO Используя бинарный поиск, вывести словарь у которого ключ age == 13
data = [
    {'name': 'Name1', 'age': 12},
    {'name': 'Name2', 'age': 13},
    {'name': 'Name3', 'age': 15},
    {'name': 'Name4', 'age': 18},
    {'name': 'Name5', 'age': 22},
    {'name': 'Name6', 'age': 34},
    {'name': 'Name7', 'age': 37},
]


# N = 34
# 2 4 6 8 10
# 12 14 16 18 20
# 22 24 26 28 30
# 32 34

# number = input('enter number: ')
# while not number.isdigit():
#     number = input('enter number: ')

# while not (numbers := input('enter number: ')).isdigit(): pass
