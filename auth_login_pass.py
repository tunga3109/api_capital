'''
list of endpoints here : https://open-api.capital.com
API documantation here: https://capital.com/api-development-guide
'''


'''
API key, login and password details. The value of the encryptionKey parameter in the POST/session endpoint = false
'''

'''
Here you should simply use the POST/session endpoint and mention the received 
in the platform's Settings API key in the X-CAP-API-KEY header, login and password info in the identifier and password parameters.
'''
import requests
import json

from config import * 


URL = 'https://demo-api-capital.backend-capital.com' #base url
        

session = requests.Session() # Create session

# Returns the user's session details and optionally tokens.
response = session.post(
    URL + '/api/v1/session',
    json={"encryptedPassword": False, 'identifier': login, 'password': password},
    headers={'X-CAP-API-KEY': API_KEY}
)

CST = response.headers['CST']
X_SECURITY_TOKEN = response.headers['X-SECURITY-TOKEN']

data = json.dumps(response.json(), sort_keys=True, indent=4)
print(data)





