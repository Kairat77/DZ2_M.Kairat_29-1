
from aiogram import types, Dispatcher
from config import  bot
from aiogram import types
import requests



async def start(message: types.Message):
    await message.answer(f"Salam {message.from_user.full_name}")




async def mem_command_handler(message:types.Message):
    response = requests.get("https://picsum.photos/200/300") 
    if response.status_code == 200:
        image_url = response.url
       
        await bot.send_photo(message.chat.id, image_url)
    else:
        await message.answer("Произошла ошибка при получении изображения.")

def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'anime'])
    dp.register_message_handler(mem_command_handler, commands=['mem'])
    