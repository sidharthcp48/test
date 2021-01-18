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
for i in range(0,5):
    for coin in coins:
        if api["data"][i]["symbol"]==coin["symbol"]:
            print(api["data"][i]["name"]+"-"+api["data"][i]["symbol"])
            print("price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("-----------")