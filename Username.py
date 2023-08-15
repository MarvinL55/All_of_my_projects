from getpass import getpass
from tkinter import *
import maskpass

def Log():
    print("You've logged in")

def Sign():
    print("You just signed up")

window = Tk()

userlabel = Label(text="Username:", font="Verdana")
userlabel.place(x=1, y=20)

usertext = Text(height=0, width=20)
usertext.place(x=130, y=30)

passlabel = Label(text="Password:", font="Verdana")
passlabel.place(x=1, y=100)

passtext = Text(height=0, width=20)
passtext.place(x=130, y=108)

button = Button(text="Log in", font="Verdana", command=Log)
button.place(x=5, y=155)

signbutton = Button(text="Sign up", font="Verdana", command=Sign)
signbutton.place(x=245, y=155)

window.geometry("350x200")
window.mainloop()