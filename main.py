import logging
from os import getenv
from addon.dp import init, create_table
from addon.car_commands import show_cars
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv


async def startup(_):
    """
        запускаем дополнительные сервисы
    """
    init()
    create_table()


logger = logging.basicConfig(level=logging.INFO)
load_dotenv()
bot = Bot(getenv('TOKEN_TELEGA'))
dp = Dispatcher(bot, storage=MemoryStorage())


dp.register_message_handler(show_cars, commands=['cars'])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup = startup)