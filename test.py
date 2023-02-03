from capitalcom import *
import requests
from config import *


tung = Client(login, password, API_KEY)
print(tung.place_the_position(direction=DirectionType.BUY, size=1, epic='BTCUSD'))


        