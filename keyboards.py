from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_main_menu():
    builder = InlineKeyboardBuilder()

    builder.button(text="Крутая кнопка", callback_data="cool_button")
    builder.button(text="Некрутая кнопка", callback_data="notcool_button")

    builder.adjust(2)

    return builder.as_markup()