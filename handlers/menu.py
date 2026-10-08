from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from keyboards import get_main_menu
from database import add_click, get_clicks

router = Router()

@router.message(Command("menu"))
async def inline_menu(message: Message):
    await message.answer("Выберите действие:", reply_markup=get_main_menu())

@router.callback_query(F.data == "cool_button")
async def handle_cool_button(callback: CallbackQuery):
    await add_click(callback.from_user.id, "cool_button")
    count = await get_clicks(callback.from_user.id, "cool_button")
    await callback.answer()
    await callback.message.edit_text(
        f"Вы нажали крутую кнопку! Всего нажатий: {count}",
        reply_markup=get_main_menu(),
    )

@router.callback_query(F.data == "notcool_button")
async def handle_cool_button(callback: CallbackQuery):
    await add_click(callback.from_user.id, "notcool_button")
    count = await get_clicks(callback.from_user.id, "notcool_button")
    await callback.answer()
    await callback.message.edit_text(
        f"Вы нажали не крутую кнопку! Всего нажатий: {count} ",
        reply_markup=get_main_menu(),
    )
