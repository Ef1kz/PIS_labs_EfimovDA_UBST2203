# Файл: articles/views.py

from django.shortcuts import render
from .models import Article

def archive(request):
    """
    Представление для отображения архива всех статей

    Args:
        request: Объект HTTP запроса от пользователя

    Returns:
        HttpResponse: HTML страница с архивом статей
    """
    # Получаем все статьи из базы данных
    # Article.objects.all() выполняет SQL: SELECT * FROM articles_article;
    all_articles = Article.objects.all()

    # Создаем контекст - словарь с данными для шаблона
    context = {
        'posts': all_articles  # Ключ 'posts' будет переменной в шаблоне
    }

    # Рендерим шаблон archive.html с переданным контекстом
    # Функция render:
    # 1. Находит шаблон archive.html
    # 2. Заполняет его данными из context
    # 3. Возвращает готовую HTML страницу
    return render(request, 'archive.html', context)