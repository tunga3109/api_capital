import http.client
import json

from Crypto.Cipher import PKCS1_v1_5 # Install via pip/pip3 install pycryptodome
from Crypto.PublicKey import RSA
from base64 import b64decode, b64encode

from config import login, password, API_KEY

URL = 'demo-api-capital.backend-capital.com' 

conn = http.client.HTTPSConnection(URL)
payload = ''
headers = {
  'X-CAP-API-KEY': API_KEY
}
conn.request("GET", "/api/v1/session/encryptionKey", payload, headers)
res = conn.getresponse()
data = res.read()
res_dict = json.loads(data.decode("utf-8"))

enc_key = res_dict['encryptionKey']
timestamp = res_dict['timeStamp']

input = bytes(password + '|' + str(timestamp), encoding='UTF-8')
input = b64encode(input)
key = b64decode(bytes(enc_key, encoding='UTF-8'))
key = RSA.importKey(key)
cipher = PKCS1_v1_5.new(key)
ciphertext = b64encode(cipher.encrypt(input))
enc_pass = ciphertext.decode('utf-8') # Encrypted password

payload = json.dumps({
  "encryptedPassword": True,
  "identifier": login,
  "password": enc_pass 
})

headers = {
  'X-CAP-API-KEY': API_KEY,
  'Content-Type': 'application/json'
}

conn.request("POST", "/api/v1/session", payload, headers)
res = conn.getresponse()
data = res.read()
res_dict_2 = json.loads(data.decode('utf-8'))
headers = res.getheaders()
print(json.dumps(dict(headers), sort_keys=True, indent=4))
#print(json.dumps(res_dict_2, sort_keys=True, indent=4))




