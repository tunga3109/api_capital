import requests
import json
import sys
import unittest

from config import *
from call import CST, X_SECURITY_TOKEN


BASE_DEMO_URL = 'https://demo-api-capital.backend-capital.com' 
BASE_LIVE_URL = 'https://api-capital.backend-capital.com'
        
'''Create session'''
session = requests.Session()

def list_of_trades():
    '''Show the list of trades'''    
    response = session.get(
        BASE_DEMO_URL + '/api/v1/positions',
        headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
        )

    return len(response.json()["positions"])

list_of_trades()

class EndpointTestCase(unittest.TestCase):

    def test_list_of_trades(self):
        
        
        self.assertEqual(list_of_trades(), 0)

unittest.main()
        