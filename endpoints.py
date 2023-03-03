'''
list of endpoints here : https://open-api.capital.com
API documantation here: https://capital.com/api-development-guide
'''
import requests
import json
import sys

import pprint
from datetime import datetime
from config import *

#from config import API_KEY, login, password

now = datetime.now() # current date and time
#from config import *

BASE_DEMO_URL = 'https://demo-api-capital.backend-capital.com' 
BASE_LIVE_URL = 'https://api-capital.backend-capital.com'

# print('------WELCOME TO CAPITAL API----------')
# login = input('YOUR LOGIN: ')
# password = input('YOUR PASSWORD: ')
# api_key = input('YOUR API KEY: ')
# if login == 'q' or password == 'q' or api_key == 'q':
#     sys.exit()

#UTC time
utc_datetime  = datetime.utcnow()
dt_now_str = utc_datetime.strftime("%Y-%m-%dT%H:%M:%S")
print(dt_now_str)


#now = datetime.now() # current date and time
#date_time = now.strftime("%Y-%m-%dT%H:%M:%S")
#print("date and time:",date_time)	


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


def account_info():
    '''Returns account preferences'''
    response = session.get(
    URL + '/api/v1/session',
    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )

    print(json.dumps(response.json(), indent=4))


def get_preferences():

    '''Returns account preferences'''
    response = session.get(
        URL + '/api/v1/accounts/preferences',
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )

    print(json.dumps(response.json(), indent=4))

def switch_account():
    '''Switches active accounts, optionally setting the default account'''
    account_id = input('ACCOUNT ID (q to cancel): ')
    if account_id == 'q':
        account_menu()
    response = session.put(
    URL + '/api/v1/session',
    json={"accountId": account_id},
    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
)
    print(json.dumps(response.json(), indent=4))

def account_menu():
    '''Account menu'''
    while True:
        choose = input('\nCHOOSE THE ACTION:\n\t1 - ACCOUNT INFORMATION\n\t2 - ACCOUNT PREFERENCES\n\t3 - SWITCH ACCOUNT\n\tq - BACK TO MENU\n: ')
        if choose == '1':
            account_info()
        elif choose == '2':
            get_preferences()
        elif choose == '3':
            switch_account()
        elif choose == 'q':
            main_menu()
        else:
            print('TRY AGAIN')
            account_menu()

def position_menu():
    pass


def main_menu():
    while True:
        choose = input('\tCHOOSE THE ACTION:\n\t1 - ACCOUNT\n\t2 - POSITIONS\n\tq - QUIT\n: ')
        if choose == '1':
            account_menu()
        elif choose == '2':
            position_menu()
        elif choose == 'q':
            sys.exit()
        else:
            print('TRY AGAIN')
            main_menu()

# if response.status_code == 200:
#     CST = response.headers['CST']
#     X_SECURITY_TOKEN = response.headers['X-SECURITY-TOKEN']

#     print('SUCCESSFULLY')
#     main_menu()
    
# else:
#     print('UNSUCCESSFULLY')
#     print('Please double-check credentials'.upper())
            


#Returns the user's session details and optionally tokens.
#response = session.get(
#    URL + '/api/v1/session',
#    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
#)
#
#pp.pprint(response.json())


#Creates a trading session, obtaining session tokens for subsequent API access.
#def get_encryprion_key():
#    response = session.get(
#        URL + '/api/v1/session/encryptionKey',
#        headers={'X-CAP-API-KEY' : API_KEY}
#        )
#
#    print([response.json()['encryptionKey'], response.json()['timeStamp']])

#Returns the account activity history.
#def get_history_activity_by_dealId(dealID, filter, per_from, per_to) -> str:
#    response = session.get(
#        URL + '/api/v1/history/activity',
#        params = { "detailed": True, "filter": filter, "dealId": dealID, 'from': per_from , 'to': per_to},
#        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}     
#    )
#
#    print(response.json())



#Returns all open positions for the active account. Here the dealId and dealReference values have the 'p_' prefix.
#def list_of_trade_ids():
#    response = session.get(
#    URL + '/api/v1/positions',
#    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
#    )
#   
#    for trade_id in response.json()["positions"]:
#        pp.pprint(trade_id)

#Returns the details of the given markets.
#def find_epic(searchTerm) -> str:
#    response = session.get(
#        URL + f'/api/v1/markets?',
#        params={'searchTerm': searchTerm},
#        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
#    )
#    
#    pp.pprint(response.json())


