from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Lets make Radio Buttons.")
root.iconbitmap("disneyland.ico")

MODES = [
    ("Tony Stark", "Iron Man"),
    ("Pepper Potts", "Iron Woman"),
    ("Morgan Stark", "Iron Princess"),
]

character = StringVar()
character.set("1")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=character, value=mode).pack()


def clicked(mode):
    my_Label = Label(root, text="You selected : "+str(mode))
    my_Label.pack()


my_Button = Button(root, text="Click!", command=lambda: clicked(character.get()))
my_Button.pack()

root.mainloop()
