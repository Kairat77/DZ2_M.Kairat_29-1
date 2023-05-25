from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import dp, bot



async def quiz_1(message: types.Message):
    marcap = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Next", callback_data="button")
    marcap.add(button)
    question = "Кто является главной героиней в аниме 'Sailor Moon'"
    answers = [
        "Sakura Kinomoto",
        "Bulma Briefs",
        "Usagi Tsukino",
        "Misato Katsuragi",
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        open_period=15,
        reply_markup=marcap
    )


async def quiz_2(call: types.CallbackQuery):
    marcap = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("Next", callback_data="button_1")
    marcap.add(button_1)
    question = "В каком аниме главный герой является пиратом и путешествует по Grand Line в поисках One Piece?"
    answers = [
        " Naruto",
        "Attack on Titan",
        "One Piece",
        "Dragon Ball Z",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        open_period=15,
        reply_markup=marcap
        
    )
async def quiz_3(call: types.CallbackQuery):
    question = "Какое аниме является адаптацией манги, созданной Масаси Кишимото?"
    answers = [
        "Naruto",
        "Attack on Titan",
        "One Piece",
        "Death Note",
    ]




    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        open_period=15,
        
    )

def register_hendlers_callback(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text="button")
    dp.register_callback_query_handler(quiz_3, text="button_1")