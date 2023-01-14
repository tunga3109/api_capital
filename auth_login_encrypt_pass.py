'''
list of endpoints here : https://open-api.capital.com
API documantation here: https://capital.com/api-development-guide
'''
import requests
import pprint

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from base64 import b64decode, b64encode

from config import *

URL = 'https://demo-api-capital.backend-capital.com' #base URL


session = requests.Session() # Create session

'''
API key, login and encrypted password details. The value of the encryptionKey parameter in the POST/session endpoint = true
'''

'''
First of all you should use the GET /session/encryptionKey and mention the generated in the platform's Settings API key in the X-CAP-API-KEY header.
As a response you will receive the encryptionKey and timestamp parameters;
'''

response = session.get(
    URL + '/api/v1/session/encryptionKey',
    headers={'X-CAP-API-KEY': API_KEY}
)

enc_key = response.json()['encryptionKey'] # Encryption Key
timestamp = response.json()["timeStamp"] # Timestamp


'''
Using the received encryptionKey and timestamp parameters you should encrypt your password using the AES encryption method.
'''
input = bytes(password + '|' + str(timestamp), encoding='UTF-8')
input = b64encode(input)
key = b64decode(bytes(enc_key, encoding='UTF-8'))
key = RSA.importKey(key)
cipher = PKCS1_v1_5.new(key)
ciphertext = b64encode(cipher.encrypt(input))
enc_pass = ciphertext.decode('utf-8') # Encrypted password
print(enc_pass)

'''
Go to the POST /session endpoint, set true value for the encryptionKey parameter and mention the received 
in the platform's Settings API key in the X-CAP-API-KEY header, login and prior encrypted password info in the identifier and password parameters.
'''
response_1 = session.post(
    URL + '/api/v1/session',
    json={'encryptedPassword': True, 'identifier': login, 'password': enc_pass},
    headers={'X-CAP-API-KEY': API_KEY}
)

#print(response_1.status_code) # Checking the status code
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(response_1.json())

print('-' * 100)

