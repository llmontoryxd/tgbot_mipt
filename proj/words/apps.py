"""
Модуль, отвечающий за созданные приложения
"""
from django.apps import AppConfig


class WordsConfig(AppConfig):
    """
    Класс приложения слов
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'words'
