from capitalcom.client_demo import *
from config import *
import requests
import time

cl = Client(login, password, API_KEY)
pos = cl.all_positions()
pos_dict = json.loads(pos)

webhook_url = "https://webhook.site/token/75fe23d9-b6ac-46ba-810d-72b0bbd41a44/requests?sorted=newest"

while True:
    r = requests.get(webhook_url, headers={'Content-Type': 'application/json'})

    pos = json.loads(r.text)['data']
    if len(pos) == 0:
        time.sleep(0.5)
        print(pos)
    else:
        body_params = json.loads(pos[-1]['content'])
        time.sleep(1)
        level = body_params['level']
        direction = body_params['direction']
        size = body_params['size']
        type = body_params['type']
        epic = body_params['epic']
        print(cl.place_the_order(direction=DirectionType.BUY, epic=epic, size=size, level=level,type=OrderType.LIMIT))
        break