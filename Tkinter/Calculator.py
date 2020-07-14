from tkinter import *
root = Tk()
root.title("Calculator")

e = Entry(root, width=50, bg="pink", fg="black", borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# e.insert(0,"")



def button_clr():
    e.delete(0, END)


def button_click(num):
    # e.delete(0,END)
    cur = e.get()
    e.delete(0,END)
    e.insert(0, str(cur) + str(num))


def button_add():
    first_num = e.get()
    global fnum
    fnum = float(first_num)
    e.delete(0, END)
    global val
    val="+"


def button_sub():
    first_num = e.get()
    global fnum
    fnum = float(first_num)
    e.delete(0, END)
    global val
    val="-"


def button_mul():
    first_num = e.get()
    global fnum
    fnum = float(first_num)
    e.delete(0, END)
    global val
    val="x"


def button_div():
    first_num = e.get()
    global fnum
    fnum = float(first_num)
    e.delete(0, END)
    global val
    val="/"



def button_eq():
    second_num = e.get()
    if(float(second_num)==0):
        global val
        val="0e"
    e.delete(0, END)
    if(val == "+"):
        e.insert(0, fnum + float(second_num))
    if(val == "-"):
        e.insert(0, fnum - float(second_num))
    if(val == "x"):
        e.insert(0, fnum * float(second_num))
    if(val == "/"):
        e.insert(0, fnum / float(second_num))
    if(val == "0e"):
        e.insert(0, "Cannot Divide By 0")


button1 = Button(root, bg="#87ceeb", fg="black", text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, bg="#87ceeb", fg="black", text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, bg="#87ceeb", fg="black", text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, bg="#87ceeb", fg="black", text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, bg="#87ceeb", fg="black", text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, bg="#87ceeb", fg="black", text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, bg="#87ceeb", fg="black", text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, bg="#87ceeb", fg="black", text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, bg="#87ceeb", fg="black", text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, bg="#87ceeb", fg="black", text="0", padx=40, pady=20, command=lambda: button_click(0))
buttonadd = Button(root, bg="#87ceeb", fg="black", text="+", padx=40, pady=20, command=lambda: button_add())
buttonsub = Button(root, bg="#87ceeb", fg="black", text="-", padx=40, pady=20, command=lambda: button_sub())
buttonmul = Button(root, bg="#87ceeb", fg="black", text="x", padx=40, pady=20, command=lambda: button_mul())
buttondiv = Button(root, bg="#87ceeb", fg="black", text="/", padx=40, pady=20, command=lambda: button_div())
buttoneq = Button(root, bg="#87ceeb", fg="black", text="=", padx=95, pady=20, command=lambda: button_eq())
buttonclr = Button(root, bg="#87ceeb", fg="black", text="CLR", padx=90, pady=20, command=lambda: button_clr())

# put buttons on screen

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonadd.grid(row=6, column=0)

buttoneq.grid(row=5, column=1, columnspan=2)
buttonclr.grid(row=6, column=1, columnspan=2)

buttonsub.grid(row=5, column=0)
buttonmul.grid(row=4, column=1)
buttondiv.grid(row=4, column=2)

root.mainloop()
