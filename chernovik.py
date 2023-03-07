from capitalcom.client_demo import *
from config import *

import json

cl = Client(login, password, API_KEY)

a = cl.account_activity_history()
print(a)