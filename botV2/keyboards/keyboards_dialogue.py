from aiogram.utils.keyboard import ReplyKeyboardBuilder
from botV2.Config.constants import answer

def dialogue_keyboard():
    builder = ReplyKeyboardBuilder()
    for answer_name in answer:
        builder.button(text=answer_name)
    builder.adjust(3)  # 3 кнопки в ряд
    return builder.as_markup()
