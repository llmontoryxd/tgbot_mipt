"""
Модуль, отвечающий за админ-панель
"""
from django.contrib import admin
from . import models


class WordAdmin(admin.ModelAdmin):
    """
    Класс админ-панели для слов
    """
    list_display = ['pk', 'word', 'translation']
    list_editable = ['word', 'translation']


admin.site.register(models.Words, WordAdmin)
