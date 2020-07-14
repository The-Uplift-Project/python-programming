from tkinter import *

root = Tk()

myLabel0 = Label(root, text="Enter Your Name !")
myLabel0.pack()

e=Entry(root,width=50,fg="black",bg="pink",borderwidth=10)
e.pack()
e.insert(0,"Enter Your Name")
def myClick():
    myLabel = Label(root,text="Hello There ! "+ e.get())
    myLabel.pack()

myButton = Button(root,text="Click me",command=myClick,fg="blue",bg="pink")

myButton.pack()

root.mainloop()