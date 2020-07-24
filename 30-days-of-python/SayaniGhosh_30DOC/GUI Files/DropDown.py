from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hi")
root.iconbitmap("disneyland.ico")
root.geometry("200x200")

# DropDown Boxes


def show():
    myLabel = Label(root, text="You selected : "+str(clicked.get())).pack()


options = ["Cheese", "Sauce", "Mayo"]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

my_Btn = Button(root, text="Select", command=show)
my_Btn.pack()

root.mainloop()
