from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ boshlash'),
            KeyboardButton(text='📚 malumot'),
        ],
        [
            KeyboardButton(text='🧮 natijam'),
            KeyboardButton(text='🏆 sovrinlar')
        ],
    ],
    resize_keyboard=True
)