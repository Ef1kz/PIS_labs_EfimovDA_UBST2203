# Файл: blog/urls.py

from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    # Маршрут для административной панели
    path('admin/', admin.site.urls),

    # Маршрут для главной страницы
    # path('') - соответствует корневому URL (http://127.0.0.1:8000/)
    # views.archive - функция, которая обработает запрос
    # name='archive' - имя маршрута для использования в шаблонах
    path('', views.archive, name='archive'),
]