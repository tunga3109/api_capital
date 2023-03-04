import aiohttp
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.utils.callback_data import CallbackData
import json


from capitalcom import client_demo, client

from config import token, login, password, API_KEY
from endpoints import close_all_positions

# Initialize bot and dispatcher
bot = Bot(token=token)
dp = Dispatcher(bot)

# Define a command handler
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    demo_account_button = KeyboardButton(text="Live account")
    live_account_button = KeyboardButton(text="Demo account")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(live_account_button, demo_account_button)

    await bot.send_message(message.chat.id, "Hello! Click the button below to continue:", reply_markup=keyboard)

@dp.message_handler(Text(equals="Live account"))
async def live_acc_button_click(message: types.Message):
    cl = client.Client(login, password, API_KEY)
    a = json.loads(cl.all_accounts())
    for acc in a['accounts']:
        acc_id = acc['accountId']
        acc_name = acc['accountName']
        await bot.send_message(message.chat.id, f'{acc_id} - {acc_name}')
    
    button1 = InlineKeyboardButton(text="Button 1", callback_data="button1")
    button2 = InlineKeyboardButton(text="Button 2", callback_data="button2")

    # Create the inline keyboard and add the buttons to it
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button1, button2)

# Send the message with the inline keyboard
    await bot.send_message(message.chat.id, 'Choose the button', reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'button1')
async def handle_button1(callback_query: CallbackQuery):
    await bot.send_message(chat_id=callback_query.from_user.id, text="You pressed button 1")

@dp.message_handler(Text(equals="Demo account"))
async def live_acc_button_click(message: types.Message):
    city_name = message.text.replace('Demo account ', '')
    await bot.send_message(message.chat.id, city_name)
    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
