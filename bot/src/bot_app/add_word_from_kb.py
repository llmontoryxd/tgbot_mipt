"""
Модуль, отвечающий за команду, добавляющую одно слово с клавиатуры пользователя
"""
import json
from aiogram import types
from aiogram.dispatcher import FSMContext
from .app import dp
from .states import GameStates
from .data_fetcher import add_word_to_db


@dp.message_handler(commands=['add_one_word'], state='*')
async def add_one_word(message: types.Message):
    """
    Функция, исполняющаяся при вызове команды /add_one_word
    """
    await GameStates.add_one_word.set()
    await message.answer('Пожалуйста, напиши слово, которое ты ' +
                         'хочешь выучить ' +
                         '(<b>на английском)</b>.', parse_mode='HTML')


@dp.message_handler(state=GameStates.add_one_word)
async def add_word(message: types.Message, state: FSMContext):
    """
    Функция, считывающая перевод
    """
    await GameStates.get_word.set()
    word = message.text
    async with state.proxy() as data:
        data['word'] = word
    await message.answer("Пожалуйста, введите перевод " +
                         f"<b>{data['word']}</b> " +
                         "на <b>русский язык</b>", parse_mode='HTML')


@dp.message_handler(state=GameStates.get_word)
async def add_translation(message: types.Message, state: FSMContext):
    """
    Функция вызова записи слова в базу данных
    """
    translation = message.text
    async with state.proxy() as data:
        data_to_db = {}
        data_to_db['word'] = data['word']
        data_to_db['translation'] = translation
        json_data = json.dumps(data_to_db)
        await add_word_to_db(json_data)
        await message.answer('Выполнено!')
        await GameStates.start.set()
