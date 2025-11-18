# Файл: articles/models.py

from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    """
    МОДЕЛЬ СТАТЬИ - представляет таблицу в базе данных
    Каждое поле модели = столбец в таблице базы данных
    """

    # ПОЛЕ ЗАГОЛОВКА - строка максимум 200 символов
    title = models.CharField(
        max_length=200,           # Максимальная длина
        verbose_name="Заголовок"  # Человеко-читаемое имя
    )

    # ПОЛЕ АВТОРА - связь с моделью пользователя
    author = models.ForeignKey(
        User,                     # Связываем с моделью User
        on_delete=models.CASCADE, # При удалении пользователя удалять его статьи
        verbose_name="Автор"
    )

    # ПОЛЕ ТЕКСТА - текст без ограничения длины
    text = models.TextField(
        verbose_name="Текст статьи"
    )

    # ПОЛЕ ДАТЫ - автоматически устанавливается при создании
    created_date = models.DateField(
        auto_now_add=True,        # Автоматически = текущая дата
        verbose_name="Дата создания"
    )

    def __str__(self):
        """
        Метод возвращает строковое представление объекта
        Например: "efimov: Моя первая статья"
        """
        return f"{self.author.username}: {self.title}"

    def get_excerpt(self):
        """
        Метод возвращает краткое описание статьи
        Первые 140 символов + многоточие если текст длинный
        """
        if len(self.text) > 140:
            return self.text[:140] + "..."  # Обрезаем и добавляем "..."
        else:
            return self.text  # Возвращаем как есть если короткий