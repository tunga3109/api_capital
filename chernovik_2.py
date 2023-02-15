from capitalcom import *
from config import *
import json



cl = Client(login, password, API_KEY)
acc_switch = cl.switch_account(accountId='172785881488634142')
acc_dict = json.loads(cl.all_accounts())
print(json.dumps(acc_dict['accounts'], indent=4))

# lev = {
#     "SHARES": 2,
#     "CURRENCIES": 30,
#     "INDICES": 50,
#     "CRYPTOCURRENCIES": 5,
#     "COMMODITIES": 10
#   }

# cl = Client(login, password, API_KEY)
# acc = cl.update_account_preferences(leverages=lev, hedgingmode=False)
# print(acc)
