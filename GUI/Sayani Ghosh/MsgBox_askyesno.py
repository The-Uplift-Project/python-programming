from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Lets make Radio Buttons.")
root.iconbitmap("disneyland.ico")


def popup():
    response = messagebox.askquestion("Message !", "Hello World")
    # can be messagebox.askyesno too
    # if response == 1:
    if response == "yes":
       Label(root, text="You selected YES").pack()
    # if response == 0:
    if response == "no":
        Label(root, text="You selected NO").pack()


Button(root, text="PopUp(Yes & No)", command=popup).pack()

root.mainloop()
