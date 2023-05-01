"""
Модуль инициализации приложения-бота
"""
import logging
from . app import dp
from . import commands, print_words, train_random_choice, train_all_choice, \
    add_word_from_kb, add_words_from_file


logging.basicConfig(level=logging.INFO)
