import requests
import json
api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=6c0f5764-4356-4ba4-8e23-b52996b63242")
api=json.loads(api_request.content)

coins=[
    {
        "symbol":"BTC",
        "amount_owned":2,
        "price_per_coin":3200
    },
    {
        
        "symbol":"ETH",
        "amount_owned":100,
        "price_per_coin":2.05
    }
]
total_pl=0
for i in range(0,5):
    for coin in coins:
        if api["data"][i]["symbol"]==coin["symbol"]:
            total_paid=coin["amount_owned"]*coin["price_per_coin"]
            current_value=coin["amount_owned"]*api["data"][i]["quote"]["USD"]["price"]
            pl_coin=api["data"][i]["quote"]["USD"]["price"]-coin["price_per_coin"]
            total_pl_coin=pl_coin*coin["amount_owned"]
            total_pl=total_pl+total_pl_coin

            print(api["data"][i]["name"]+"-"+api["data"][i]["symbol"])
            print("price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("No of coins",coin["amount_owned"])
            print("Total amount paid","${0:.2f}".format(total_paid))
            print("current value","${0:.2f}".format(current_value))
            print("P/L per coin","${0:.2f}".format(pl_coin))
            print("Total P/L per coin","${0:.2f}".format(total_pl_coin))
            print("-----------")
print("Total P/L for portfolio","${0:.2f}".format(total_pl))            