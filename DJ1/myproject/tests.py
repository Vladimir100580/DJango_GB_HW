# b = 0  # левая часть больше правой
# m = 0  # правая часть больше левой
# solv = []
# for z in range(0, 50):
#     for x in range(-50, 0):
#         for y in range(-50, 50):
#             l = 1 + x**2 + x**3 + y**2
#             r = 9*x*y*z
#             if r == l:
#                 solv.append([x, y, z])
#             if l > r:
#                 b += 1
#             else:
#                 m += 1
#
#
# print(solv, b, m)

# t = '67'.add_argument('id', type=int, help='User ID')
# print(t)
from random import randint
import random
from datetime import date, datetime


def generate_rnd_st(*args):  # для фейковых данных
    """ Генерация случайной строки (латиница, нижний регистр, кроме первой буквы) из случайного количества символов.
        Диапазон задается одной или двумя целыми числами. В случае одного параметра, длина фиксирована"""
    if len(args) == 0:
        a = b = 5
    elif len(args) == 1:
        a = b = args[0]
    else:
        a, b = args[0], args[1]
    return ''.join([chr(randint(97, 122)) for _ in range(randint(a, b))]).capitalize()

def generate_rnd_date(start='01.01.80', end='28.03.24'):
    """ Генерация случайной даты из заданного диапазона. Формат ввода '%d.%m.%y'"""
    s0 = datetime.strptime(start, '%d.%m.%y').date()
    s1 = datetime.strptime(end, '%d.%m.%y').date()
    return (s1 - s0) * random.random() + s0


print(generate_rnd_st(2, 9))
print(generate_rnd_date(), type(generate_rnd_date()))


print(random.sample([1, 2, 4, 5], 2))

count = 10
n = randint(1, 5)
l = random.sample([i for i in range(0, 2*count)], n)
print(l)

dic = {1: "one", 2: "two", 3: "three"}
print(dic.get(4))

print(random.sample(['01.06.22', '07.03.24', '01.04.24'], 1))