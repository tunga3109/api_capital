'''
list of endpoints here : https://open-api.capital.com
API documantation here: https://capital.com/api-development-guide
'''

'''
Here you should simply use the POST/session endpoint and mention the received 
in the platform's Settings API key in the X-CAP-API-KEY header, login and password info in the identifier and password parameters.
'''
import requests
import pprint
import sys
import json

from config import *
from datetime import date, datetime
import time

#UTC time
utc_datetime  = datetime.utcnow()
dt_now_str = utc_datetime.strftime("%Y-%m-%dT%H:%M:%S")
time_now_str = utc_datetime.strftime("%H:%M:%S")

BASE_DEMO_URL = 'https://demo-api-capital.backend-capital.com' 
BASE_LIVE_URL = 'https://api-capital.backend-capital.com'

session = requests.Session() # Create session

'''Returns the user's session details and optionally tokens.'''

response = session.post(
    BASE_DEMO_URL + '/api/v1/session',
    json={"encryptedPassword": False, 'identifier': login, 'password': password},
    headers={'X-CAP-API-KEY': API_KEY}
)

CST = response.headers['CST']
X_SECURITY_TOKEN = response.headers['X-SECURITY-TOKEN']

pp = pprint.PrettyPrinter(indent=4)

def logging(func):

    def wrapper():
        from datetime import datetime
        start = datetime.now().time()
        end = datetime.now().time()
        print(f'Start function {start}')
        func()
        print(f'End function {end}')
    return wrapper


'''Check the account information'''
@logging
def check_acc_info():
    response = session.get(
        BASE_DEMO_URL + '/api/v1/accounts',
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )

    pp.pprint(response.json())



'''Place the trade'''
trade_body = {
  "direction": "BUY",
  "epic": "LTCUSD", 
  "guaranteedStop": False, # or False
  "size": 1, #Numbers - without quotes
  'stopLevel' : 48.67, #Stop loss price. Numbers - without quotes
   } #Take profit price. Numbers - without quotes




def place_the_trade(body):
    response = session.post(
        BASE_DEMO_URL + '/api/v1/positions',
        json=body,
        headers={
            'CST': CST, 
            'X-SECURITY-TOKEN': X_SECURITY_TOKEN,
            } 
        # You are to find out the CST and X-SECURITY-TOKEN in response.headers()
    )
    print(response.json())



'''Update the trade'''
#update_body = {
#  "epic": "LTCUSD", 
#  "guaranteedStop": False,
#  "stopLevel" : 50.67, #Stop loss price. Numbers - without quotes
#  "profitLevel": 64} #Take profit price. Numbers - without quotes

def update_the_trade(body):
    dealID = input('Paste Deal ID: ')
    if dealID == 'q':
        sys.exit()
    else:
        response = session.put(
            BASE_DEMO_URL + f'/api/v1/positions/{dealID}',
            json=body,
            headers={
                'CST': CST, 
                'X-SECURITY-TOKEN': X_SECURITY_TOKEN,}
            # You are to find out the CST and X-SECURITY-TOKEN in response.headers()
        )
        print(response.json())



'''Check the trade by Deal Reference'''
def check_trade_by_deal_ref():
    dealReference = input('Please paste the DealReference: ')
    if dealReference == 'q':
        sys.exit()
    else:
        response = session.get(
            BASE_DEMO_URL + f'/api/v1/confirms/{dealReference}',
            headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
        )
    
        if len(response.json()['affectedDeals']) == 0:
            status = response.json()['dealStatus']
            print(f'The order was {status}')



'''Check all opened trades'''
def list_of_trades():
    print('-' * 5, 'Check all opened trades', '-' * 5)
    response = session.get(
        BASE_DEMO_URL + '/api/v1/positions',
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
        )

    #print(json.dumps(response.json()['positions'], indent=4))
    for trade in response.json()['positions']:
        dealid = trade['position']['dealId']
        instrument_name = trade['market']['instrumentName']
        print(f'{instrument_name} - {dealid}')

    #print(type(response.json()['positions']))
    #for trade in r['positions']:
    #    #pp.pprint(f'{trade["market"]["instrumentName"]} - {trade["position"]["dealId"]} - {trade["market"]["updateTime"]}')
    #    print(trade["position"]["dealId"])
    




