import requests



res = requests.get(
    'https://demo-api-capital.backend-capital.com/api/v1/markets?epics=BTCUSD',
    headers={'CST': CST, 'X-SECURITY-TOKEN': X_SECURITY_TOKEN}
)