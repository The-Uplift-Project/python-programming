from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hi")
root.iconbitmap("disneyland.ico")
root.geometry("200x200")


def show():
    my_Label = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text="Choose", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

myButton = Button(root, text="Click to select !", command=show).pack()

root.mainloop()
