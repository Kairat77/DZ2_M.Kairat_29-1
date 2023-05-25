from aiogram import types, Dispatcher
from config import dp, bot, DICES
import random


async def echo(message: types.Message):
    bad_words = ['буратина', 'козел', 'дурак']
    user = f"@{message.from_user.username} "\
      if message.from_user.username else message.from_user.full_name
    for word in bad_words:
        if word in message.text.lower().replace(' ',''):
            await message.delete()
            await message.answer(f"не матерись @{user}, сам ты {word} ")


    
async def pin(message:types.Message):
    if message.chat != 'private':
        if not message.reply_to_message:
            await message.answer('команда должна быть ответом')
        else:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.answer('пиши в группу')


    # if message.text =='game':
    #     await bot.send_dice(message.chat.id, emoji='🎲' )
async def dice(message: types.Message):
    await bot.send_dice(message.chat.id, emoji=random.choice(DICES))

            
def register_hendlers_empty(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'],commands_prefix='!/')
    dp.register_message_handler(dice, commands=['game'])
    dp.register_message_handler(echo)

