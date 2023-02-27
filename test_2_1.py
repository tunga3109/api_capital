from capitalcom.client import *
from config import *

cl = Client(login, password, API_KEY)

print(cl.close_position(dealid='00018509-0055-311e-0000-000080fa363a'))