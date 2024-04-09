from django.shortcuts import render
from django.db.models import Sum
from myapp5.models import Product


def total_in_db(request):  # Оказался самым быстрым
    total = Product.objects.aggregate(Sum('quantity'))  # метод агрегиованны запросов к БД
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)  # сумма по столбцу количество
    context = {
        'title': 'Общее количество посчитано в представлении',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


def total_in_template(request):  # пусть модель и шаблон сами поработают
    context = {
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product,
    }
    return render(request, 'myapp6/total_count.html', context)
