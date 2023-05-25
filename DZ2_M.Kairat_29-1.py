from aiogram.utils import executor
from config import dp
from handlers import commands, empty_handler, callback, admin, fsm
import logging


callback.register_hendlers_callback(dp)

fsm.register_handlers_fsm(dp)

commands.register_handlers_commands(dp)

admin.register_handler_admin(dp)

empty_handler.register_hendlers_empty(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)