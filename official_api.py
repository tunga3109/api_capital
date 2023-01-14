import http.client

conn = http.client.HTTPSConnection("demo-api-capital.backend-capital.com")
payload = "{\n\t\"identifier\": \"tunga3109@gmail.com\", \n\t\"password\": \"Xuxin_10031999\"\n}"
headers = {
  'X-CAP-API-KEY': 'Ydb8GV1oruPrsd4j',
  'Content-Type': 'application/json'
}
conn.request("POST", "/api/v1/session", payload, headers)
res = conn.getresponse()
data = res.read()
headers = res.getheaders()
print(headers)
print(data.decode("utf-8"))




#payload = "{\n    \"epic\": \"SILVER\",\n    \"direction\": \"BUY\",\n    \"size\": 1,\n    \"guaranteedStop\": true,\n    \"stopLevel\": 19,\n    \"profitLevel\": 24\n}"
#headers = {
#  'X-SECURITY-TOKEN': 'ZWPAaHU4eWiid1OEzVLdscpDk8nJBdJ',
#  'CST': 'SNph3drJaxuS2O1Zk7tDhDyU',
#  'Content-Type': 'application/json'
#}
#conn.request("POST", "/api/v1/positions", payload, headers)
#res = conn.getresponse()
#data = res.read()
#print(data.decode("utf-8"))

#payload = ''
#headers = {
#  'X-SECURITY-TOKEN': 'ZWPAaHU4eWiid1OEzVLdscpDk8nJBdJ',
#  'CST': 'SNph3drJaxuS2O1Zk7tDhDyU',
#  'Content-Type': 'application/json'
#}
#dealReference = input('DEAL REFERENCE: ')
#conn.request("GET", f"/api/v1/confirms/{dealReference}", payload, headers)
#res = conn.getresponse()
#data = res.read()
#print(data.decode("utf-8"))


#006011e7-0055-311e-0000-0000804a1bd2
#dealId = input(' DEAL ID: ')
#conn.request("DELETE", f"/api/v1/positions/{dealId}", payload, headers)
#res = conn.getresponse()
#data = res.read()
#print(data.decode("utf-8"))

#payload = "{\n    \"guaranteedStop\": true,\n    \"stopLevel\": 18,\n    \"profitLevel\": 22\n}"
#headers = {
#  'X-SECURITY-TOKEN': 'ZWPAaHU4eWiid1OEzVLdscpDk8nJBdJ',
#  'CST': 'SNph3drJaxuS2O1Zk7tDhDyU',
#  'Content-Type': 'application/json'
#}
#dealId = input(' DEAL ID: ')
#conn.request("PUT", f"/api/v1/positions/{dealId}", payload, headers)
#res = conn.getresponse()
#data = res.read()
#print(data.decode("utf-8"))
