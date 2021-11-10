from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, state
from loader import dp
from aiogram import types
from states import Test
import requests
import datetime
from data import config


@dp.message_handler(Command("test_bot"))
async def questions(message: types.Message):
    await message.answer("What is your name?")
    await Test.first()

    @dp.message_handler(state=Test.Q1)
    async def answer_question_1(message: types.Message, state: FSMContext):
        answer_question_1 = message.text

        await state.update_data(
            {
            "answer_question_1": answer_question_1
            }
        )

        await message.answer("What is your current city?")
        await Test.next()

    @dp.message_handler(state=Test.Q2)
    async def answer_question_2(message: types.Message, state: FSMContext):
        data = await state.get_data()
        answer_question_1 = data.get("answer_question_1")
        answer_question_2 = message.text
        await state.update_data({
            "answer_question_1": answer_question_1,
            "answer_question_2": answer_question_2
        })
        await message.answer("Thanks for your answers!!!")
        await message.answer(f"Question - 1: {answer_question_1}")
        await message.answer(f"Question - 2: {answer_question_2}")

        symbol_degree = '\u00b0'
        temp_const = 273.15
        text_message = answer_question_2
        url = config.OMW_URL.format(city=text_message, OMW_TOKEN=config.OMW_TOKEN)
        response = requests.get(url)
        data = response.json()
        try:
            city = data['name']
            current_weather = round(data["main"]['temp'] - temp_const)
            country = data["sys"]["country"]
            await message.answer(f"{datetime.datetime.now().strftime('Date: %Y-%m-%d; Time: %H-%M')}\n"
                                     f"{answer_question_1}, "
                                     f"the weather in {city}({country}) is {current_weather}{symbol_degree}C,\n")

        except:
            await message.answer("City not found")

        await state.reset_state(with_data=False)
