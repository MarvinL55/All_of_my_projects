from tkinter import *
from PIL import ImageTk, Image

window = Tk()

window.geometry("500x500")

frame = Frame(window, width=400, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("1485357.jpg"))

button = Button(window, text="->")
button.pack()

label = Label(frame, image=img)
label.pack()


window.mainloop()