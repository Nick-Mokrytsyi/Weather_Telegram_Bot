from aiogram import types
from aiogram.dispatcher.filters import state
from aiogram.dispatcher import FSMContext
from loader import dp
import requests
import datetime
from data import config
from icecream import ic
from handlers.users import testing


@dp.message_handler()
async def get_weather(message: types.Message, state: FSMContext):
    symbol_degree = '\u00b0'
    temp_const = 273.15
    text_message = message.text
    url = config.OMW_URL.format(city=text_message, OMW_TOKEN=config.OMW_TOKEN)
    response = requests.get(url)
    data = response.json()

    data2 = await state.get_data()
    name = data2.get("answer_question_1")


    try:
        city = data['name']
        current_weather = round(data["main"]['temp'] - temp_const)
        country = data["sys"]["country"]
        await message.answer(f"{datetime.datetime.now().strftime('Date: %Y-%m-%d; Time: %H-%M')}\n"
                             f"{name}, "
                             f"the weather in {city}({country}) is {current_weather}{symbol_degree}C,\n")

    except:
        await message.answer("City not found")