#Create orders and positions. 
#Please note that when creating the position an order is created first with the 'o_' prefix in the dealReferance parameter.
#Example 1
#def open_position():
#    par = {
#  "direction": "BUY",
#  "epic": "ETHUSD",
#  "guaranteedStop": False,
#  "size": 0.04,
#  }
#    response = session.post(
#        URL + '/api/v1/positions',
#        json=par,
#        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
#    )
#
#    print(response.json())

# Example 2
#body = {
#  "direction": "BUY",
#  "epic": "LTCUSD",
#  "guaranteedStop": True, # or False
#  "size": 1,
#  'stopLevel' : 56.67,
#  "limitLevel": 60,
#}
#
#response = session.post(
#    URL + '/api/v1/positions',
#    json=body,
#    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
#    # You are to find out the CST and X-SECURITY-TOKEN in response.headers
#)
#
#print(response.json())


#Closes one or more positions
def close_position_all(dealId):
    response = session.delete(
    URL + '/api/v1/positions/',
    json={"dealId": dealId},
    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )
    print(response.json())




#Closes all positions
def close_all_positions():
    response = session.get(
    URL + '/api/v1/positions',
    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
    )

    for trade_id in response.json()["positions"]:
        close_position_all(trade_id['position']['dealId'])


#Returns all watchlists belonging to the active account.
#def get_watchlist():
#    response = session.get(
#        URL + '/api/v1/watchlists',
#        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
#    )
#
#    print(response.json())
#
#

#Returns all open working orders for the active account.
#def get_workingorders():
#    response = session.get(
#    URL + '/api/v1/workingorders',
#    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
#    )
#    print(response.json())

#for i in range(3):
#    epic = input('Epic name: ')
#    find_epic(epic)
#open_position()                  
#get_workinggorders()
#close_position('0015421d-0055-311e-0000-000080b4ae04')
#close_all_positions()
#list_of_trade_ids()
#get_watchlist()
#list_of_trade_ids()
#get_encryprion_key()
#get_history_activity_by_dealId('0015421d-0055-311e-0000-000080a5744c', "type==POSITION", '2022-04-25T00:00:00.000', '2022-05-12T00:00:00.000')
#get_preferences()
#close_position('0015421d-0055-311e-0000-000080bb8e38')
#list_of_trade_ids()
#close_all_positions()


#-------------------------------------------------------------------

#Returns historical prices for a particular instrument. 
#By default returns the minute prices within the last 10 minutes.
#def get_prices(epic):
#    response = session.get(
#        URL + f'/api/v1/prices/{epic}',
#        params={'to':  dt_now_str ,'max': 50, 'resolution': 'MINUTE'},
#        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
#    )
#    pp.pprint(response.json())


#Returns an open position for the active account by deal identifier.
#dealId = str(input('Trade ID: '))
#
#response = session.put(
#    URL + f'/api/v1/positions/{dealId}',
#    json={"stopLevel": 50},
#    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
#    # You are to find out the CST and X-SECURITY-TOKEN in response.headers
#)
#
#
#print(response.json())



#Creates an working order.
#body = {
#"direction": "BUY",
#"epic": "BTCUSD",
#"level": 80,
#"size": 1,
#"type": "LIMIT"
#}
#response = session.post(
#    URL + '/api/v1/workingorders',
#    json=body,
#    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
#    # You are to find out the CST and X-SECURITY-TOKEN in response.headers
#)

#print(response.json())


#Returns all open working orders for the active account.
#response = session.get(
#    URL + '/api/v1/workingorders',
#    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
#    # You are to find out the CST and X-SECURITY-TOKEN in response.headers
#)
#
#pp.pprint(response.json())
    




#Deletes an working order.
#def close_orders(dealid):
#    
#    response = session.delete(
#        URL + f'/api/v1/workingorders/{dealid}',
#        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
#        # You are to find out the CST and X-SECURITY-TOKEN in response.headers
#    )
#
#    print(response.json())


#Deletes ALL working order.
#def close_all_orders():
#    response = session.get(
#    URL + '/api/v1/workingorders',
#    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN})
#    # You are to find out the CST and X-SECURITY-TOKEN in response.headers)
#    dealid = response.json()['workingOrders']
#    for i in dealid:
#        close_orders(i['workingOrderData']['dealId'])


#close_orders('000940dd-0055-311e-0000-0000814b744a')
#close_all_orders()
#get_prices('BTCUSD')


response = session.get(
    URL + '/api/v1/session',
    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )

print(response.json()['accountId'])


    