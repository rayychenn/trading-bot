from binance.client import Client
import variables as var
from datetime import datetime

dollar = 1000
trading = 1000
position = 0

##Setup the client with your APIs stored in the variables.py folder
client = Client(var.API,var.APIKey)

klines = client.get_historical_klines(var.Pair, Client.KLINE_INTERVAL_1DAY, var.StartDate)

print("You are trading the",var.BigEMA,"vs",var.SmallEMA,"exponential moving average on"
      , var.Pair, " since ",var.StartDate, " and ", dollar , " dollars.")

old_direction = 'Null'

returns = []

for i in range(var.BigEMA,len(klines)):
    price_now = float(klines[i][4])
    if old_direction == 'Null':

        ##Calculate SMA for shorter time period.
        smallMA = 0
        for each in klines[i - var.SmallEMA:i]:
            smallMA += float(each[4])
        smallMA = smallMA / var.SmallEMA

        ##Calculate SMA for longer time period.
        bigMA = 0
        for each in klines[i - var.BigEMA:i]:
            bigMA += float(each[4])
        bigMA = bigMA / var.BigEMA

        SmallEMA = smallMA
        smallWeight = var.Smoothing / (var.SmallEMA + 1)
        BigEMA = bigMA
        bigWeight = var.Smoothing / (var.BigEMA + 1)
    elif old_direction != 'Null':
        ##Calculate EMA for shorter time period.
        SmallEMA = (price_now * smallWeight) + SmallEMA *(1-smallWeight)
        ##Calculate EMA for shorter time period.
        BigEMA = (price_now * bigWeight) + BigEMA *(1-bigWeight)

    if (BigEMA < SmallEMA) and (price_now > SmallEMA):
        direction = 'Positive'
    elif BigEMA < SmallEMA and old_direction == 'Null':
        direction = 'Positive'
    if (BigEMA > SmallEMA) and (price_now < BigEMA):
        direction = 'Negative'
    elif BigEMA > SmallEMA and old_direction == 'Null':
        direction = 'Negative'
    if old_direction != direction:
        if old_direction == 'Null':
            old_direction = direction
        elif old_direction != direction and i > 3*var.BigEMA:
            # Determine the date and time of the trade
            date = datetime.utcfromtimestamp(float(klines[i][6])/1000).strftime('%Y-%m-%d %H:%M:%S')
            if old_direction == 'Positive' and position != 0:
                print("Sell at " + str(klines[i][4]))
                dollar += position * price_now * (1-var.TakerFee)
                position = 0
                if price_now > buy:
                    gain = round((10000*(price_now-buy)/price_now))
                    print("Profit = " + str(price_now - buy) + " Or " + str(gain/100) + "% at " + date)
                    returns += [gain/100]
                else:
                    loss = round((10000*(price_now-buy)/price_now))
                    print("Loss = " + str(price_now - buy) + " Or " + str(loss/100) + "% at " + date)
                    returns += [loss/100]
                buy = 0
            elif old_direction != 'Positive':
                print("Buy at " + str(klines[i][4]))
                position += (trading/price_now) * (1-var.MakerFee)
                dollar -= trading
                buy = price_now
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
print(returns)


ReturnsTest = var.Returns(returns)

print("Average is ",str(ReturnsTest.average()))
print("Variance is ",str(ReturnsTest.variance()))
print("Standard Deviation is ",str(ReturnsTest.standard_dev()))