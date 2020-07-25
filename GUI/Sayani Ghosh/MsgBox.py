from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Lets make Radio Buttons.")
root.iconbitmap("disneyland.ico")


def popup():
    response = messagebox.showinfo("Message !", "Hello World")


Button(root, text="PopUp", command=popup).pack()

root.mainloop()
