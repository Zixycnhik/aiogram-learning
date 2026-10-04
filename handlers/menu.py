from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from keyboards import get_main_menu

router = Router()

@router.message(Command("menu"))
async def inline_menu(message: Message):
    await message.answer("Выберите действие:", reply_markup=get_main_menu())

@router.callback_query(F.data == "cool_button")
async def handle_cool_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Вы нажали крутую кнопку", reply_markup=get_main_menu())

@router.callback_query(F.data == "notcool_button")
async def handle_cool_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Вы нажали не крутую кнопку", reply_markup=get_main_menu())
