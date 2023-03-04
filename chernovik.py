from capitalcom.client_demo import *
from config import *

import json

cl = Client(login, password, API_KEY)

a = json.loads(cl.all_accounts())
print(a['accounts'])