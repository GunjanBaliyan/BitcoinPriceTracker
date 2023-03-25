import requests as requests
import tkinter as tk
from datetime import datetime


def trackbitcoin():
    # api to fetch the price of the bitcoin
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text=str(price)+"$")
    labelTime.config(text="Updated at: "+time)

    canvas.after(1000, trackbitcoin)

# define the UI
canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("BITCOIN TRACKER")

f1 = ("poppins", 24, "bold")
f2 = ("poppins", 22, "bold")
f3 = ("poppins", 18, "bold")

label = tk.Label(canvas, text= "Bitcoin Price", font =f1)
label.pack(pady=20)

labelPrice = tk.Label(canvas,font=f2)
labelPrice.pack(pady=20)

labelTime = tk.Label(canvas, font=f3)
labelTime.pack(pady=20)

trackbitcoin()

canvas.mainloop()

