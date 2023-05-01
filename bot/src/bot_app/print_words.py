"""
Модуль, отвечающий за команду, выводяющую все слова на экран
"""
from aiogram.dispatcher import FSMContext
from aiogram import types
from . app import dp, bot
from . states import GameStates
from . data_fetcher import get_next


@dp.message_handler(commands=['print_all_words'], state='*')
async def print_all_words(message: types.Message, state: FSMContext):
    """
    Функция вывода всех слов на экран
    """
    await GameStates.print_words.set()
    pk = 0
    print_string = ''
    while True:
        res = await get_next(pk)
        if not res:
            await bot.send_message(message.from_user.id, print_string,
                                   parse_mode='HTML')
            await GameStates.start.set()
            return
        async with state.proxy() as data:
            data['pk'] = res.get('pk')
            data['answer'] = res.get('gender')
            data['word'] = res.get('word')
            data['translation'] = res.get('translation')
            print_string += f"<b>{data['word']}</b> - " \
                            f"<i>{data['translation']}</i>\n"
        pk += 1
