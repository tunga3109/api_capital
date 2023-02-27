from capitalcom.client_demo import *
from config import *

cl = Client(login, password, API_KEY)

print(cl.position_order_confirmation(deal_reference='p_00601567-0055-311e-0000-000080ee0613'))