from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from .load_model import classificate_text
from .formated_text import get_formated_text
from .api_requests import classificate_text

main_router = Router()


@main_router.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.answer(
        "Здравствуйте! Добро пожаловать в бота для обработки обращений от граждан",
    )
    await message.answer("Введите обращение")


@main_router.message(F.text)
async def get_classification(message: Message) -> None:
    await message.answer("Вы ввели обращение, обрабатываем его...")
    wait_message = await message.answer("⏳")
    classification_dict = await classificate_text(message.text)
    await wait_message.delete()
    await message.answer(get_formated_text(classification_dict), parse_mode='Markdown')
    await message.answer("Введите обращение")
