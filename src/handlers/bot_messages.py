from aiogram import Router
from aiogram.types import Message
from client.get_messages import get_message

router = Router()

@router.message()
async def echo_handler(message: Message) -> None:
    await message.answer(await get_message('error'))