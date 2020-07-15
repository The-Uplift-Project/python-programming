# Buttons 

from tkinter import *

root = Tk()

def onClick():
	myLabel = Label(root, text = "Clicked it!")
	myLabel.pack()

myButton = Button(root, text = "Click me", command = onClick)
# myButton = Button(root, text = "Click me", state = DISABLED, padx = 20, pady = 20, fg = "blue", bg = "red")

myButton.pack()

root.mainloop()