from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def echo_handler(message: Message) -> None:
    await message.copy_to(chat_id=message.chat.id)