import requests

webhook_url = "https://webhook.site/75fe23d9-b6ac-46ba-810d-72b0bbd41a44"

a = {"epic": "BTCUSD", "direction": "BUY", "size": 1, "level": 24745 , "type": "LIMIT"}

r = requests.get(webhook_url, json=a, headers={'Content-Type': 'application/json'})