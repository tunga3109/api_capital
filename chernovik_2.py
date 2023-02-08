from capitalcom.client_demo import *
from config import *

lev = {
    "SHARES": 2,
    "CURRENCIES": 30,
    "INDICES": 50,
    "CRYPTOCURRENCIES": 5,
    "COMMODITIES": 10
  }

cl = Client(login, password, API_KEY)
acc = cl.update_account_preferences(leverages=lev, hedgingmode=False)
print(acc)
