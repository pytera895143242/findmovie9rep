import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

TOKEN = '6172437136:AAH9eE3QJcuBnmu1OFiUNEsp9fE5jIiWTpI'
memory_storage = MemoryStorage()

bot = Bot(token=TOKEN,parse_mode='html',disable_web_page_preview=True)
dp = Dispatcher(bot,storage=memory_storage)
logging.basicConfig(level=logging.INFO)