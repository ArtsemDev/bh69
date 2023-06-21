# age = 34
# name = 'Alex'
# is_human = True
#
# # text = 'Hello  your age  is human '
# text1 = 'Hello ' + name + ' your age ' + str(age) + ' is human ' + str(is_human)
# text2 = 'Hello %s your age %d is human %d' % (name, age, is_human)
# text3 = 'Hello {} your age {} is human {}'.format(name, age, is_human)
# text4 = f'Hello {name} your age {age * 2} is human {is_human}'
#
# # print(f'{name:*>10}')
# # print(f'{2 * 2=     }')
# # print(f'{name!r}')
# # print(f'{"привет"!a}')
# # print(f'{32345678.14159:,.2f}')
#
# # print('\N{fire}')
#
#


# text = 'Hello___world___python'
# print(text.split('___', 1))
# print(text.rsplit('___', 1))
# print(' | '.join(['hello', 'world']))

# text = 'hello world python world'
# print(text.replace(' ', '', 2))
# print(text.find('world'))
# print(text.rfind('world'))
# print(text.index('world'))
# print(text.rindex('world'))
# print(text.count('world', 10, 16))
# print(text.partition('world'))
# print(text.rpartition('world'))
# print('for'.isidentifier())
# print('hello world'.casefold())
# print('ß'.lower())
# print('ß'.upper())
# print('ß'.title())
# print('ß'.capitalize())
# print('ß'.swapcase())
# print('ß'.casefold())

# print('hello\tworld\tpython\tpycharm'.expandtabs(12))

# print('-=-=-=-,.,/./hello,./,./world,./,./-=-=-='.strip('-=,./'))
# print('-=-=-=-,.,/./hello,./,./world,./,./-=-=-='.lstrip('-=,./'))
# print('-=-=-=-,.,/./hello,./,./world,./,./-=-=-='.rstrip('-=,./'))

# print('hello'.center(12, '_'))
# print('hello'.ljust(12, '_'))
# print('hello'.rjust(12, '_'))
# print('hello'.zfill(12))


# print(bin(14)[2:].zfill(8))


# TODO Пользователь вводит строку состоящую из 3х слов
#  необходимо поменять местами первое и последнее слово
# text = input('enter text: ')
# first_space = text.find(' ')
# last_space = text.rfind(' ')
# first_word = text[:first_space]
# center = text[first_space: last_space + 1]
# last_word = text[last_space + 1:]
# text = last_word + center + first_word

# result = ' '.join(input().split()[::-1])


# a = 400
# b = 20 * 20
# print(a is b)

# print(bin(13))
# print(bin(14))
# print(bin(13 ^ 14))
# print(~-10)


# text = 'qwerty'


# TODO пользователь вводит слово, не учитывая регистр, проверить является ли
#  данное слово палиндромом (вывести True или False)

# text = input().lower()
# print(text == text[::-1])


# TODO Вводится возраст отца и сына, посчитать сколько лет назад или через сколько лет
#  отец был/будет в два раза старше сына

# dad = int(input())
# son = int(input())
# print(dad - son * 2)

# TODO Вводится трехзначное число, посчитать сумму его цифр

# number = input()
# print(int(number[0]) + int(number[1]) + int(number[2]))

# TODO Вводятся координаты двух точек на координатной плоскости, высчитать расстояние
#  между ними

x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
width = abs(x1) + abs(x2)  # abs(x1 - x2)
height = abs(y1) + abs(y2)  # abs(y1 - y2)
length = (width ** 2 + height ** 2) ** 0.5
print(length)
