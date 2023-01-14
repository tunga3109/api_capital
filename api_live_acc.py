'''
list of endpoints here : https://open-api.capital.com
API documantation here: https://capital.com/api-development-guide
'''
import requests
import pprint

from config import *

URL = 'https://api-capital.backend-capital.com' #base url
        
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

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(response.json())

#Returns the transaction history.
response = session.get(
    URL + '/api/v1/history/transactions',
    params={'from': '2022-01-01T00:00:00' ,'to': '2022-04-01T00:00:00' ,'type': 'WITHDRAWAL'},
    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
)

#pp.pprint(response.json())

#json with double quotes
#data = response.json()
#j = json.dumps(data)
#print(j)