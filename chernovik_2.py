from capitalcom.client_demo import *
from config import *


cl = Client(login, password, API_KEY)
pos_dict = json.loads(cl.all_positions())['positions']

for i in pos_dict:
    dealId = i['position']['dealId']
    cl.close_position(dealid=dealId)

