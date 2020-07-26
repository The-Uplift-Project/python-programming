from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Hello")
root.iconbitmap("disneyland.ico")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/PycharmProjects/code1/imgs", title="File", filetypes=(("*.jpg", "jpg files"),("*.png", "png files"), ("all files","*.*")))
    my_lbl = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_img_lbl = Label(image=my_image).pack()


btn = Button(root, text="click to open file", command=open).pack()

root.mainloop()
