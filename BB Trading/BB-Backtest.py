from binance.client import Client
import variables as var

## Adjust your variables in the variables file in the same directory
client = Client(var.API,var.APIKey)

print(client.get_account())

dollar = 1000
trading = 500
position = 0
klines = client.get_historical_klines(var.Pair, Client.KLINE_INTERVAL_30MINUTE, var.StartDate)
print("You are trading the Boilinger Bands with a SMA of", var.SMA_Value, "and standard deviation of",var.StandardDev,"since",var.StartDate, "and", dollar , "dollars.")
#for i in range(var.SMA_Value,len(klines)):
for i in range(var.SMA_Big,len(klines)):
    ## Calculate the Simple Moving Average
    SMA = 0
    for each in klines[i-var.SMA_Value:i]:
        SMA += float(each[4])
    SMA = SMA/var.SMA_Value

    if i//5 == 0:
        SMA_5 = SMA
        print(SMA_5)
    elif i//10 == 0:
        SMA_10 = SMA
        print(SMA_10)
    elif i//20 == 0:
        SMA_20 = SMA
        print(SMA_20)
    SMA2 = 0
    for each in klines[i-var.SMA_Big:i]:
        SMA2 += float(each[4])
    SMA2 = SMA2/var.SMA_Big

    ## Determine The Size of the Standard Deviation
    SD = 0
    for each in klines[i-var.SMA_Value:i]:
        SD += (float(each[4])-SMA) ** 2
    SD = (SD/var.SMA_Value) ** 0.5

    ## Determine the upper and lower band
    Upper = SMA + (SD * var.StandardDev)
    Lower = SMA - (SD * var.StandardDev)
    if float(each[4]) < Lower and position == 0:
        print("Buy at", str(each[4]))
        position += (trading / float(each[4])) * (1 - var.MakerFee)
        dollar -= trading
    if float(each[4]) > Upper and position != 0:
        print("Sell at", str(each[4]))
        dollar += position * float(each[4]) * (1 - var.TakerFee)
        position = 0

if position != 0:
    print("Final sell at" + str(float(klines[len(klines)-1][4])))
    dollar += position * float(klines[len(klines)-1][4])
    position = 0
print("Dollar is ",str(dollar))