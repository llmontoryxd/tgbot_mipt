"""
Модуль, отвечающий за тренировку случайного слова с выбором ответа
"""
import random
from aiogram import types
from aiogram.dispatcher import FSMContext
from . app import dp, bot
from . keyboard import generate_choice_keyboard
from . states import GameStates
from . data_fetcher import get_random


@dp.message_handler(commands=['train_random_choice'], state='*')
async def train_random(message: types.Message, state: FSMContext):
    """
    Функция, исполняющаяся при вызове команды /train_random_choice.
    Выводит слово и варианты ответа
    """
    await GameStates.train_random_choice.set()
    res = await get_random()
    async with state.proxy() as data:
        data['answer'] = res.get('translation')
        data['word'] = res.get('word')
        data['seed'] = random.randint(1, 100)
        inline_kb = await generate_choice_keyboard(data['answer'],
                                                   data['seed'])
        await message.reply(f"Слово <b>{data['word']}</b>",
                            reply_markup=inline_kb, parse_mode='HTML')


@dp.callback_query_handler(state=GameStates.train_random_choice)
async def button_click_callback(callback_query: types.CallbackQuery,
                                state: FSMContext):
    """
    Функция проверки правильности ответа
    """
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    async with state.proxy() as data:
        if answer == data['answer']:
            await bot.send_message(callback_query.from_user.id,
                                   '<b>Ты молодец!</b>',
                                   parse_mode='HTML')
            await GameStates.start.set()
        else:
            inline_kb = await generate_choice_keyboard(data['answer'],
                                                       data['seed'])
            await bot.send_message(callback_query.from_user.id,
                                   'К сожалению, неправильно...',
                                   reply_markup=inline_kb)
