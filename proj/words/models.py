"""
Модуль, отвечающий за созданные модели
"""
from django.db import models


class Words(models.Model):
    """
    Класс модели слов "слово-перевод"
    """

    word = models.CharField(verbose_name='Word', max_length=100)
    translation = models.CharField(verbose_name='Translation', max_length=100)

    def __str__(self):
        """
        Функция вывода объекта класса
        """
        return self.word + ' ' + self.translation
