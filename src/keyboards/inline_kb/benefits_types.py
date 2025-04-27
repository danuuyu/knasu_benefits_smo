from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def create_benefits_types_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text = 'Социальная поддержка',
            callback_data = 'list_type_benefits_1' 
        ),
        InlineKeyboardButton(
            text = 'Трудовые льготы',
            callback_data = 'list_type_benefits_2'
        ),
        InlineKeyboardButton(
            text = 'Образовательные льготы',
            callback_data = 'list_type_benefits_3'
        ),
        InlineKeyboardButton(
            text = 'Жилищные льготы',
            callback_data = 'list_type_benefits_4'
        ),
        InlineKeyboardButton(
            text = 'Иные льготы',
            callback_data = 'list_type_benefits_5'
        )
    )
    builder.adjust(1)
    return builder.as_markup()

def create_benefit_type_back() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text = '⬅️ Назад',
            callback_data = 'back'
        )
    )
    builder.adjust(1)
    return builder.as_markup()