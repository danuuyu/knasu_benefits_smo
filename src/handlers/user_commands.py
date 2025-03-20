from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from client.get_messages import get_message
from keyboards.reply_kb.start_kb import start_keyboard

router = Router()

# функция для реагирования на команду /start
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(await get_message('start_message'),
                         reply_markup=start_keyboard())
