##Note: This API has trading disabled and has been IP locked.
API = '6VbJxwqwLuCHS4ZD6BP11ZBxIO4t0sg43DDela9UV9aZeKG6HXry9hcgT63RKONP'
APIKey = 'pct3lKi6ezYb3ej1KmF2dbPEePCtXDjnvpO5Pcov8oDSlIm6K3G78nudsVCSrJcT'
StartDate = "1 Nov, 2017"
EndDate = "20 Dec, 2019"
Pair = "BTCUSDT"
SmallMA = 50
BigMA = 100
MakerFee = 0.00075
TakerFee = 0.00075
SmallEMA = 9
BigEMA = 20
Smoothing = 2

class Returns():

    def __init__(self,returnslist):
        self.returns = returnslist
        self.mean = float()
        self.variance = float()
        self.standard_dev = float()

    def average(self):
        # Calculate the mean of the list
        for each in self.returns:
            self.mean += each
        self.mean = self.mean/len(self.returns)
        return(self.mean)

    def variance(self):
        if self.mean != 0 and self.variance == 0:
            for each in self.returns:
                self.variance += (each-self.mean)**2
            self.variance = self.variance/len(self.returns)
        return(self.variance)

    def standard_deviation(self):
        if self.variance != 0:
            self.standard_dev = self.variance **0.5
        return (self.standard_dev)
