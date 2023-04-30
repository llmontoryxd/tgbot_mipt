from aiogram.dispatcher.filters.state import State, StatesGroup


class GameStates(StatesGroup):
    start = State()
    train_random_choice = State()
    train_all_choice = State()
    add_one_word = State()
    get_word = State()
    print_words = State()
    add_from_file = State()