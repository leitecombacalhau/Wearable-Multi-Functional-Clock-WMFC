from requests import Request, Session
import pprint
import json
import math

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'slug': 'bitcoin',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'aacc2c17-3b65-4e4e-9442-a12bf3f6921b',
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)
pprint.pprint(math.floor(json.loads(response.text)['data']['1']['quote']['USD']['price']))