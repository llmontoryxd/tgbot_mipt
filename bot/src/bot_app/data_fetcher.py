"""
Модуль, отвечающий за связь бота с базой данных
"""

import aiohttp
from . local_settings import WORDS_API_URL_RANDOM, WORDS_API_URL_GENDER_ALL, \
    WORDS_API_URL_ALL, WORDS_API_URL_ADD


async def get_random():
    """
    Получение рандомного слова из базы данных
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(WORDS_API_URL_RANDOM) as response:
            return await response.json()


async def get_next(pk):
    """
    Получение следующего слова из базы данных

    Параметры:
    pk - первичный ключ текущего слова
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(WORDS_API_URL_GENDER_ALL +
                               '/'+str(pk)) as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def get_all():
    """
    Получение всех слов из базы данных
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(WORDS_API_URL_ALL) as response:
            return await response.json()


async def add_word_to_db(json_data):
    """
    Добавление слова в базу данных. Проверки существования слова не происходит.

    Параметры:
    json_data - данные слово+перевод в формате json
    """
    async with aiohttp.ClientSession() as session:
        async with session.post(WORDS_API_URL_ADD, data=json_data) as response:
            status = response.status
