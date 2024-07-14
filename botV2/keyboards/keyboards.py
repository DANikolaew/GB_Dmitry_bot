from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from botV2.Config.constants import YOUTUBE_CATEGORIES

def get_main_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="/start"))
    builder.add(KeyboardButton(text="/trends"))
    builder.add(KeyboardButton(text="/help"))
    builder.add(KeyboardButton(text="/dialogue"))
    return builder.as_markup(resize_keyboard=True)

def get_categories_keyboard():
    builder = InlineKeyboardBuilder()
    for category_id, category_name in YOUTUBE_CATEGORIES.items():
        builder.button(text=category_name, callback_data=f"category_{category_id}")
    builder.adjust(2)  # 2 кнопки в ряд
    return builder.as_markup()