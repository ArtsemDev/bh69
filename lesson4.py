# # # # # # numbers = [2, 4, 3, 5, 6, 7, 2, 3, 4]
# # # # # # words = ['hello', 'python', 'world']
# # # # # # letters = list('hello')
# # # # # # numbers2 = [i ** 2 for i in range(1, 101)]
# # # # # #
# # # # # # words[1] = 'pycharm'
# # # # # #
# # # # # # # del numbers[1:3]
# # # # # # # print(numbers)
# # # # # #
# # # # # # # number = numbers.pop(1)
# # # # # # # print(numbers)
# # # # # # # print(number)
# # # # # # # numbers.remove(4)
# # # # # # # print(numbers)
# # # # #
# # # # #
# # # # # # objs = [1, 2, 3, 4, 5]
# # # # # # objs.append(5)
# # # # # # objs.extend('hello')
# # # # # # print(objs)
# # # # # # objs.append(6)
# # # # # # objs.insert(0, 6)
# # # # # # print(objs)
# # # # #
# # # # # # a = [1, 2, 3]
# # # # # # print(a.count(3))
# # # # # # b = [4, 5, 6]
# # # # # # c = a + b
# # # # # # print(c * 2)
# # # # #
# # # # # # numbers = [5, 3, 6, 4, 2, 5, 4, 8, 7, 9, 10]
# # # # # # # numbers.sort(reverse=True)
# # # # # # # print(numbers)
# # # # # # print(sorted(numbers, reverse=True))
# # # # # # print(numbers)
# # # # #
# # # # # # a = [1, 2, 3, 4]
# # # # # # b = list(a)
# # # # # # b = a[:]
# # # # # # b = a.copy()
# # # # # # a.append(5)
# # # # # # print(b)
# # # # # # b = [a, 5, 6, 7]
# # # # # # c = b.copy()
# # # # # # b[0].append(5)
# # # # # # print(a)
# # # # # # print(b)
# # # # # # print(c)
# # # # # # c = 1
# # # # # # a = [1, 2, 3, 4]
# # # # # # b = [1, 2, 3, 4]
# # # # # # print(a == b)
# # # # # # print(a[0] is b[0] is c)
# # # # #
# # # # #
# # # # # # statuses = 200,
# # # # # # print(statuses)
# # # # #
# # # # # # b = [5, 6, 7]
# # # # # # a = (1, 2, 3, 4, b)
# # # # # # a[4].append(8)
# # # # # # print(a)
# # # # # # available_methods = ('get', 'post')
# # # # #
# # # # #
# # # # # # s = set('hello')
# # # # # # print(s)
# # # # #
# # # # # numbers = [-42, 3, 51, 2, 7, 8, 654, 4, 6, 4, 3, 9, 0, 10, 11]
# # # # # numbers = set(numbers)
# # # # # # print(numbers)
# # # # # # print(numbers.isdisjoint({100, 155, 256}))
# # # # # # print(numbers.isdisjoint({100, 155, 256}))
# # # # # a = {1, 2, 3, 4, 5}
# # # # # b = {3, 4, 5, 2, 1, 6, 7}
# # # # # # print(a.issubset(b))
# # # # # # print(a <= b)
# # # # #
# # # # # # c = a.union(b, {77, 88, 99}, 'hello')
# # # # # # print(c)
# # # # # # print(a | b | {77, 88, 99})
# # # # # # print(a.difference(b))
# # # # # # print(a.intersection(b, {55, 66, 3, 4}))
# # # # # print(a & b & {55, 66, 3, 4})
# # # #
# # # #
# # # # data = {
# # # #     'name': 'Alex',
# # # #     'age': 34,
# # # #     'is_human': True
# # # # }
# # # # new_data = {
# # # #     'name': 'Maksim',
# # # #     'city': 'Minsk'
# # # # }
# # # # # res = {**data, **new_data}
# # # # res = data | new_data
# # # # print(data)
# # # # print(new_data)
# # # # print(res)
# # # # # data.update(new_data)
# # # # # print(data)
# # # # # print(data['name'])
# # # # # data['name'] = 'Maksim'
# # # # # data['city'] = 'Minsk'
# # # # # print(data)
# # # #
# # # # # data = dict([('name', 'alex'), ('age', 34), ('city', 'minsk')])
# # # # # print(data)
# # # #
# # # # # data = dict.fromkeys(('name', 'age', 'city'))
# # # # # print(data)
# # # # # print(data['city'])
# # # #
# # # # # print(data.get('name', 'Н/У'))
# # # # # print(data.setdefault('city', 'Н/У'))
# # # # # print(data)
# # # #
# # # # # print(data.pop('city', None))
# # # # # print(data)
# # # #
# # # # # print(list(data))
# # # # # print(data.items())
# # #
# # # # print(sum([1, 2, 3, 4, 5]))
# # # # print(max())
# # # # print(min())
# # #
# # #
# # # # numbers = [(i + 2) ** 3 for i in range(10)]
# # # # print(numbers)
# # #
# # # # numbers = [int(input('enter number: ')) for i in range(3)]
# # # # print(numbers)
# # #
# # # # data = {f'{i}': i ** 2 for i in range(1, 100, 2)}
# # # # print(data)
# # #
# # # # data = (i for i in range(10))
# # # # print(data)
# # #
# # # from collections import *
# # #
# # #
# # # # User = namedtuple('User', ('name', 'age', 'email'))
# # # # vasya = User(name='vasya', age=34, email='vasya@gmail.com')
# # # # # print(vasya.email)
# # # # print(vasya._asdict())
# # #
# # # # words = ('hello', 'python', 'python', 'world')
# # # # c = Counter(words)
# # # # print(c)
# # #
# # # # c1 = Counter('hello python')
# # # # c2 = Counter('hello world')
# # # # # print(c1.most_common(n=4))
# # # # # print(list(c2.elements()))
# # # # # print(c1.total())
# # # # print(c1)
# # # # print(c2)
# # # # # c1.subtract(c2)
# # # # print(c1 - c2)
# # #
# # #
# # # # data = defaultdict(int)
# # # # data['languages'] += 1
# # # # print(data)
# # # data = {
# # #     'a': 1,
# # #     'b': 2,
# # #     'c': 3,
# # #     'd': 4,
# # # }
# # #
# # # data2 = {
# # #     'b': 5,
# # #     'e': 6
# # # }
# # #
# # # chain = ChainMap(data, data2)
# # # # print(chain['e'])
# # # # chain.parents['e'] = 8
# # # # print(chain)
# # # print(chain.maps[-1])
# # from collections import Counter
# #
# # # TODO Заполнить список числами от А до Б с шагом С
# # start = int(input())
# # stop = int(input())
# # step = int(input())
# #
# # numbers = [i for i in range(start, stop, step)]
# # # TODO Вводится предложение, необходимо подсчитать вхождение каждого слова в текст
# # # word_counter = Counter(input().split())
# # text = input().lower().split()
# # c = {i: text.count(i) for i in text}
# # str
#
# data = {
#     'п': 'p',
#     'р': 'r'
# }
# data = str.maketrans(data)
# text = 'привет'
# text = text.translate(data)
# print(text)
