import tkinter as tk

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("My GUI")

        self.label = tk.Label(master, text="")
        self.label.pack()

        self.button = tk.Button(master, text="Click me!", command=self.display_message)
        self.button.pack()

    def display_message(self):
        self.label.config(text="Hello, world!")

root = tk.Tk()
my_gui = MyGUI(root)
root.mainloop()
