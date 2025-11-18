from django.shortcuts import render

# Create your views here.
# Файл: flatpages/views.py

# Импортируем класс HttpResponse для создания HTTP-ответов
from django.shortcuts import render

def home(request):
    """Главная страница - теперь использует static_handler.html"""
    return render(request, 'static_handler.html')  # Изменено с index.html на static_handler.html

def old_version(request):
    """Страница со старой версией (index.html)"""
    return render(request, 'index.html')