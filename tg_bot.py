import aiohttp
import asyncio
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text

from config import token, login, password, API_KEY
from endpoints import close_all_positions

# Initialize bot and dispatcher
bot = Bot(token=token)
dp = Dispatcher(bot)


BASE_DEMO_URL = 'https://demo-api-capital.backend-capital.com' 

session = requests.Session() # Create session

'''Returns the user's session details and optionally tokens.'''
response = session.post(
    BASE_DEMO_URL + '/api/v1/session',
    json={"encryptedPassword": False, 'identifier': login, 'password': password},
    headers={'X-CAP-API-KEY': API_KEY}
)

CST = response.headers['CST']
X_SECURITY_TOKEN = response.headers['X-SECURITY-TOKEN']

# Define a command handler
@dp.message_handler(commands=['check-account'])
async def send_weather(message: types.Message):

    # Get the city name from the message

    # Make a request to the weather API
        response = session.get(
                BASE_DEMO_URL + '/api/v1/session',
                headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
                )

        account_id = response.json()['accountId']

    # Send a message with the weather information
        await bot.send_message(message.chat.id, f'Your current account id is {account_id}')

# Define a handler for the /start command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Create a button
    button = KeyboardButton(text="Close")

    # Create a keyboard markup with the button
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button)

    # Send a message with the keyboard
    await bot.send_message(message.chat.id, "Hello! Click the button below to continue:", reply_markup=keyboard)

@dp.message_handler(Text(equals="Close"))
async def handle_button_click(message: types.Message):
    button = KeyboardButton(text="Close all positions")

    # Create a keyboard markup with the button
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button)
    await bot.send_message(message.chat.id, "Click the button below to continue:", reply_markup=keyboard)

# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
