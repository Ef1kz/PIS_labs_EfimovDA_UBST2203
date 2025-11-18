# Файл: articles/admin.py

from django.contrib import admin
from .models import Article  # Импортируем нашу модель

class ArticleAdmin(admin.ModelAdmin):
    """
    Класс для настройки отображения статей в админ-панели
    """

    # Какие поля показывать в списке статей
    list_display = ('title', 'author', 'get_excerpt', 'created_date')

    # По каким полям можно фильтровать статьи
    list_filter = ('created_date', 'author')

    # По каким полям можно искать статьи
    search_fields = ('title', 'text')

# РЕГИСТРИРУЕМ МОДЕЛЬ В АДМИНКЕ
# Теперь статьи будут видны в административной панели
admin.site.register(Article, ArticleAdmin)