from tkinter import *

count = 0

def button():
  global count

  print(count)
  count+=1


window = Tk()

button = Button(window, text="Click me", command=button)

button.pack()

window.mainloop()