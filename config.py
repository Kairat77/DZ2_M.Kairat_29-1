from decouple import config, Csv
from aiogram import Bot, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage





TOKEN = config("TOKEN")



storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
ADMINS = config("ADMINS", cast=Csv(post_process=tuple, cast=int))

DICES = ['🎲','🎯','🎳','🎰','⚽','🏀']




