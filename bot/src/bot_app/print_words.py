from aiogram import types
from . app import dp, bot
from . keyboard import inline_gender_kb
from . states import GameStates
from . data_fetcher import get_random, get_next
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=['print_all_words'], state='*')
async def print_all_words(message: types.Message, state: FSMContext):
    await GameStates.print_words.set()
    pk = 0
    print_string = ''
    while True:
        res = await get_next(pk)
        if not res:
            await bot.send_message(message.from_user.id, print_string)
            await GameStates.start.set()
            return
        async with state.proxy() as data:
            data['pk'] = res.get('pk')
            data['answer'] = res.get('gender')
            data['word'] = res.get('word')
            data['translation'] = res.get('translation')
            print_string += f"{data['pk']}) {data['word']} - {data['translation']}\n"
        pk += 1
