from tkinter import *
import requests
import json
import sqlite3

pycrypto=Tk()
pycrypto.title("My Crypto Portfolio")
pycrypto.iconbitmap("favicon.ico")

con=sqlite3.connect('coin.db')
cobj=con.cursor()
cobj.execute("create table if not exists coin(id integer primary key,symbol text,amount integer,price real)")
con.commit()

def font_color(amount):
    if amount>=0:
        return "green"
    else:
        return "red"    

def my_portfolio():
    api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=6c0f5764-4356-4ba4-8e23-b52996b63242")
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
      },
      {
         "symbol":"XRP",
        "amount_owned":20,
        "price_per_coin":2.05 
      }
    ]
    total_pl=0
    coin_row=1
    total_current_value=0
    total_price=0
    for i in range(0,5):
        for coin in coins:
            if api["data"][i]["symbol"]==coin["symbol"]:
               total_paid=coin["amount_owned"]*coin["price_per_coin"]
               current_value=coin["amount_owned"]*api["data"][i]["quote"]["USD"]["price"]
               pl_coin=api["data"][i]["quote"]["USD"]["price"]-coin["price_per_coin"]
               total_pl_coin=pl_coin*coin["amount_owned"]
               total_pl=total_pl+total_pl_coin
               total_current_value=total_current_value+current_value
               total_price=total_price+api["data"][i]["quote"]["USD"]["price"]

               name=Label(pycrypto,text=api["data"][i]["symbol"],bg="#F3F4F6",fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
               name.grid(row=coin_row,column=0,sticky=N+S+E+W)

               price=Label(pycrypto,text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]),bg="#F3F4F6",fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
               price.grid(row=coin_row,column=1,sticky=N+S+E+W)

               no_coins=Label(pycrypto,text=coin["amount_owned"],bg="#F3F4F6",fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
               no_coins.grid(row=coin_row,column=2,sticky=N+S+E+W)

               amount_paid=Label(pycrypto,text="${0:.2f}".format(current_value),bg="#F3F4F6",fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
               amount_paid.grid(row=coin_row,column=3,sticky=N+S+E+W)

               current_val=Label(pycrypto,text="${0:.2f}".format(current_value),bg="#F3F4F6",fg=font_color(float("{0:.2f}".format(current_value))),font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
               current_val.grid(row=coin_row,column=4,sticky=N+S+E+W)

               pl_coin=Label(pycrypto,text="${0:.2f}".format(pl_coin),bg="#F3F4F6",fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
               pl_coin.grid(row=coin_row,column=5,sticky=N+S+E+W)

               total_pl_co=Label(pycrypto,text="${0:.2f}".format(total_pl_coin),bg="#F3F4F6",fg=font_color(float("{0:.2f}".format(total_pl_coin))),font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
               total_pl_co.grid(row=coin_row,column=6,sticky=N+S+E+W)
               
               coin_row=coin_row+1
    total_pl_co=Label(pycrypto,text="${0:.2f}".format(total_pl),bg="#F3F4F6",fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
    total_pl_co.grid(row=coin_row,column=6,sticky=N+S+E+W)
    current_val=Label(pycrypto,text="${0:.2f}".format(total_current_value),bg="#F3F4F6",fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
    current_val.grid(row=coin_row,column=4,sticky=N+S+E+W)
    price=Label(pycrypto,text="${0:.2f}".format(total_price),bg="#F3F4F6",fg="black",font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
    price.grid(row=coin_row,column=1,sticky=N+S+E+W)
    api=""
    update=Button(pycrypto,text="Update",bg="#142E54",fg="white",command=my_portfolio,font="Lato 12",padx="2",pady="2",borderwidth=2,relief="groove")
    update.grid(row=coin_row+1,column=6,sticky=N+S+E+W)   

name=Label(pycrypto,text="Coin Name",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
name.grid(row=0,column=0,sticky=N+S+E+W)

price=Label(pycrypto,text="Price",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
price.grid(row=0,column=1,sticky=N+S+E+W)

no_coins=Label(pycrypto,text="Coins Owned",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
no_coins.grid(row=0,column=2,sticky=N+S+E+W)

amount_paid=Label(pycrypto,text="Total Amount Paid",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
amount_paid.grid(row=0,column=3,sticky=N+S+E+W)

current_val=Label(pycrypto,text="Current Value",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
current_val.grid(row=0,column=4,sticky=N+S+E+W)

pl_coin=Label(pycrypto,text="P/L per coin",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
pl_coin.grid(row=0,column=5,sticky=N+S+E+W)

total_pl_co=Label(pycrypto,text="Total P/L per coin",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
total_pl_co.grid(row=0,column=6,sticky=N+S+E+W)

my_portfolio()

pycrypto.mainloop()

cobj.close()
con.close()
print("Program completed")