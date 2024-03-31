from random import randint

count = 3

l_contr = []  # список контроля за повторениями (т.к. товар в заказах не должен повторяться, по условию)
for j in range(1, randint(1, 4)):  # Каждый клиент имеет от 0 до 3 заказов
    ll = []
    for _ in range(randint(1, 5)):  # Количество товаров в каждом заказе от 1 до 5. (к примеру)
        l = randint(1, 2 * count)
        while l in ll or l in l_contr:
            l = randint(1, 2 * count)
        ll.append(l)
    l_contr.extend(ll)
    print(ll)