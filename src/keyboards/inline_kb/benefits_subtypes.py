from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def create_benefits_some_type_kb(list_values) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    count, num = list_values
    for i in range(1, count + 1):
        builder.add(
            InlineKeyboardButton(
                text = str(i),
                callback_data = f'benefit_name_{num}{i}'
            )
        )
    
    builder.adjust(4)

    builder.row(
        InlineKeyboardButton(
            text = '⬅️ Назад',
            callback_data = 'back'
        )
    )
    return builder.as_markup()

def create_benefits_subtype_kb(benefit_key) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text = 'Содержание',
            callback_data = f'{benefit_key}_content' 
        ),
       InlineKeyboardButton(
            text = 'Нормативные акты',
            callback_data = f'{benefit_key}_acts' 
        ),
        InlineKeyboardButton(
            text = '⬅️ Назад',
            callback_data = 'back'
        )
    )
    builder.adjust(2)
    return builder.as_markup()
