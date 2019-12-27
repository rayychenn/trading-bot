from binance.client import Client
import variables as var
from datetime import datetime
## Adjust your variables in the variables file in the same directory
client = Client(var.API,var.APIKey)
dollar = 1000
trading = 1000
klines = client.get_historical_klines(var.Pair, Client.KLINE_INTERVAL_4HOUR, var.StartDate)
print("You are trading the",var.BigMA,"vs",var.SmallMA,"moving average on"
      , var.Pair, " since ",var.StartDate, " and ", dollar , " dollars.")

old_direction = 'Null'
position = 0

for i in range(var.BigMA,len(klines)):
    ##Calculate the small Simple Moving Average klines
    smallMA = 0
    for each in klines[i-var.SmallMA:i]:
        smallMA += float(each[4])
    smallMA = smallMA/var.SmallMA

    bigMA = 0
    for each in klines[i-var.BigMA:i]:
        bigMA += float(each[4])
    bigMA = bigMA/var.BigMA

    if bigMA < smallMA:
        direction = 'Positive'

    if bigMA > smallMA:
        direction = 'Negative'

    if old_direction != direction:
        if old_direction == 'Null':
            old_direction = direction
        else:
            # Determine the date and time of the trade
            date = datetime.utcfromtimestamp(float(each[6])/1000).strftime('%Y-%m-%d %H:%M:%S')
            if old_direction == 'Positive' and position != 0:
                print("Sell at " + str(each[4]))
                dollar += position * float(each[4]) * (1-var.TakerFee)
                position = 0
                if float(each[4]) > buy:
                    print("Profit = " + str(float(each[4]) - buy) + " Or " + str((round((10000*(float(each[4])-buy)/float(each[4]))))/100) + "% at " + date)
                else:
                    print("Loss = " + str(float(each[4]) - buy) + " Or " + str((round((10000*(float(each[4])-buy)/float(each[4]))))/100) + "% at " + date)
                buy = 0
            elif old_direction != 'Positive':
                print("Buy at " + str(each[4]))
                position += (trading/float(each[4])) * (1-var.MakerFee)
                dollar -= trading
                buy = float(each[4])
            old_direction = direction

if position != 0:
    print("Final sell at " + str(float(klines[len(klines)-1][4])))
    if float(klines[len(klines)-1][4]) > buy:
        print("Profit = " + str(float(klines[len(klines)-1][4]) - buy) + " Or " + str(
            (round((10000 * (float(klines[len(klines)-1][4]) - buy) / float(klines[len(klines)-1][4])))) / 100) + "%.")
    else:
        print("Loss = " + str(float(klines[len(klines)-1][4]) - buy) + "Or " + str(
            (round((10000 * (float(klines[len(klines)-1][4]) - buy) / float(klines[len(klines)-1][4])))) / 100) + "%.")

    dollar += position * float(klines[len(klines)-1][4])
    position = 0
print("Dollar is ",str(dollar))