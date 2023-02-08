from capitalcom.client_demo import *
from config import *

cl = Client(login, password, API_KEY)
acc = cl.all_accounts()
print(acc)
