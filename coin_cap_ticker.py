import json
import requests

ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array'

limit = 100
start = 1
sort = 'id'
convert = 'GBP'

request = requests.get(ticker_url)
results = request.json()

choice = input("Do you want to enter any custom parameters? (y/n):")

if choice == "y":
    limit = input('What is the custom limit?: ')
    start = input('What is the custom start number?: ')
    sort = input('What do you want to sort by?: ')
    convert = input('What is your local currency?: ')

ticker_url += '&limit=' + limit + '&sort=' + sort + '&start=' + start + '&convert=' + convert

request = requests.get(ticker_url)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))

data = results['data']

print()
for currency in data:
    rank = currency['rank']
    name = currency['name']
    symbol = currency['symbol']

    circulating_supply = active_currencies_string(currency['circulating_supply'])
    total_supply = int(currency['total_supply'])

    quotes = currency[quotes][convert]
    market_cap = quotes['market_cap']
    hour_change = quotes['prevent_change_1h']
    day_change = quotes['prevent_change_24h']
    week_change = quotes['prevent_change_7d']
    price = quotes['price']
    volume = quotes['volume_24h']

    volume_string = '{:,}'.format(volume)
    market_cap_string = '{:,}'.format(market_cap)
    circulating_supply_string = '{:,}'.format(circulating_supply)
    total_supply_string = '{:,}'.format(total_supply)

    print(str(rank) + ': '+ name + ' (' + symbol + ')')
    print('Market cap: $' + mark_cap_string)
    print('Price: $' + str(price))
    print('24h Volume: $' + volume_string)
    print('Hour change: ' + hour_change + '%')
    print('Day change: ' + day_change + '%')
    print('Week change: ' + week_change + '%')
