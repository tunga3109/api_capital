from config import *

from capitalcom.client_demo import *

cl = Client(login, password, API_KEY)

print(cl.check_position(dealid='00018387-0055-311e-0000-000080be16c7'))