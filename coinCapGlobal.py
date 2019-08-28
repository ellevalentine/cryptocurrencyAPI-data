import json
import requests
from datetime import datetime

global_url= 'https://api.coinmarketcap.com/v2/global/'

request = requests.get(global_url)
results = request.json()

#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
# setting sort_keys=True will sort all keys
# print(json.dumps(results, sort_keys=True, indent=4))

#this will return to us the figure for active_cryptocurrencies
active_currencies = results['data']['active_cryptocurrencies']
active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_cap = int(results['data']['quotes']['USD']['total_market_cap'])
global_volume = int(results['data']['quotes']['USD']['total_volume_24h'])

active_currencies_string = '{:,}'.format(active_currencies)
active_markets_string = '{:,}'.format(active_markets)
global_cap_string = '{:,}'.format(global_cap)
global_volume_string = '{:,}'.format(global_volume)

# to format the date we have used: strftime - format date and time --> https://linux.die.net/man/3/strftime

last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')

print()
print('There are currently '+ str(active_currencies_string) + ' active crytocurrencies and ' + str(active_markets_string) + ' active markets.')
print('The gobal cap of all crytos is ' + str(global_cap_string) + ' and the 24h global volume is ' + str(global_volume_string) + '.')
print('Bitcoin\'s total percentage of the global cap is ' + str(bitcoin_percentage) + '%.')
print('This information was last updated on ' + str(last_updated_string) + '.')
