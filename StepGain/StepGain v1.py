from binance.client import Client
import variables as var

## Adjust your variables in the variables file in the same directory
client = Client(var.API,var.APIKey)
dollar = 1000
trading = 100
Position = 0
klines = client.get_historical_klines(var.Pair, Client.KLINE_INTERVAL_12HOUR, var.StartDate)
for i in range(var.Candles,len(klines)):
