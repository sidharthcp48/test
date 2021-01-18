from tkinter import *
import requests
import json

pycrypto=Tk()
pycrypto.title("My Crypto Portfolio")

name=Label(pycrypto,text="Coin Name",bg="black",fg="white")
name.grid(row=0,column=0,sticky=N+S+E+W)

price=Label(pycrypto,text="Price",bg="black",fg="white")
price.grid(row=0,column=1,sticky=N+S+E+W)

no_coins=Label(pycrypto,text="Coins Owned",bg="black",fg="white")
no_coins.grid(row=0,column=2,sticky=N+S+E+W)

amount_paid=Label(pycrypto,text="Total Amount Paid",bg="black",fg="white")
amount_paid.grid(row=0,column=3,sticky=N+S+E+W)

current_val=Label(pycrypto,text="Current Value",bg="black",fg="white")
current_val.grid(row=0,column=4,sticky=N+S+E+W)

pl_coin=Label(pycrypto,text="P/L per coin",bg="black",fg="white")
pl_coin.grid(row=0,column=5,sticky=N+S+E+W)

total_pl=Label(pycrypto,text="Total P/L per coin",bg="black",fg="white")
total_pl.grid(row=0,column=6,sticky=N+S+E+W)
pycrypto.mainloop()