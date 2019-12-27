from binance.client import Client
import variables as var
from datetime import datetime

ts = int(1507725176595)
## Adjust your variables in the variables file in the same directory
client = Client(var.API,var.APIKey)

print(client.get_historical_klines('ETHUSDT', Client.KLINE_INTERVAL_1DAY, '27 Dec, 2019'))

print(datetime.utcfromtimestamp(float(each[6]))/1000).strftime('%Y-%m-%d %H:%M:%S')