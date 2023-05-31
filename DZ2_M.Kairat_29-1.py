import asyncio
from aiogram.utils import executor
from config import dp
from handlers import commands, empty_handler, callback, admin, fsm, time
from database import bot_db
import logging


callback.register_hendlers_callback(dp)

fsm.register_handlers_fsm(dp)

commands.register_handlers_commands(dp)


time.register_handlers_notification(dp)
admin.register_handler_admin(dp)

empty_handler.register_hendlers_empty(dp)

async def on_startup(_):
    asyncio.create_task(time.scheduler())
    bot_db.sql_create()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)