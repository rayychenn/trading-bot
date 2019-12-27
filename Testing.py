from binance.client import Client

API = '6VbJxwqwLuCHS4ZD6BP11ZBxIO4t0sg43DDela9UV9aZeKG6HXry9hcgT63RKONP'
APIKey = 'pct3lKi6ezYb3ej1KmF2dbPEePCtXDjnvpO5Pcov8oDSlIm6K3G78nudsVCSrJcT'
client = Client(API, APIKey)
balances = client.get_account()

assets = {}
for each in balances['balances']:
    if float(each['free']) != 0:
        assets[each['asset']] = each['free']

print(assets)
strong = ""
for each in assets:
    strong += str(each) + ',' + str(assets[each]) + ';'

print(strong)
list1=[]
for asset in assets:
    list1 += [str((asset,float(assets[asset])))]

a = ';'.join(list1)
b = a.split(';')
print(b)
for each in b:
    each = each.strip('"')
    each = each.strip("(")
    each = each.strip(")")
    each = each.strip("'")
    each = each.strip("'")

class test:
    def __init__(self):
        self.list = []
        self.list += [(1,2)]
        return None
    def __str__(self):
        return self.list

