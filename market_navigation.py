import requests
import json

from call import *
from call_2 import *
from config import API_KEY, login, password

URL = 'https://demo-api-capital.backend-capital.com'

session = requests.Session()

response = session.post(
    URL + '/api/v1/session',
    json={'encryptedPassword': False, 'identifier': login, 'password': password},
    headers={'X-CAP-API-KEY': API_KEY},
)

CST = response.headers['CST']
X_SECURITY_TOKEN = response.headers['X-SECURITY-TOKEN']


id = input('id: ')
response = session.get(
    URL + f'/api/v1/marketnavigation/{id}',
    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
)


# def most_volatile(id, country):

#     response_1 = session.get(
#             URL + f'/api/v1/marketnavigation/{id}.most_volatile',
#             headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
#         )
#     n = 0
#     if 'markets' in response_1.json():
#         print(country)
#         for market in response_1.json()['markets']:
#             n += 1
#             epic = market['epic']
#             instrument_name = market['instrumentName']
#             bid_price = market['bid']
#             print(f'{n} {epic} - {instrument_name} -> bid price - {bid_price} $')
#         print(f'Sum: {n}')
        
    
            

if __name__ == '__main__':

    print(json.dumps(response.json(), indent=4, sort_keys=True))
    
    # shares = response.json()['nodes']
    # # print(shares)
    # for id_1 in shares:
    #     id = id_1['id']
        # most_volatile(id, id_1['name'])
        
        

        #for i in response.json()['markets']:
        #    print(i)
        
    #print(pd.DataFrame(response.json()['markets']).to_string())

    print('-----------' * 10)
