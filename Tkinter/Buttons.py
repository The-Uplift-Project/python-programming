from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root,text="Look ! Button Works ")
    myLabel.pack()

myButton = Button(root,text="Click me",command=myClick,fg="blue",bg="pink")

myButton.pack()

#state=DISABLED (button wont do anything)
#padx, pady size changing of buttons


root.mainloop()