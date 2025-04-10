from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def create_benefits_type_1_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for i in range(1, 9):
        builder.row(
            InlineKeyboardButton(
                text = str(i),
                callback_data = f'benefit_name_1{i}'
            )
        )
    builder.row(
        InlineKeyboardButton(
            text = '⬅️ Назад',
            callback_data = 'back'
        )
    )
    builder.adjust(4)
    return builder.as_markup()

def create_benefit_type_kb(benefit_key) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text = 'Содержание',
            callback_data = f'{benefit_key}_content' 
        ),
       InlineKeyboardButton(
            text = 'Постановления',
            callback_data = f'{benefit_key}_acts' 
        ),
        InlineKeyboardButton(
            text = '⬅️ Назад',
            callback_data = 'back'
        )
    )
    builder.adjust(2)
    return builder.as_markup()

def create_benefit_type_content() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text = '⬅️ Назад',
            callback_data = 'back'
        )
    )
    builder.adjust(1)
    return builder.as_markup()