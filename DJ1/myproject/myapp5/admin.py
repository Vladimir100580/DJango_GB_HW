import random

from django.contrib import admin
from .models import Category, Product


# для массовых операций
@admin.action(description="Задать случайные значения по количеству")
def rand_quantity(modeladmin, request, queryset):
    queryset.update(quantity=random.randint(1, 100))


@admin.action(description="Сброс всех количеств на 0")  # не забыть добавить в action в ProductAdmin
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):  # Не забываем добавить в регистрацию
    """Список продуктов."""
    list_display = ['name', 'category', 'quantity', 'price']
    ordering = ['category', '-quantity']  # сортировка по приоритету
    list_filter = ['date_added', 'price']  # фильтр
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description) '  # подсказка для search_fields
    actions = [rand_quantity, reset_quantity]

    """Отдельный продукт ."""
    # fields = ['name', 'description', 'category', 'date_added', 'rating']  # не дружит с fieldsets
    readonly_fields = ['date_added', 'rating']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'date_added'],
            }
        ),
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
