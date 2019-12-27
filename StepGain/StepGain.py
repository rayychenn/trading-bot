from binance.client import Client
import variables as var

## Adjust your variables in the variables file in the same directory
client = Client(var.API,var.APIKey)
dollar = 1000
trading = 100
klines = client.get_historical_klines(var.Pair, Client.KLINE_INTERVAL_4HOUR, var.StartDate)
print("You are trading the StepGain movement on", var.Pair, " since ",var.StartDate, " and ", dollar , " dollars.")
old_direction = 'Null'
position = 0

for i in range(var.Candles,len(klines)):
##Calculate the small Simple Moving Average klines
    HighVal = 0
    LowVal = 10000000000
    for each in klines[i-var.Candles:i]:
        if float(each[4]) > HighVal:
            HighVal = float(each[4])
        if float(each[4]) < LowVal:
            LowVal = float(each[4])

    CurrentPrice = float(each[4])

    ##Define a buy
    if position == 0 and CurrentPrice < HighVal:
        if CurrentPrice/HighVal < (1-var.SGBuy1/100):
            print("Buy at " + str(each[4]))
            position += (trading / float(each[4])) * (1 - var.MakerFee)
            dollar -= trading
            BoughtPrice = float(each[4])

    ##Define a sell where we have a position,
    if position != 0 and ((CurrentPrice > LowVal and (BoughtPrice*(1+(var.SGSell1/100))) < CurrentPrice) or ((BoughtPrice/CurrentPrice) < (1-(var.StopLoss/100)))):# and BoughtPrice < CurrentPrice:
        print("Sell at " + str(each[4]))
        dollar += position * float(each[4])
        position = 0
        dollar -= trading
        SoldPrice = float(each[4])

if position != 0:
    print("Final sell at " + str(float(klines[len(klines)-1][4])))
    dollar += position * float(klines[len(klines)-1][4])
    position = 0
print("Dollar is ",str(dollar))