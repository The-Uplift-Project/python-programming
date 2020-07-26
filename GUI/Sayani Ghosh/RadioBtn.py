from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Lets make Radio Buttons.")
root.iconbitmap("disneyland.ico")

r = IntVar()
r.set("3")
# r can also be a string var depending on value type


def clicked(value):
    my_Label = Label(root, text="You clicked option : "+str(value))
    my_Label.pack()


Radiobutton(root, text="Option 1", variable=r, value=1).pack()
Radiobutton(root, text="Option 2", variable=r, value=2).pack()
Radiobutton(root, text="Option 3", variable=r, value=3).pack()

my_Button = Button(root, text="Click!", command=lambda: clicked(r.get()))
my_Button.pack()

root.mainloop()
