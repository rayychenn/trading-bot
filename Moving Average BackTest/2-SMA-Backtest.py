from binance.client import Client
import variables as var

client = Client(var.API,var.APIKey)
dollar = 250
klines = client.get_historical_klines(var.Pair, Client.KLINE_INTERVAL_1DAY, var.StartDate)#, enddate)
print("You are trading the",var.BigMA,"vs",var.SmallMA,"moving average on", var.Pair, " since ",var.StartDate)
old_direction = 'Negative'
position = 0
for i in range(var.BigMA,len(klines)):
##Calculate the 10 day klines
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
        if old_direction == 'Positive':
            print("Sell at " + str(each[4]))
            position += -float(each[4])
            dollar += float(each[4])
            #position += -1.01*float(each[4])
        else:
            print("Buy at " + str(each[4]))
            position += float(each[4])
            dollar -= float(each[4])
            #position += 0.99*float(each[4])
        old_direction = direction
if position != 0:
    position -= float(klines[len(klines)-1][4])
    dollar += float(klines[len(klines)-1][4])
    print("Sell at ", str(float(klines[len(klines)-1][4])))
print("Position is ",str(position))