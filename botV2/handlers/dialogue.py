from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from botV2.Config.constants import answer
from botV2.keyboards.keyboards import get_main_keyboard
from botV2.keyboards.keyboards_dialogue import dialogue_keyboard
from aiogram.filters import Command
import logging

router = Router()

class AnswerUser(StatesGroup):
    question1 = State()
    question2 = State()
    question3 = State()
    question4 = State()
    question5 = State()
    question6 = State()
    question7 = State()
    question8 = State()
    question9 = State()
    question10 = State()

@router.message(Command("dialogue"))
async def cmd_answer1(message: types.Message, state: FSMContext):
    logging.info("Starting dialogue")
    await message.answer(
        text="Давайте пройдем тест:\n"
        "Вопрос 1:\n"
        "Смотрите ли вы фильмы и анимацию на YouTube?",
        reply_markup=dialogue_keyboard()
    )
    await state.set_state(AnswerUser.question1)

@router.message(AnswerUser.question1)
async def cmd_answer2(message: types.Message, state: FSMContext):
    logging.info(f"Answer 1 received: {message.text}")
    if message.text not in answer:
        await message.answer("Пожалуйста, выберите один из предложенных вариантов.")
        return
    await state.update_data(question1=message.text)
    await message.answer(
        text="Вопрос 2:\n"
        "Интересуют ли вас видеоролики про автомобили и транспорт?",
        reply_markup=dialogue_keyboard()
    )
    await state.set_state(AnswerUser.question2)

@router.message(AnswerUser.question2)
async def cmd_answer3(message: types.Message, state: FSMContext):
    logging.info(f"Answer 2 received: {message.text}")
    if message.text not in answer:
        await message.answer("Пожалуйста, выберите один из предложенных вариантов.")
        return
    await state.update_data(question2=message.text)
    await message.answer(
        text="Вопрос 3:\n"
        "Любите ли вы слушать музыку на YouTube?",
        reply_markup=dialogue_keyboard()
    )
    await state.set_state(AnswerUser.question3)

@router.message(AnswerUser.question3)
async def cmd_answer4(message: types.Message, state: FSMContext):
    logging.info(f"Answer 3 received: {message.text}")
    if message.text not in answer:
        await message.answer("Пожалуйста, выберите один из предложенных вариантов.")
        return
    await state.update_data(question3=message.text)
    await message.answer(
        text="Вопрос 4:\n"
        "Смотрите ли вы спортивные видео и трансляции на YouTube?",
        reply_markup=dialogue_keyboard()
    )
    await state.set_state(AnswerUser.question4)

@router.message(AnswerUser.question4)
async def cmd_answer5(message: types.Message, state: FSMContext):
    logging.info(f"Answer 4 received: {message.text}")
    if message.text not in answer:
        await message.answer("Пожалуйста, выберите один из предложенных вариантов.")
        return
    await state.update_data(question4=message.text)
    await message.answer(
        text="Вопрос 5:\n"
        "Интересует ли вас игровой контент на YouTube?",
        reply_markup=dialogue_keyboard()
    )
    await state.set_state(AnswerUser.question5)

@router.message(AnswerUser.question5)
async def cmd_answer6(message: types.Message, state: FSMContext):
    logging.info(f"Answer 5 received: {message.text}")
    if message.text not in answer:
        await message.answer("Пожалуйста, выберите один из предложенных вариантов.")
        return
    await state.update_data(question5=message.text)
    await message.answer(
        text="Вопрос 6:\n"
        "Нравятся ли вам комедийные видео на YouTube?",
        reply_markup=dialogue_keyboard()
    )
    await state.set_state(AnswerUser.question6)

@router.message(AnswerUser.question6)
async def cmd_answer7(message: types.Message, state: FSMContext):
    logging.info(f"Answer 6 received: {message.text}")
    if message.text not in answer:
        await message.answer("Пожалуйста, выберите один из предложенных вариантов.")
        return
    await state.update_data(question6=message.text)
    await message.answer(
        text="Вопрос 7:\n"
        "Смотрите ли вы развлекательный контент на YouTube?",
        reply_markup=dialogue_keyboard()
    )
    await state.set_state(AnswerUser.question7)

@router.message(AnswerUser.question7)
async def cmd_answer8(message: types.Message, state: FSMContext):
    logging.info(f"Answer 7 received: {message.text}")
    if message.text not in answer:
        await message.answer("Пожалуйста, выберите один из предложенных вариантов.")
        return
    await state.update_data(question7=message.text)
    await message.answer(
        text="Вопрос 8:\n"
        "Интересуют ли вас новости и политические видео на YouTube?",
        reply_markup=dialogue_keyboard()
    )
    await state.set_state(AnswerUser.question8)

@router.message(AnswerUser.question8)
async def cmd_answer9(message: types.Message, state: FSMContext):
    logging.info(f"Answer 8 received: {message.text}")
    if message.text not in answer:
        await message.answer("Пожалуйста, выберите один из предложенных вариантов.")
        return
    await state.update_data(question8=message.text)
    await message.answer(
        text="Вопрос 9:\n"
        "Смотрите ли вы видео по хобби и стилю жизни на YouTube?",
        reply_markup=dialogue_keyboard()
    )
    await state.set_state(AnswerUser.question9)

@router.message(AnswerUser.question9)
async def cmd_answer10(message: types.Message, state: FSMContext):
    logging.info(f"Answer 9 received: {message.text}")
    if message.text not in answer:
        await message.answer("Пожалуйста, выберите один из предложенных вариантов.")
        return
    await state.update_data(question9=message.text)
    await message.answer(
        text="Вопрос 10:\n"
        "Интересуют ли вас научные и технологические видео на YouTube?",
        reply_markup=dialogue_keyboard()
    )
    await state.set_state(AnswerUser.question10)

@router.message(AnswerUser.question10)
async def cmd_finish_test(message: types.Message, state: FSMContext):
    logging.info(f"Answer 10 received: {message.text}")
    if message.text not in answer:
        await message.answer("Пожалуйста, выберите один из предложенных вариантов.")
        return
    await state.update_data(question10=message.text)
    user_data = await state.get_data()

    def get_emoji(response):
        emojis = {
            "Точно нет": "🔴",
            "Скорее всего нет": "🟠",
            "Не знаю": "🟡",
            "Скорее всего да": "🟢",
            "Да": "🟢"
        }
        return emojis.get(response, "")

    result_text = (
        f"Ваш результат:\n"
        f"1. Фильмы и анимации: {get_emoji(user_data['question1'])}\n"
        f"2. Автомобили и транспорт: {get_emoji(user_data['question2'])}\n"
        f"3. Музыка: {get_emoji(user_data['question3'])}\n"
        f"4. Спорт: {get_emoji(user_data['question4'])}\n"
        f"5. Игровой контент: {get_emoji(user_data['question5'])}\n"
        f"6. Комедийные видео: {get_emoji(user_data['question6'])}\n"
        f"7. Развлекательный контент: {get_emoji(user_data['question7'])}\n"
        f"8. Новости и политика: {get_emoji(user_data['question8'])}\n"
        f"9. Хобби и стиль жизни: {get_emoji(user_data['question9'])}\n"
        f"10. Наука и технологии: {get_emoji(user_data['question10'])}\n"
    )

    await message.answer(text=result_text, reply_markup=get_main_keyboard() )
    await state.clear()
