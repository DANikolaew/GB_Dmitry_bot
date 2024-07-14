import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from botV2.Config.config import BOT_TOKEN  # Убедитесь, что путь корректный
from botV2.handlers import common
from botV2.handlers import dialogue


logging.basicConfig(level=logging.INFO)
logging.info("Main function started")  # Лог для проверки запуска
async def main() -> None:
    # Настройка логирования


    # Инициализация бота и диспетчера
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(common.router)
    #dp.storage = FSMcontext.Storage()  # Настройка хранилища
    dp.include_router(dialogue.router)  # Настройка роутера диалог
    logging.info("Bot and dispatcher initialized")  # Лог для проверки инициализации

    # Удаление вебхука и ожидание завершения всех обновлений
    await bot.delete_webhook(drop_pending_updates=True)
    logging.info("Webhook deleted")  # Лог для проверки удаления вебхука

    try:
        logging.info("Starting polling")
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
    finally:
        logging.info("Stopping bot")
        await bot.session.close()

if __name__ == "__main__":
    logging.info("Starting bot")
    try:
        if sys.platform == "win32":
            asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped manually")
