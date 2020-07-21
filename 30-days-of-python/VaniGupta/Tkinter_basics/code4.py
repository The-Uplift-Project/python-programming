# adding exit buttons, images and icons

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Icon tutorial!")
root.iconbitmap('C:/Users/Vani/Desktop/Girlscript/icon.ico')

img = ImageTk.PhotoImage(Image.open('C:/Users/Vani/Desktop/GHC/cap1.png'))
label = Label(image = img)
label.pack()


quit_button = Button(root, text = "Exit", command = root.quit)
quit_button.pack()

root.mainloop()
