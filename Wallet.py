class Wallet:

    def __init__(self,API,APIKey):
        self.API = API
        self.APIKey = APIKey

        ## Initialise a Wallet class with your API and APIKey and retrieve your balances
        from binance.client import Client
        client = Client(self.API, self.APIKey)
        balances = client.get_account()

        ## Create a dictionary with the balances that aren't zero
        self.assets = {}
        for each in balances['balances']:
            if float(each['free']) != 0:
                self.assets[each['asset']] = each['free']

    def refresh(self):
        ## Initialise a Wallet class with your API and APIKey and retrieve your balances
        from binance.client import Client
        client = Client(self.API, self.APIKey)
        balances = client.get_account()

        ## Create a dictionary with the balances that aren't zero
        self.assets = {}
        for each in balances['balances']:
            if float(each['free']) != 0:
                self.assets[each['asset']] = each['free']

    def __str__(self):
        output_string = ""
        for each in self.assets:
            output_string += '<' + str(each) + ',' + str(float(self.assets[each])) + '>'
        return output_string

    def buy(self,coin,amount):
        if coin in self.assets:
            self.assets[coin] += amount
        else:
            self.assets[coin] = amount
        return("You have added this asset")

    def sell(self,coin,amount):
        if (coin in self.assets) and (self.assets[coin] > amount):
            self.assets[coin] -= amount
            return("You have sold this asset")
        else:
            return("You cannot sell this asset")

API = '6VbJxwqwLuCHS4ZD6BP11ZBxIO4t0sg43DDela9UV9aZeKG6HXry9hcgT63RKONP'
APIKey = 'pct3lKi6ezYb3ej1KmF2dbPEePCtXDjnvpO5Pcov8oDSlIm6K3G78nudsVCSrJcT'

Binance = Wallet(API,APIKey)

print(Binance)