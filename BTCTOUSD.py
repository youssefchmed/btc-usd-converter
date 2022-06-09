import urllib.request as urllib2
import json
api="https://blockchain.info/ticker"
def convert_to_bitcoin(amount, currency):
    data = urllib2.urlopen(api)
    converted = json.loads(data.read())
    print(converted[currency]["last"]*amount)

n=0.00091214
print("USD",end='   ')
convert_to_bitcoin(n, "USD")
print("TND",end='   ')
convert_to_bitcoin(n*3, "USD")
