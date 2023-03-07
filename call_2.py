'''
list of endpoints here : https://open-api.capital.com
API documantation here: https://capital.com/api-development-guide
'''

'''
Here you should simply use the POST/session endpoint and mention the received 
in the platform's Settings API key in the X-CAP-API-KEY header, login and password info in the identifier and password parameters.
'''
from turtle import Turtle
import requests
import pprint
import sys
from datetime import datetime
import json

from config import *


BASE_DEMO_URL = 'https://demo-api-capital.backend-capital.com' 
BASE_LIVE_URL = 'https://api-capital.backend-capital.com'

#UTC time
utc_datetime  = datetime.utcnow()
dt_now_str = utc_datetime.strftime("%Y-%m-%dT%H:%M:%S")
print(dt_now_str)


        

session = requests.Session() # Create session

'''Returns the user's session details and optionally tokens.'''
response = session.post(
    BASE_LIVE_URL + '/api/v1/session',
    json={"encryptedPassword": False, 'identifier': login, 'password': password},
    headers={'X-CAP-API-KEY': API_KEY}
)

CST = response.headers['CST']
X_SECURITY_TOKEN = response.headers['X-SECURITY-TOKEN']


pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(response.json())


'''Search epics'''
def search_epic():
    epic_name = input('Paste the epic name: ')
    response = session.get(
        BASE_DEMO_URL + f'/api/v1/markets/',
        params={'searchTerm': epic_name},
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )

    print(json.dumps(response.json(), sort_keys=True, indent=4))


'''Place the order'''
#Creates an working order.
#order_body = {
#"direction": "BUY",
#"epic": "BTCUSD",
#"level": 80,
#"size": 1,
#"type": "LIMIT"
#}

def place_order(body):
    print('------Place the order-------')
    response = session.post(
        BASE_DEMO_URL + '/api/v1/workingorders',
        json=body,
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
        # You are to find out the CST and X-SECURITY-TOKEN in response.headers
    )

    print(response.json())


'''Check the order by Deal Reference'''
def check_order_by_deal_ref():
    print('-------Check the order by Deal Reference--------')
    dealReference = input('Please paste the DealReference: ')
    if dealReference == 'f':
        sys.exit()
    else:
        response = session.get(
            BASE_DEMO_URL + f'/api/v1/confirms/{dealReference}',
            headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
        )
    
        pp.pprint(response.json()) # DealID in 'affectedDeals' array


'''Update the order'''
def update_the_order(body):
    print('----Update the order----')
    dealID = input('Paste Deal ID: ')
    if dealID == 'q':
        sys.exit()
    else:
        response = session.put(
            BASE_DEMO_URL + f'/api/v1/workingorders/{dealID}',
            json=body,
            headers={
                'CST': CST, 
                'X-SECURITY-TOKEN': X_SECURITY_TOKEN,}
            # You are to find out the CST and X-SECURITY-TOKEN in response.headers()
        )
        print(response.json())


'''Returns all open working orders for the active account.'''
def list_of_orders():
    print('-----Returns all open working orders for the active account-----')
    response = session.get(
        BASE_DEMO_URL + '/api/v1/workingorders',
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
    )

    pp.pprint(response.json())
    

'''Deletes an working order.'''
def close_orders():
    print('----Deletes an working order------')
    dealid = input('Paste the order dealID: ')
    response = session.delete(
        BASE_DEMO_URL + f'/api/v1/workingorders/{dealid}',
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN} 
        # You are to find out the CST and X-SECURITY-TOKEN in response.headers
    )

    print(response.json())

    
'''Checking prices'''

response = session.get(
    BASE_LIVE_URL + f'/api/v1/history/activity?from=2016-01-01T00:00:00&to=2023-03-05T00:00:00&detailed=true&filter=source!=DEALER;type!=POSITION;',
    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
)
if __name__ == '__main__':
    print(json.dumps(response.json(), indent=4))
 
