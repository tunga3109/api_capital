import json
import requests
from config import *


URL = 'https://demo-api-capital.backend-capital.com'

class Credentials:

    def __init__(self, log, pas, api_key):
        self.log = log
        self.pas = pas
        self.api_key = api_key
        self.url = URL

    def __str__(self) -> str:
        return f'{self.log}, {self.pas}, {self.api_key}'

class  ApiSession(Credentials):
    
    def start_session(self):

        session = requests.Session()
        response = session.post(
            self.url + '/api/v1/session',
            json={"encryptedPassword": False, 'identifier': self.log, 'password': self.pas},
            headers={'X-CAP-API-KEY': self.api_key}
            )

        global CST
        global X_SECURITY_TOKEN
    
        CST = response.headers['CST']
        X_SECURITY_TOKEN = response.headers['X-SECURITY-TOKEN']

        if response.status_code == 200:
            print('OK')
        else:
            print(response.json())

    def session_details(self):

        session = requests.Session()
        response = session.get(
            self.url + '/api/v1/session',
            headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN},
            )

        data = json.dumps(response.json(), sort_keys=True, indent=4)
        print(data)

    def switch_session(self, acc_id:str):
        session = requests.Session()
        response = session.put(
            URL + '/api/v1/session',
            json={"accountId": acc_id},
            headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN},
            )

        data = json.dumps(response.json(), sort_keys=True, indent=4)
        print(data)

    def remove_session(self):
        session = requests.Session()
        response = session.delete(
            self.url + '/api/v1/session',
            headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN},
            )

        data = json.dumps(response.json(), sort_keys=True, indent=4)
        print(data)


class Account():

    def account_info(self):

        session = requests.Session()
        
        response = session.get(
            URL + '/api/v1/accounts',
            headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN},
            )

        data = json.dumps(response.json(), sort_keys=True, indent=4)
        print(data) 
    
    def account_preferences(self):
        session = requests.Session()
        
        response = session.get(
            URL + '/api/v1/accounts/preferences',
            headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN},
            )

        data = json.dumps(response.json(), sort_keys=True, indent=4)
        print(data) 


   
    

session_api = ApiSession(login, password, API_KEY)
session_api.start_session()
#session_api.session_details()

acc = Account()
acc.account_preferences()
#acc = Account()
#acc.account_info()
#session_api.switch_session('104862060329120030')
#acc.account_info()


        