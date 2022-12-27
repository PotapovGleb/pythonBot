import json
from aiogram.utils.markdown import hbold, hlink
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from main import get_data_with_selenium
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

API_Token = "5842803741:AAGNnALdjohfxJ6xojvz2JO8840Nz49ZTWc"
bot = Bot(token=API_Token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):


    await message.answer('Введите ссылку на авито: ')

    @dp.message_handler(content_types="text")
    async def get_avito_items(message: types.Message):
        await message.answer('Пожалуйста подождите...')

        get_data_with_selenium(f"{message.text}")

        with open("index_selenium.html", encoding="utf-8") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")

        items = soup.find_all("div", class_="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum")

        for index, item in enumerate(items):
            item = "https://www.avito.ru" + item.find("a").get("href")

            if index % 20 == 0:
                time.sleep(5)

            await message.answer(item)



def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
