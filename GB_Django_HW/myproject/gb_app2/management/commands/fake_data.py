from random import randint
import random
from datetime import date, datetime
from django.core.management.base import BaseCommand
from gb_app2.models import User, Product, Order


class Command(BaseCommand):
    help = "Fake data generation User, Product and Order."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of users')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')    # продуктов в два раза больше чем пользователей
        for i in range(1, 2 * count + 1):
            prod = Product(name=f'{generate_rnd_st(5, 7)}',
                           description=f'{generate_rnd_st(50, 70)}',
                           price=randint(5, 600000) / 100,
                           quantity=randint(200, 500),
                           date_added=generate_rnd_date('01.01.10', '29.03.24'),
                           )
            prod.save()
        for i in range(1, count + 1):
            user = User(name=f'{generate_rnd_st(6, 9)}',
                        email=f'{generate_rnd_st(5, 12).lower()}@mail.ru',
                        phone_number=f'+79{randint(100000000, 999999999)}',
                        password=f'{generate_rnd_st(7, 10).lower}',
                        address=f'City: {generate_rnd_st(5, 9)}, St: {generate_rnd_st(4, 10)}, home: {randint(1, 100)}',
                        date=generate_rnd_date('01.01.90', '29.03.24'),
                        )
            user.save()
            for j in range(1, randint(1, 4)):  # Каждый клиент имеет от 0 до 3 заказов
                n = randint(1, 5)  # Количество товаров в каждом заказе от 1 до 5. (к примеру)
                ll = random.sample([i for i in range(1, 2 * count + 1)], n)
                s = 0
                for l in ll:
                    s += Product.objects.filter(pk=l).first().price  # сумма всего заказа
                order = Order(customer=user,      # Здесь обязателен экземпляр User (id(int) - не прокатит)
                              total_price=s,
                              date_ordered=generate_rnd_date('01.01.18', '29.03.24'))
                order.save()     # сначала сохраняем, потом добавляем
                order.products.set(ll)  # Ох, уж эти 'многие-ко-многим'! ... однако, здесь достаточно id-шек


def generate_rnd_date(start='01.01.80', end='28.03.24'):
    """ Генерация случайной даты из заданного диапазона. Формат ввода '%d.%m.%y'"""
    s0 = datetime.strptime(start, '%d.%m.%y').date()
    s1 = datetime.strptime(end, '%d.%m.%y').date()
    return (s1 - s0) * random.random() + s0


def generate_rnd_st(*args):  # для фейковых данных
    """ Генерация случайной строки (латиница, нижний регистр, кроме первой буквы) из случайного количества символов.
        Диапазон задается одной или двумя целыми числами. В случае одного параметра, длина фиксирована
    """
    if len(args) == 0:
        a = b = 5
    elif len(args) == 1:
        a = b = args[0]
    else:
        a, b = args[0], args[1]
    return ''.join([chr(randint(97, 122)) for _ in range(randint(a, b))]).capitalize()