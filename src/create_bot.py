from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from decouple import config
import os

# переменные для работы из .env
ADMIN_ID = config("ADMIN_ID")
BOT_TOKEN = config("TOKEN")
HOST = config("HOST")
PORT = int(config("PORT"))
WEBHOOK_PATH = f'/{BOT_TOKEN}'
BASE_URL = config("BASE_URL")

data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
 
# инициализируем бота и диспетчера для работы с ним
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()