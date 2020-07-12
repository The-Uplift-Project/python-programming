# Buttons 

from tkinter import *

root = Tk()

enter = Entry(root, width = 50)
enter.pack()
enter.insert(1, "Enter your name: ")

def onClick():
	greet = "Hello " + enter.get()
	myLabel = Label(root, text = greet)
	myLabel.pack()

myButton = Button(root, text = "Click me", command = onClick)
# myButton = Button(root, text = "Click me", state = DISABLED, padx = 20, pady = 20, fg = "blue", bg = "red")

myButton.pack()

root.mainloop()