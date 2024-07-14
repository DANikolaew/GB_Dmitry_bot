import aiohttp
import logging
from aiogram import Bot, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from botV2.Config.config import YOUTUBE_API_KEY, YOUTUBE_API_URL
from botV2.Config.constants import YOUTUBE_CATEGORIES
from botV2.keyboards.keyboards import get_main_keyboard, get_categories_keyboard

router = Router()

# Хэндлер старта бота
@router.message(Command("start"))
async def cmd_start(message: Message):
    logging.info("Received /start command")  # Лог для проверки получения команды /start
    await message.answer(
        "Привет! Я бот, который показывает тренды YouTube по категориям. "
        "Используй /trends, чтобы выбрать категорию.\n" 
        "Используй /help, чтобы получить список доступных команд.",
        reply_markup=get_main_keyboard()
    )

# Хэндлер трендов YouTube по категории
@router.message(Command("trends"))
async def cmd_trends(message: Message):
    logging.info("Received /trends command")  # Лог для проверки получения команды /trends
    await message.answer(
        "Выберите категорию:",
        reply_markup=get_categories_keyboard()
    )

@router.callback_query(lambda c: c.data and c.data.startswith('category_'))
async def process_callback_category(callback_query: types.CallbackQuery, bot: Bot):
    logging.info("Received callback for category")  # Лог для проверки получения callback
    await bot.answer_callback_query(callback_query.id)
    category_id = callback_query.data.split('_')[1]
    category_name = YOUTUBE_CATEGORIES[category_id]

    params = {
        "part": "snippet",
        "chart": "mostPopular",
        "regionCode": "RU",  # Измените на код вашей страны
        "videoCategoryId": category_id,
        "maxResults": 5,
        "key": YOUTUBE_API_KEY
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(YOUTUBE_API_URL, params=params) as response:
            if response.status == 200:
                logging.info("YouTube API request successful")  # Лог для проверки успешного запроса к YouTube API
                data = await response.json()
                trends = data.get('items', [])
                if trends:
                    trend_text = f"Топ-5 трендов YouTube в категории '{YOUTUBE_CATEGORIES[category_id]}':\n\n"
                    for i, trend in enumerate(trends, 1):
                        title = trend['snippet']['title']
                        video_id = trend['id']
                        trend_text += f"{i}. {title}\nhttps://www.youtube.com/watch?v={video_id}\n\n"
                    await bot.send_message(callback_query.from_user.id, trend_text)
                else:
                    await bot.send_message(callback_query.from_user.id, "Не удалось найти тренды для этой категории.")
            else:
                logging.error(f"YouTube API request failed with status {response.status}")  # Лог ошибки запроса к YouTube API
                await bot.send_message(callback_query.from_user.id,
                                       "Извините, не удалось получить тренды. Попробуйте позже.")

# Хэндлер помощи и информации о боте
@router.message(Command("help"))
async def cmd_help(message: Message):
    logging.info("Received /help command")  # Лог для проверки получения команды /help
    help_text = (
        "Вот что я умею:\n"
        "/start - Начать работу с ботом\n"
        "/trends - Показать категории YouTube трендов\n"
        "/dialogue - Пройти диалоговый тест для определения ваших предпочтений контента\n"
    )
    await message.answer(help_text)
