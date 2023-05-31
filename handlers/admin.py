from aiogram import types, Dispatcher
from config import  bot,ADMINS






async def start_command(message: types.Message):
    # Проверяем, является ли пользователь разрешенным
    if message.from_user.id in ADMINS:
        await message.reply("Привет! Я бот.")
    else:
        await message.reply("Извините, вы не имеете доступа к этому боту.")

# Обработчик всех входящих сообщений
async def handle_all_messages(message: types.Message):
    # Проверяем, является ли пользователь разрешенным
    if message.from_user.id in ADMINS:
        await message.reply("Я получил ваше сообщение.")
    else:
        await message.reply("Извините, вы не имеете доступа к этому боту.")

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
    dp.register_message_handler(start_command,commands=['go'])
    dp.register_message_handler(handle_all_messages)
    