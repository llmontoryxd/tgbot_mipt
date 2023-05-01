"""
Модуль, отвечающий за создание inline-клавиатуры
"""

import random
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from . data_fetcher import get_all


async def generate_choice_keyboard(answer, seed):
    """
    Функция создания клавиатуры выбора по правильному ответу и случайному сиду
    """
    keyboard_choices = []
    all_words = await get_all()
    random.Random(seed).shuffle(all_words)
    for i in range(4):
        if (all_words[i].get('translation') != answer) and \
                len(keyboard_choices) < 3:
            keyboard_choices.append(all_words[i].get('translation'))
    keyboard_choices.append(answer)
    random.Random(seed).shuffle(keyboard_choices)

    inline_choice_kb = InlineKeyboardMarkup()
    for choice in keyboard_choices:
        inline_choice_kb.add(InlineKeyboardButton(choice,
                                                  callback_data=choice))

    return inline_choice_kb
