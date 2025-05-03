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

benefit_types = {'list_type_benefits_1': [8, 1], #кол-во льгот и порядковый номер
                 'list_type_benefits_2': [3, 2],
                 'list_type_benefits_3': [1, 3],
                 'list_type_benefits_4': [1, 4],
                 'list_type_benefits_5': [5, 5]
                 }

data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
 
# инициализируем бота и диспетчера для работы с ним
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()