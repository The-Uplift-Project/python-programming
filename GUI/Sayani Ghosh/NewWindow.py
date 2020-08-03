from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello")
root.iconbitmap("disneyland.ico")


def open():
    global my_img
    top = Toplevel()
    top.titleS("Second Window")
    top.iconbitmap("disneyland.ico")
    # lbl = Label(top, text="Hi").pack()
    my_img = ImageTk.PhotoImage(Image.open("disneyland.png"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy)
    btn2.pack()


btn = Button(root, text="Click to open second window !", padx=50, pady=50, command=open)
btn.pack()


root.mainloop()
