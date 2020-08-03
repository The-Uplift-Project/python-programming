from tkinter import *
from PIL import ImageTk, Image

# py -m pip ...(for installing pillow)

root = Tk()

root.title("Hi")
root.iconbitmap("disneyland.ico")

myimg = ImageTk.PhotoImage(Image.open("disneyland.png"))
my_label = Label(image=myimg)
my_label.pack()


button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()
