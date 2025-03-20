from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def start_keyboard():
    buttons = [
        [KeyboardButton(text="Льготы"), KeyboardButton(text="Обратная связь")],
    ]
    keyboard = ReplyKeyboardMarkup(
    keyboard=buttons,
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Воспользуйтесь меню:")
    return keyboard
