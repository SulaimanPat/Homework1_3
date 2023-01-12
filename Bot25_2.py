from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from decouple import config
import logging

TOKEN = config(TOKEN)

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Салалекум хозяин {message.from_user.first_name}")
    await message.answer("This is an answer method")
    await message.reply("This is a reply method")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)
    question = "Invoker or Shadow fiend?"
    answers = [
        "Invoker",
        "Shadow fiend"
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="1000-7",
        open_period=60,
        reply_markup=markup
    )
@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    question = "Blink Eul ult+?"
    answers = [
        'F9',
        'destroy items']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="U missed timing",
        open_period=60,
    )

@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open("media/mem.png", 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await message.answer(f"{int(message.text) ** 2}")
    else:
        await message.answer(f"{message.text}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)