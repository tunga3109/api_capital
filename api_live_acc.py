'''
list of endpoints here : https://open-api.capital.com
API documantation here: https://capital.com/api-development-guide
'''
import requests
import json

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


#data = json.dumps(response.json(), sort_keys=True, indent=4)
#print(data)

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(response.json())

#Returns the transaction history.
response = session.get(
    URL + '/api/v1/history/transactions',
    params={'from': '2022-01-01T00:00:00' ,'to': '2022-04-01T00:00:00' ,'type': 'WITHDRAWAL'},
    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
)
a = {'a': 'a', 'b': 'b'}


for i in response.json()["transactions"]:
    data_dict = {"currency": i["currency"], "reference": i["reference"], "size": i["size"]}
    print(json.dumps(data_dict, sort_keys=True ,indent=4))
    
    
    #data = json.dumps(data_dict, sort_keys=True, indent=4)
    #print(data)

