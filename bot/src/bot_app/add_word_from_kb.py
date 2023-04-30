from aiogram import types
from .app import dp, bot
from .keyboard import generate_choice_keyboard
from .states import GameStates
from .data_fetcher import get_random, add_word_to_db
from aiogram.dispatcher import FSMContext
import random
import json


@dp.message_handler(commands=['add_one_word'], state='*')
async def add_one_word(message: types.Message, state: FSMContext):
    await GameStates.add_one_word.set()
    await message.answer('Пожалуйста, напиши слово, которое ты хочешь выучить.')


@dp.message_handler(state=GameStates.add_one_word)
async def add_word(message: types.Message, state: FSMContext):
    await GameStates.get_word.set()
    word = message.text
    async with state.proxy() as data:
        data['word'] = word
    await message.answer(f"Пожалуйста, введите перевод {data['word']} на русский язык")


@dp.message_handler(state=GameStates.get_word)
async def add_translation(message: types.Message, state: FSMContext):
    translation = message.text
    async with state.proxy() as data:
        data_to_db = {}
        data_to_db['word'] = data['word']
        data_to_db['translation'] = translation
        json_data = json.dumps(data_to_db)
        await add_word_to_db(json_data)
        await message.answer('Выполнено!')
        await GameStates.start.set()

