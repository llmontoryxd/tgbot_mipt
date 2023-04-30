from aiogram import types
from . app import dp
from . import messages
from . states import GameStates


@dp.message_handler(commands=['start', 'help'], state='*')
async def send_welcome(message: types.Message):
    await message.reply(messages.WELCOME_MESSAGE)
