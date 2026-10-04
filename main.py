import asyncio

from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers import start, menu, echo

async def main() -> None:
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(echo.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())