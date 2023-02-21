import json
import pprint
import websockets
import asyncio

from config import API_KEY as ApiKey
from call import CST, X_SECURITY_TOKEN


demo = "wss://api-streaming-capital.backend-capital.com/connect"

async def checkPrices():
    async with websockets.connect(demo) as websocket:
        req = {
                "destination": "marketData.subscribe",
                "correlationId": "1",
                "cst": CST,
                "securityToken": X_SECURITY_TOKEN,
                "payload": { "epics": [ "BTCUSD"] }
                    }
        await websocket.send(json.dumps(req))
        while True: 
            response = json.loads(await websocket.recv())['payload']
            pprint.pprint(response)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(checkPrices())