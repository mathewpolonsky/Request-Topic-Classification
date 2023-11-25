from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Перезапустить бота')]
], resize_keyboard=True)
