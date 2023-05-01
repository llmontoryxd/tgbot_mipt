"""
Модуль, отвечающий за стандартные команды
"""
from aiogram import types
from . app import dp
from . import messages


@dp.message_handler(commands=['start', 'help'], state='*')
async def send_welcome(message: types.Message):
    """
    Эхо-команда
    """
    await message.reply(messages.WELCOME_MESSAGE, parse_mode='HTML')
