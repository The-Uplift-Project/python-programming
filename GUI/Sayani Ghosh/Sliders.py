from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello")
root.iconbitmap("disneyland.ico")
root.geometry("400x400")

verti = Scale(root, from_=0, to=100)
verti.pack()

hori = Scale(root, from_=0, to=100, orient=HORIZONTAL)
hori.pack()


def slide():
    my_label1 = Label(root, text="Vertical value: "+str(verti.get())).pack()
    my_label2 = Label(root, text="Vertical value: "+str(hori.get())).pack()


btn = Button(root, text="Click to Slide !", command=slide).pack()

root.mainloop()