import aiohttp
import asyncio
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import token, login, password, API_KEY

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

# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
