# from tkinter import everything
from tkinter import *

# this comes before anything else
root = Tk()

# Creating a Label widget
myLabel = Label(root, text = "Hello")

# Displaying on screen
myLabel.pack()

root.mainloop()
