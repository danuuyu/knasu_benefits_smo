from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def start_keyboard():
    buttons = [
        [KeyboardButton(text="Льготы")],
    ]
    keyboard = ReplyKeyboardMarkup(
    keyboard=buttons,
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Воспользуйтесь меню:")
    return keyboard
