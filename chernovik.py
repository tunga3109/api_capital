from capitalcom.client_demo import *
from config import *

import json

cl = Client(login, password, API_KEY)

a = cl.position_order_confirmation(deal_reference='o_7c0d3f1e-9b86-4e7f-9e4e-29cd669eebf4')
print(a)