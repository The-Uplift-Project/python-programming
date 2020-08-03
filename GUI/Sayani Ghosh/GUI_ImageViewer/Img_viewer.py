from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Hi")
root.iconbitmap("disneyland.ico")

my_img1 = ImageTk.PhotoImage(Image.open("disneyland.png"))
my_img2 = ImageTk.PhotoImage(Image.open("cartoon.png"))
my_img3 = ImageTk.PhotoImage(Image.open("message.png"))
my_img4 = ImageTk.PhotoImage(Image.open("panda.png"))
my_img5 = ImageTk.PhotoImage(Image.open("money-bag.png"))

img_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

stat = Label(root, text="Image 1 of "+str(len(img_list)), bd=1, bg="pink", fg="black", relief=SUNKEN)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def fwd(i_num):
    global my_label
    global button_fwd
    global button_bck

    my_label.grid_forget()
    my_label = Label(image=img_list[i_num-1])

    my_label.grid(row=0, column=0, columnspan=3)
    button_fwd = Button(root, text=">>", command=lambda: fwd(i_num+1))
    button_bck = Button(root, text="<<", command=lambda: bck(i_num-1))

    if i_num == 5:
        button_fwd = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_bck.grid(row=1, column=0)
    button_fwd.grid(row=1, column=2)

    stat = Label(root, text="Image "+str(i_num)+" of " + str(len(img_list)), bd=1, bg="pink", fg="black", relief=SUNKEN)
    stat.grid(row=2, column=0, columnspan=3, sticky=W + E)


def bck(i_num):
    global my_label
    global button_fwd
    global button_bck

    my_label.grid_forget()
    my_label = Label(image=img_list[i_num - 1])

    my_label.grid(row=0, column=0, columnspan=3)
    button_fwd = Button(root, text=">>", command=lambda: fwd(i_num + 1))
    button_bck = Button(root, text="<<", command=lambda: bck(i_num - 1))

    if i_num == 1:
        button_bck = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_bck.grid(row=1, column=0)
    button_fwd.grid(row=1, column=2)

    stat = Label(root, text="Image " + str(i_num) + " of " + str(len(img_list)), bd=1, bg="pink", fg="black", relief=SUNKEN)
    stat.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_bck = Button(root, text="<<", command=lambda: bck)
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_fwd = Button(root, text=">>", command=lambda: fwd(2))

button_bck.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_fwd.grid(row=1, column=2, pady=10)
stat.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
