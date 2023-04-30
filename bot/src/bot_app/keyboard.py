from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, \
    InlineKeyboardButton, InlineKeyboardMarkup

from . data_fetcher import get_all
import random


async def generate_choice_keyboard(answer, seed):
    keyboard_choices = []
    all_words = await get_all()
    random.Random(seed).shuffle(all_words)
    for i in range(4):
        if (all_words[i].get('translation') != answer) and len(keyboard_choices) < 3:
            keyboard_choices.append(all_words[i].get('translation'))
    keyboard_choices.append(answer)
    random.Random(seed).shuffle(keyboard_choices)

    inline_choice_kb = InlineKeyboardMarkup()
    for choice in keyboard_choices:
        inline_choice_kb.add(InlineKeyboardButton(choice,
                                                  callback_data=choice))

    return inline_choice_kb


inline_button_m = InlineKeyboardButton('Masculine', callback_data='m')
inline_button_f = InlineKeyboardButton('Feminine', callback_data='f')
inline_button_n = InlineKeyboardButton('Neuter', callback_data='n')

inline_gender_kb = InlineKeyboardMarkup()
inline_gender_kb.add(inline_button_m)
inline_gender_kb.add(inline_button_f)
inline_gender_kb.add(inline_button_n)