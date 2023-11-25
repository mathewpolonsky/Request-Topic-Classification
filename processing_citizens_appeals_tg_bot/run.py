import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from config import TOKEN
from application.handlers import main_router


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(main_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
