from aiogram import types
from .app import dp, bot
from .keyboard import generate_choice_keyboard
from .states import GameStates
from .data_fetcher import get_random, add_word_to_db
from aiogram.dispatcher import FSMContext
import random
import json
import csv


@dp.message_handler(commands=['add_from_file'], state='*')
async def add_from_file(message: types.Message, state: FSMContext):
    await GameStates.add_from_file.set()
    await message.answer('Пожалуйста, отправь файл для загрузки слов')


@dp.message_handler(state=GameStates.add_from_file, content_types=['document'])
async def get_data_from_file(message: types.Message, state: FSMContext):
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
