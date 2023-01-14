from pickle import NONE
from tkinter.messagebox import NO
import telebot
from config import *
from telebot import types
import requests
from endpoints import *
#from encrypted_pass import encryptPassword

URL = 'https://demo-api-capital.backend-capital.com' #base url
        
# Create session
session = requests.Session()

# Returns the user's session details and optionally tokens.
response = session.post(
    URL + '/api/v1/session',
    json={'identifier': login, 'password': password},
    headers={'X-CAP-API-KEY': API_KEY}
)

CST = response.headers['CST']
X_SECURITY_TOKEN = response.headers['X-SECURITY-TOKEN']

#print(response.status_code)
#print(type(response.json()['accountType']))

response = session.get(
    URL + '/api/v1/positions',
    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
    )
list_of_trade_ids = []
for trade_id in response.json()["positions"]:
        info = f"{trade_id['market']['instrumentName']} | {trade_id['position']['dealId']}"
        list_of_trade_ids.append(info)



bot = telebot.TeleBot(token)

#@bot.message_handler(content_types=['text'])
#def start_message(message):
#	bot.send_message(message.chat.id,message.text)
        

@bot.message_handler(commands=['start'])
def button_message(message):	

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

        close_position = types.KeyboardButton(text='Закрыть все позиции')
        keyboard.add(close_position)

        close_one_position = types.KeyboardButton(text='Закрыть позицию')
        keyboard.add(close_one_position)

        positions = types.KeyboardButton(text='Открытые позиции')
        keyboard.add(positions)

        bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=keyboard)                  
    

@bot.message_handler(content_types='text')
def message_reply(mes):

        if mes.text == 'Закрыть все позиции':
                close_all_positions()

                for trade_id in list_of_trade_ids:
                        bot.send_message(mes.from_user.id, text=f'the position {trade_id} has been closed', reply_markup=None)
                list_of_trade_ids.clear()

        
        elif mes.text == 'Открытые позиции':

                for trade_id in list_of_trade_ids:
                        bot.send_message(mes.chat.id, text=f'{trade_id} \n ', reply_markup=None)


                if len(list_of_trade_ids) == 0:
                        bot.send_message(mes.chat.id, text='You have no positions', reply_markup=None)
                                

        elif mes.text == 'Закрыть позицию':
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                
                if len(list_of_trade_ids) == 0:
                        bot.send_message(mes.chat.id, text='You have no positions', reply_markup=None)

                for trade_id in list_of_trade_ids:
                        
                        positions = types.KeyboardButton(text=trade_id)
                        keyboard.add(positions)
                        bot.send_message(mes.from_user.id, text='Close the position', reply_markup=keyboard)
                        

bot.polling(none_stop=True)

