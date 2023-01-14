'''
list of endpoints here : https://open-api.capital.com
API documantation here: https://capital.com/api-development-guide
'''
import requests
import json
import sys

BASE_DEMO_URL = 'https://demo-api-capital.backend-capital.com' 
BASE_LIVE_URL = 'https://api-capital.backend-capital.com'

print('------WELCOME TO CAPITAL API----------')
login = input('YOUR LOGIN: ')
password = input('YOUR PASSWORD: ')
api_key = input('YOUR API KEY: ')
if login == 'q' or password == 'q' or api_key == 'q':
    sys.exit()

URL = 'https://demo-api-capital.backend-capital.com' #base url
        
'''Create session'''
session = requests.Session()

'''Returns the user's session details and optionally tokens.'''
response = session.post(
    URL + '/api/v1/session',
    json={'identifier': login, 'password': password},
    headers={'X-CAP-API-KEY': api_key}
)

'---------------------------------------------------------------------'

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
    

def accounts():
    '''Returns a list of accounts belonging to the logged-in client'''
    response = session.get(
        URL + '/api/v1/accounts',
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )

    print(json.dumps(response.json(), indent=4))

'--------------------------------------------------------------'


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
        elif choose == 'q':
            main_menu()
        else:
            print('TRY AGAIN')
            account_menu()

def position_menu():
    pass

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




    
