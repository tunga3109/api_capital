'''
list of endpoints here : https://open-api.capital.com
API documantation here: https://capital.com/api-development-guide
'''
import requests
import json
import sys

from config import *

BASE_DEMO_URL = 'https://demo-api-capital.backend-capital.com' 
BASE_LIVE_URL = 'https://api-capital.backend-capital.com'

print('------WELCOME TO CAPITAL API----------')

# login = input('YOUR LOGIN: ')
# password = input('YOUR PASSWORD: ')
# api_key = input('YOUR API KEY: ')
# if login == 'q' or password == 'q' or api_key == 'q':
#     sys.exit()
        
'''Create session'''
session = requests.Session()

'''Returns the user's session details and optionally tokens.'''
response = session.post(
    BASE_DEMO_URL + '/api/v1/session',
    json={'identifier': login, 'password': password},
    headers={'X-CAP-API-KEY': API_KEY}
)

'---------------------------------------------------------------------'

def account_info():
    '''Returns account preferences'''
    response = session.get(
    BASE_DEMO_URL + '/api/v1/session',
    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )

    print(json.dumps(response.json(), indent=4))


def get_preferences():
    '''Returns account preferences'''
    response = session.get(
        BASE_DEMO_URL + '/api/v1/accounts/preferences',
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )

    print(json.dumps(response.json(), indent=4))


def switch_account():
    '''Switches active accounts, optionally setting the default account'''
    account_id = input('ACCOUNT ID (q to cancel): ')
    if account_id == 'q':
        account_menu()
    response = session.put(
    BASE_DEMO_URL + '/api/v1/session',
    json={"accountId": account_id},
    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
)
    print(json.dumps(response.json(), indent=4))
    

def accounts():
    '''Returns a list of accounts belonging to the logged-in client'''
    response = session.get(
        BASE_DEMO_URL + '/api/v1/accounts',
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )

    print(json.dumps(response.json(), indent=4))


def log_out():
    '''Log out of the current session'''
    response = session.delete(
        BASE_DEMO_URL + '/api/v1/session',
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )

    print(json.dumps(response.json(), indent=4))


'--------------------------------------------------------------'
def open_position(body):
    '''Create orders and positions'''
    response = session.post(
        BASE_DEMO_URL + '/api/v1/positions',
        json=body,
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
    )

    dealid = response.json()["dealReference"]
    check_trade_by_deal_ref(dealid)
# ---

def check_trade_by_deal_ref(dealReference):
    response = session.get(
        BASE_DEMO_URL + f'/api/v1/confirms/{dealReference}',
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
    )

    if len(response.json()['affectedDeals']) == 0:

        status = response.json()['dealStatus']
        print(f'The order was {status}')
    else:
        print(response.json()['affectedDeals'])

# ---

def check_trade():
    '''Returns an open position for the active account by deal identifier'''
    deal_id = input('PASTE THE TRADE ID (q to cancel): ')
    if deal_id == 'q':
        position_menu()
    else:
        response = session.get(
            BASE_DEMO_URL + f'/api/v1/positions/{deal_id}',
            headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
        )

        print(json.dumps(response.json(), indent=4))
# -----
def list_of_trades():
    '''Returns all open positions for the active account'''   
    response = session.get(
        BASE_DEMO_URL + '/api/v1/positions',
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
        )

    if len(response.json()["positions"]) == 0:
        print('There are no positions')
    else:
        print(json.dumps(response.json(), indent=4))
# ----
def update_the_trade(body):
    '''Update the position'''
    dealID = input('PASTE THE TRADE ID (q to cancel): ')
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
# ----
def close_position():
    '''Close the position'''
    dealId = input('PASTE THE TRADE ID (q to cancel): ')
    if dealId == 'q':
        position_menu()
    response = session.delete(
    BASE_DEMO_URL + '/api/v1/positions/',
    json={"dealId": dealId},
    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )
    print(response.json())
# ----

def close_position_all(dealId):
    response = session.delete(
    BASE_DEMO_URL + '/api/v1/positions/',
    json={"dealId": dealId},
    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )
    print(response.json())
# ---
def close_all_positions():
    '''Close all postions'''
    response = session.get(
    BASE_DEMO_URL + '/api/v1/positions',
    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
    )

    for trade_id in response.json()["positions"]:
        close_position_all(trade_id['position']['dealId'])

# ---------
def body():
    print('type \'q\' to quit '.upper())
    body_dict = {}
    active = True

    while active:
        parameter = input('Parameter: ')
        value = input('Value: ')
        if parameter == 'q':
            active = False
        else:
            if value.isdigit():
                body_dict[parameter] = float(value)
            else:
                body_dict[parameter] = value
    
    return body_dict

'--------------------------------------------------------------'

def account_menu():
    '''Account menu'''
    while True:
        sent = ''''
        \tCHOOSE THE ACTION:\t
        1 - ACCOUNT INFORMATION\t
        2 - ACCOUNT PREFERENCES\t
        3 - SWITCH ACCOUNT\t
        4 - CHECK ACCOUNTS\t
        5 - LOG OUT 
        q - BACK TO MENU\n: '''

        choose = input(sent)
        if choose == '1':
            account_info()
        elif choose == '2':
            get_preferences()
        elif choose == '3':
            switch_account()
        elif choose == '4':
            accounts()
        elif choose == '5':
            print('GOODBYE!')
            log_out()
            sys.exit()
        elif choose == 'q':
            main_menu()
        else:
            print('TRY AGAIN')
            account_menu()


def position_menu():
    while True:
        sent = ''''
            \tCHOOSE THE ACTION:\t
            1 - PLACE THE POSITION\t
            2 - UPDATE THE POSITION\t
            3 - POSITION INFORMATION\t
            4 - ALL OPENED POSITIONS\t
            5 - CLOSE POSITION\t
            6 - CLOSE ALL POSITIONS\t
            q - BACK TO MENU\n: '''

        choose = input(sent)
        if choose == '1':
            print('''The list of parameters here:\nhttps://open-api.capital.com/#tag/Trading-greater-Rositions/paths/~1api~1v1~1positions/post''') 
            open_position(body())
        elif choose == '2':
            print('''The list of parameters here:\nhttps://open-api.capital.com/#tag/Trading-greater-Rositions/paths/~1api~1v1~1positions~1%7BdealId%7D/put''') 
            update_the_trade(body())
        elif choose == '3':
            check_trade()
        elif choose == '4':
            list_of_trades()
        elif choose == '5':
            close_position()
        elif choose == '6':
            close_all_positions()
        elif choose == 'q':
            main_menu()
        else:
            print('TRY AGAIN')
            account_menu()
    
    

'--------------------------------------------------------------'

def main_menu():
    '''Main menu'''
    while True:
        sent = ''''
        \tCHOOSE THE ACTION:\t
        1 - ACCOUNT\t
        2 - POSITIONS\t
        q - QUIT\n: '''

        choose = input(sent)
        if choose == '1':
            account_menu()
        elif choose == '2':
            position_menu()
        elif choose == 'q':
            sys.exit()
        else:
            print('TRY AGAIN')
            main_menu()



if __name__ == '__main__':
    if response.status_code == 200:
        CST = response.headers['CST']
        X_SECURITY_TOKEN = response.headers['X-SECURITY-TOKEN']

        print(f'SUCCESSFULLY: {response.status_code}')
        main_menu()
        
    else:
        
        print(f'UNSUCCESSFULLY: {response.status_code}')
        print('Please double-check credentials'.upper())




    
