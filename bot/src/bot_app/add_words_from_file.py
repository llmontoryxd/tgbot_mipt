"""
Модуль, отвечающий за команду, добавляющую слова из файла
"""
import json
import csv
from aiogram import types
from .app import dp, bot
from .states import GameStates
from .data_fetcher import add_word_to_db


@dp.message_handler(commands=['add_from_file'], state='*')
async def add_from_file(message: types.Message):
    """
    Функция, исполняющаяся при вызове команды /add_from_file
    """
    await GameStates.add_from_file.set()
    await message.answer('Пожалуйста, отправь файл для загрузки слов.\n' +
                         'Его формат должен быть <b>.csv</b>.\n' +
                         'В <b>первой</b> колонке слово на ' +
                         '<b>английском</b>, ' +
                         'во <b>второй</b> - на <b>русском</b>\n' +
                         'Первая строка обязательно должна ' +
                         'содержать название колонок.', parse_mode='HTML')


@dp.message_handler(state=GameStates.add_from_file, content_types=['document'])
async def get_data_from_file(message: types.Message):
    """
    Функция вызова записи данных из файла в базу данных
    """
    file_id = message.document.file_id
    await bot.download_file_by_id(file_id, 'tmp.csv')
    with open('tmp.csv', 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            data_to_db = {}
            data_to_db['word'] = row[0]
            data_to_db['translation'] = row[1]
            json_data = json.dumps(data_to_db)
            await add_word_to_db(json_data)
    await message.answer('Выполнено!')
    await GameStates.start.set()
