from aiogram import types, Dispatcher
from config import  bot,ADMINS


async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMINS:
            await message.answer("ты не мой босс!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть с ответомна сообщения")
        else:
            await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.answer(
                f'{message.from_user.first_name} кикнул тебя'
                f'{message.reply_to_message.from_user.full_name}'
            )
    else:
        await message.answer('пиши в группу')


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')