'''Check opened trades'''
def check_trade():
    deal_id = input('Please paste the dealID: ')
    if deal_id == 'q':
        sys.exit()
    else:
        response = session.get(
            BASE_DEMO_URL + f'/api/v1/positions/{deal_id}',
            headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
        )

        pp.pprint(response.json())




'''Close the trade'''
def close_trade():
    deal_id = input('Please paste the dealID: ')
    if deal_id == 'q':
        sys.exit()
    else:
        response = session.delete(
            BASE_DEMO_URL + '/api/v1/positions/',
            json={"dealId": deal_id},
            headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
            )

        pp.pprint(response.json())

'''Search epics'''
def search_epic():
    epic_name = input('Paste the epic name: ')
    response = session.get(
        BASE_DEMO_URL + '/api/v1/markets',
        params={'searchTerm': epic_name},
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )


    for data in response.json()["markets"]:
        instrument_name = data['instrumentName']
        epic = data['epic']

        print(f'{instrument_name}|{epic}')

'''Checking single watchlist'''
def check_watchlist_by_id():
    watchlist_id = input('watchlist ID: ')
    response = session.get(
        BASE_DEMO_URL + f'/api/v1/watchlists/{watchlist_id}',
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )

    pp.pprint(response.json())

'''Create watchlist'''

def create_watchlist():
    how_much = int(input('How muck epics do you want to add: '))
    epic_list = []
    for epic in range(how_much):
        epic_name = input('epic name: ')
        epic_list.append(epic_name)
    name = input('watchlist name: ')
    response = session.post(
        BASE_DEMO_URL + '/api/v1/watchlists',
        json={'epics': epic_list, 'name': name},
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )

    pp.pprint(response.json())

'''Check all watchlists'''
def check_watchlists():
    response = session.get(
        BASE_DEMO_URL + '/api/v1/watchlists/',
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )

    pp.pprint(response.json())

'''Update watchlist'''
def update_watchlist():
    watchlist_id = input('watchlist ID: ')
    how_much = int(input('How muck epics do you want to add: '))
    for i in range(how_much):
        epic_name = input('epic name: ')
        response = session.put(
            BASE_DEMO_URL + f'/api/v1/watchlists/{watchlist_id}',
            headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN},
            json={'epic': epic_name} 
        )

        pp.pprint(response.json())

'''Delete watchlist'''
def delete_watchlist():
    watchlist_id = input('watchlist ID: ')
    response = session.delete(
        BASE_DEMO_URL + f'/api/v1/watchlists/{watchlist_id}',
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}, 
    )

    pp.pprint(response.json())


def get_prices():
    epic_name = input('Paste the epic name: ')
    response = session.get(
        BASE_DEMO_URL + f'/api/v1/prices/{epic_name}',
        params={'to': dt_now_str , 'resolution': 'MINUTE'},
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
    )

    pp.pprint(response.json())

    #for data in response.json()['prices']:
    #    print(data)


if __name__ == '__main__':
    #place_the_trade(trade_body)
    check_trade_by_deal_ref()
    #close_trade()



#import matplotlib.pyplot as plt
#
#xdata = []
#ydata = []
#
#fig = plt.figure()
#ax = fig.add_subplot(111)
#fig.show()
#
#def show_graf():
#    plt.plot(xdata, ydata)
#    fig.canvas.draw()
#    plt.pause(1)
#
#def get_live_prices():
#    epic_name = input('Paste the epic name: ')
#    while True:
#        response = session.get(
#            BASE_DEMO_URL + '/api/v1/markets',
#            params={'searchTerm': epic_name},
#            headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
#        )
#        
#        upd_time = response.json()['markets'][0]['updateTime'][:-4]
#        price = response.json()['markets'][0]['offer']
#
#
#        xdata.append(upd_time)
#        ydata.append(price)
#        show_graf()
#
#        print(f'{upd_time} -> {price}')
