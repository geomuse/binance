import requests

import os , sys
current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(f'{current_dir}/../')
print(path)
sys.path.append(path)

from ps.setting import live_secret , live_api
from notification_bot.loguru_notification import loguru_notf
logger = loguru_notf(current_dir)
logger.add('get_history_data')

api_key = live_api
api_secret = live_secret

symbol = 'BTCUSDT'
interval = '1s'  
limit = 1000  

url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
response = requests.get(url, headers={'X-MBX-APIKEY': api_key})
data = response.json()

for candle in data :
    timestamp = candle[0] / 1000 
    open_price = candle[1]
    high_price = candle[2]
    low_price = candle[3]
    close_price = candle[4]
    volume = candle[5]
    print(f'Timestamp: {timestamp}, Open: {open_price}, High: {high_price}, Low: {low_price}, Close: {close_price}, Volume: {volume}')