from binance.client import Client
import variables as var
from datetime import datetime

dollar = 1000
trading = 1000
position = 0

##Setup the client with your APIs stored in the variables.py folder
client = Client(var.API,var.APIKey)

klines = client.get_historical_klines(var.Pair, Client.KLINE_INTERVAL_1DAY, var.StartDate)

#klines = [[0,0,0,0,1],[0,0,0,0,2],[0,0,0,0,3],[0,0,0,0,4],[0,0,0,0,5],[0,0,0,0,6],[0,0,0,0,7],[0,0,0,0,8],[0,0,0,0,9],[0,0,0,0,10],
#         [0,0,0,0,11],[0,0,0,0,12],[0,0,0,0,13],[0,0,0,0,14],[0,0,0,0,15],[0,0,0,0,16],[0,0,0,0,17],[0,0,0,0,18],[0,0,0,0,19],[0,0,0,0,20]]


print("You are trading the",var.BigMA,"vs",var.SmallMA,"moving average on"
      , var.Pair, " since ",var.StartDate, " and ", dollar , " dollars.")

old_direction = 'Null'

returns = []
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
            date = datetime.utcfromtimestamp(float(klines[i][6])/1000).strftime('%Y-%m-%d %H:%M:%S')
            if old_direction == 'Positive' and position != 0:
                print("Sell at " + str(klines[i][4]))
                dollar += position * float(klines[i][4]) * (1-var.TakerFee)
                position = 0
                if float(klines[i][4]) > buy:
                    gain = round((10000*(float(klines[i][4])-buy)/float(klines[i][4])))
                    returns += [gain/100]
                    print("Profit = " + str(float(klines[i][4]) - buy) + " Or " + str(gain/100) + "% at " + date)
                else:
                    loss = round((10000*(float(klines[i][4])-buy)/float(klines[i][4])))
                    returns += [loss/100]
                    print("Loss = " + str(float(klines[i][4]) - buy) + " Or " + str(loss/100) + "% at " + date)
                buy = 0
            elif old_direction != 'Positive':
                print("Buy at " + str(klines[i][4]))
                position += (trading/float(klines[i][4])) * (1-var.MakerFee)
                dollar -= trading
                buy = float(klines[i][4])
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


# Define a new variable for volatility
print(returns)