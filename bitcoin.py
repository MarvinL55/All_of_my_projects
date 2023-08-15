import requests
import tkinter as tk
import datetime

def trackBitcoin():
    url="https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/historical"
    response = requests.get(url).json()
    price = response["USD"]
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    labelPrice.config(text=str(price) + " $")
    labelTime.config(text="Updated at: " + current_time)
    canvas.after(1000, trackBitcoin)

canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Bitcoin tracker")

f1 = ("poppins", 24, "bold")
f2 = ("poppins", 22, "bold")
f3 = ("poppins", 18, "normal")

label = tk.Label(canvas, text="Bitcoin Price", font=f1)
label.pack(pady=20)

labelPrice = tk.Label(canvas, font=f2)
labelPrice.pack(pady=20)

labelTime = tk.Label(canvas, font=3)
labelTime.pack(pady=20)

trackBitcoin()

canvas.mainloop()

