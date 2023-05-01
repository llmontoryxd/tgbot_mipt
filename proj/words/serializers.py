"""
Модуль, отвечающий за сериалайзеры
"""
from rest_framework import serializers
from . import models


class WordSerializator(serializers.ModelSerializer):
    """
    Класс сериалайзера для слов
    """
    class Meta:
        """
        Мета-данные
        """
        model = models.Words
        fields = ['pk', 'word', 'translation']
