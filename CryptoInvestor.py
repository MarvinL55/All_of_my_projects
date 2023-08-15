from tkinter import *

window = Tk()

window.geometry("500x400")

label = Label(window, text="How much made", font=12)
label.pack(pady=157)

startedWith = Label(window, text="how much started with", font=12)
startedWith.place(x=5, y=5)

howmuchhave = Label(window, text="how much have", font=12)
howmuchhave.place(x=365, y=5)

button = Button(window, text="Invest", font=7)
button.place(x=5, y=365)

stopbutton = Button(window, text="Stop", font=7)
stopbutton.place(x=450, y=365)

window.mainloop()