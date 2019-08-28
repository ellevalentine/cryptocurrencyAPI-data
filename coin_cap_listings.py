import json
import requests

listing_url = 'https://api.coinmarketcap.com/v2/listings'

request = requests.get(listing_url)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

data = results['data']

#here we lable each block in the hash: currency
for currency in data:
    rank = currency['id']
    name = currency['name']
    symbol = currency['symbol']
    print(str(rank) + ': ' + name + ' (' + symbol + ')')

    #this will return each block from the hash in the format -> 3854: Unification (UND)
