# from random import randint
#
# count = 3
#
# l_contr = []  # список контроля за повторениями (т.к. товар в заказах не должен повторяться, по условию)
# for j in range(1, randint(1, 4)):  # Каждый клиент имеет от 0 до 3 заказов
#     ll = []
#     for _ in range(randint(1, 5)):  # Количество товаров в каждом заказе от 1 до 5. (к примеру)
#         l = randint(1, 2 * count)
#         while l in ll or l in l_contr:
#             l = randint(1, 2 * count)
#         ll.append(l)
#     l_contr.extend(ll)
#     print(ll)
import itertools

def area_triangle(c):
    l1 = ((c[1][0] - c[0][0]) ** 2 + (c[1][1] - c[0][1]) ** 2) ** .5
    l2 = ((c[2][0] - c[0][0]) ** 2 + (c[2][1] - c[0][1]) ** 2) ** .5
    l3 = ((c[2][0] - c[1][0]) ** 2 + (c[2][1] - c[1][1]) ** 2) ** .5
    p = (l1 + l2 + l3) / 2
    return (p * (p - l1) * (p - l2) * (p - l3)) ** .5

# Здесь, понятно, что нужно сделать правильный ввод ...
iterable = ((9, 6), (5, 7), (9, 2), (4, 6), (3, 2), (2, 1), (0, 8), (7, 3), (4, 8), (1, 1))

s, n = 0, 0
for k in itertools.combinations(iterable, 3):
    s += area_triangle(k)
    n += 1

print(s/n)
