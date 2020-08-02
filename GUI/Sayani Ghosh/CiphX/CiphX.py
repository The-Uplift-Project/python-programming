from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title("CiphX")
root.iconbitmap('disneyland.ico')
root.geometry("2000x2000")
root.bind('<Escape>', lambda event: root.state('normal'))
root.bind('<F11>', lambda event: root.state('zoomed'))

filename = PhotoImage(file="T2.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

global im1
im1 = ImageTk.PhotoImage(Image.open("ebtn.png"))

global im2
im2 = ImageTk.PhotoImage(Image.open("dbtn.png"))

# Welcome msg
l1 = Label(root, padx=30, text="Welcome  To  CiphX !", font=("Helvetica", 60))
l1.place(x=700, y=100, anchor="center")

k1 = Label(root, padx=5, text="Press F11 : FullScreen", bg="Lightyellow", font=("Helvetica", 10))
k1.place(x=950, y=160)

k2 = Label(root, padx=5, text="Press ESC : NormalScreen", bg="Lightyellow", font=("Helvetica", 10))
k2.place(x=1100, y=160)

# Select Ciphering Method

def sel():
    s = clicked.get()

    # Caesar Cipher
    if s == "Caesar Cipher":
        # caesar cipher

        et = Toplevel()
        et.title("Caesar Cipher")
        et.iconbitmap('disneyland.ico')
        et.configure(bg="Pink")
        et.geometry("2000x2000")
        et.bind('<Home>', lambda event: et.state('normal'))
        et.bind('<F12>', lambda event: et.state('zoomed'))



        def Encode():
            txt = ent1.get()
            sft = int(ent2.get())
            msg = ""
            for i in range(len(txt)):
                ch = txt[i]
                if ch == ' ':
                    msg += ch
                    continue
                if ch.isupper():
                    msg += chr((ord(ch) + sft - 65) % 26 + 65)
                else:
                    msg += chr((ord(ch) + sft - 97) % 26 + 97)

            global lbl
            lbl = Label(et, text="Ciphered Message : "+msg, font=("Helvetica", 25))
            lbl.place(x=700, y=500, anchor="center")

        def Decode():
            txt = ent1.get()
            sft = int(ent2.get())
            msg = ""
            for i in range(len(txt)):
                ch = txt[i]
                if ch == ' ':
                    msg += ch
                    continue
                if ch.isupper():
                    msg += chr((ord(ch) - sft - 65) % 26 + 65)
                else:
                    msg += chr((ord(ch) - sft - 97) % 26 + 97)

            global lbl
            lbl = Label(et, text="Original Message : "+msg, font=("Helvetica", 25))
            lbl.place(x=700, y=500, anchor="center")

        def Ref():
            ent1.delete(0, END)
            ent2.delete(0, END)
            lbl.destroy()

        def Back():
            et.destroy()

        lb = Label(et, padx=30, text="CAESAR CIPHER", font=("Helvetica", 30))
        lb.place(x=700, y=50, anchor="center")

        k1 = Label(et, padx=10, text="Press F12 : FullScreen", bg="Lightyellow", font=("Helvetica", 10))
        k1.place(x=600, y=100, anchor="center")

        k2 = Label(et, padx=10, text="Press Home : NormalScreen", bg="Lightyellow", font=("Helvetica", 10))
        k2.place(x=800, y=100, anchor="center")

        lb1 = Label(et, padx=30, text="Enter Message :", font=("Helvetica", 20))
        lb1.place(x=700, y=150, anchor="center")

        ent1 = Entry(et, width=20, background="Skyblue", borderwidth=3)
        ent1.configure(font=("Helvetica", 20))
        ent1.place(x=700, y=200, anchor="center")

        lb2 = Label(et, padx=30, text="Enter SHIFT Value :", font=("Helvetica", 20))
        lb2.place(x=700, y=250, anchor="center")

        ent2 = Entry(et, width=20, background="Skyblue", borderwidth=3)
        ent2.configure(font=("Helvetica", 20))
        ent2.place(x=700, y=300, anchor="center")

        # Create Button
        btn1 = Button(et, text="ENCODE", borderwidth=0, padx=20, pady=20, command=Encode)
        btn1.configure(font=("Helvetica", 20), image=im1, bg="Pink")
        btn1.place(x=500, y=400, anchor="center")

        btn2 = Button(et, text="DECODE", borderwidth=0, padx=20, pady=20, command=Decode)
        btn2.configure(font=("Helvetica", 20), image=im2, bg="Pink")
        btn2.place(x=900, y=400, anchor="center")

        btn3 = Button(et, text="REFRESH", borderwidth=0, padx=50, pady=10, command=Ref)
        btn3.configure(font=("Helvetica", 10))
        btn3.place(x=600, y=600, anchor="center")

        btn4 = Button(et, text="BACK TO HOMESCREEN", borderwidth=0, padx=10, pady=10, command=Back)
        btn4.configure(font=("Helvetica", 10))
        btn4.place(x=800, y=600, anchor="center")

    # Homophonic Substitution Cipher
    if s == "Homophonic Substitution Cipher":

        et = Toplevel()
        et.title("Homophonic Substitution Cipher")
        et.iconbitmap('disneyland.ico')
        et.configure(bg="Pink")
        et.geometry("2000x2000")
        et.bind('<Home>', lambda event: et.state('normal'))
        et.bind('<F12>', lambda event: et.state('zoomed'))


        def Encode():
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

            txt = ent1.get()
            k = ent2.get()

            li = []
            s = ""
            for i in range(len(k)):
                if k[i] == ' ':
                    li.append(s)
                    s = ""
                    continue
                s += k[i]
                if i == len(k) - 1:
                    li.append(s)

            msg = ""
            for ch in txt:
                if ch in chars:
                    lis = list(li[chars.find(ch)])
                    msg += random.choice(lis)
                else:
                    msg += ch

            global lbl
            lbl = Label(et, text="Ciphered Message : "+msg, font=("Helvetica", 25))
            lbl.place(x=700, y=600, anchor="center")

        def Decode():
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

            txt = ent1.get()
            k = ent2.get()

            li = []
            s = ""
            for i in range(len(k)):
                if k[i] == ' ':
                    li.append(s)
                    s = ""
                    continue
                s += k[i]
                if i == len(k) - 1:
                    li.append(s)

            msg = ""
            for ch in txt:
                if ch == ' ':
                    msg += ch
                    continue
                for i in range(len(li)):
                    lis = list(li[i])
                    if ch in lis:
                        msg += chars[i]

            global lbl
            lbl = Label(et, text="Original Message : "+msg, font=("Helvetica", 25))
            lbl.place(x=700, y=600, anchor="center")

        def Ref():
            ent1.delete(0, END)
            ent2.delete(0, END)
            lbl.destroy()

        def Back():
            et.destroy()

        lb = Label(et, padx=30, text="HOMOPHONIC SUBSTITUTION  CIPHER", font=("Helvetica", 40))
        lb.place(x=700, y=50, anchor="center")

        k1 = Label(et, padx=10, text="Press F12 : FullScreen", bg="Lightyellow", font=("Helvetica", 10))
        k1.place(x=600, y=100, anchor="center")

        k2 = Label(et, padx=10, text="Press Home : NormalScreen", bg="Lightyellow", font=("Helvetica", 10))
        k2.place(x=800, y=100, anchor="center")

        lb1 = Label(et, padx=30, text="Enter Message :", font=("Helvetica", 20))
        lb1.place(x=700, y=150, anchor="center")

        ent1 = Entry(et, width=20, background="Skyblue", borderwidth=3)
        ent1.configure(font=("Helvetica", 20))
        ent1.place(x=700, y=200, anchor="center")

        lb2 = Label(et, padx=30, text="Enter Space Seperated KEY \nfor 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' :", font=("Helvetica", 20))
        lb2.place(x=700, y=300, anchor="center")

        ent2 = Entry(et, width=20, background="Skyblue", borderwidth=3)
        ent2.configure(font=("Helvetica", 20))
        ent2.place(x=700, y=400, anchor="center")

        # Create Button
        btn1 = Button(et, text="ENCODE", borderwidth=0, padx=20, pady=20, command=Encode)
        btn1.configure(font=("Helvetica", 20), image=im1, bg="Pink")
        btn1.place(x=500, y=500, anchor="center")

        btn2 = Button(et, text="DECODE", borderwidth=0, padx=20, pady=20, command=Decode)
        btn2.configure(font=("Helvetica", 20), image=im2, bg="Pink")
        btn2.place(x=900, y=500, anchor="center")

        btn3 = Button(et, text="REFRESH", borderwidth=0, padx=50, pady=10, command=Ref)
        btn3.configure(font=("Helvetica", 10))
        btn3.place(x=600, y=650, anchor="center")

        btn4 = Button(et, text="BACK TO HOMESCREEN", borderwidth=0, padx=10, pady=10, command=Back)
        btn4.configure(font=("Helvetica", 10))
        btn4.place(x=800, y=650, anchor="center")

    if s == "Vigenere Cipher":
        # Vigenere cipher

        et = Toplevel()
        et.title("Vigenere Cipher")
        et.iconbitmap('disneyland.ico')
        et.configure(bg="Pink")
        et.geometry("2000x2000")
        et.bind('<Home>', lambda event: et.state('normal'))
        et.bind('<F12>', lambda event: et.state('zoomed'))


        def Encode():
            txt = ent1.get()
            k = ent2.get()

            ls = ""
            i = 0
            while len(ls) != len(txt):
                ls += k[i]
                if i == len(k) - 1:
                    i = 0
                    continue
                i += 1

            st = ""
            for i in range(len(txt)):
                s = ((ord(txt[i]) + ord(ls[i])) % 26) + ord('A')

                st += chr(s)

            global lbl
            lbl = Label(et, text="Ciphered Message : "+st, font=("Helvetica", 25))
            lbl.place(x=700, y=500, anchor="center")

        def Decode():
            txt = ent1.get()
            k = ent2.get()

            ls = ""
            i = 0
            while len(ls) != len(txt):
                ls += k[i]
                if i == len(k) - 1:
                    i = 0
                    continue
                i += 1

            st = ""
            for i in range(len(txt)):
                s = ((ord(txt[i]) - ord(ls[i]) + 26) % 26) + ord('A')
                st += chr(s)

            global lbl
            lbl = Label(et, text="Original Message : "+st, font=("Helvetica", 25))
            lbl.place(x=700, y=500, anchor="center")

        def Ref():
            ent1.delete(0, END)
            ent2.delete(0, END)
            lbl.destroy()

        def Back():
            et.destroy()

        lb = Label(et, padx=30, text="VIGENERE CIPHER", font=("Helvetica", 40))
        lb.place(x=700, y=50, anchor="center")

        k1 = Label(et, padx=10, text="Press F12 : FullScreen", bg="Lightyellow", font=("Helvetica", 10))
        k1.place(x=600, y=100, anchor="center")

        k2 = Label(et, padx=10, text="Press Home : NormalScreen", bg="Lightyellow", font=("Helvetica", 10))
        k2.place(x=800, y=100, anchor="center")

        lb1 = Label(et, padx=30, text="Enter Message :", font=("Helvetica", 20))
        lb1.place(x=700, y=150, anchor="center")

        ent1 = Entry(et, width=20, background="Skyblue", borderwidth=3)
        ent1.configure(font=("Helvetica", 20))
        ent1.place(x=700, y=200, anchor="center")

        lb2 = Label(et, padx=30, text="Enter KEY Value :", font=("Helvetica", 20))
        lb2.place(x=700, y=250, anchor="center")

        ent2 = Entry(et, width=20, background="Skyblue", borderwidth=3)
        ent2.configure(font=("Helvetica", 20))
        ent2.place(x=700, y=300, anchor="center")

        # Create Button

        btn1 = Button(et, borderwidth=0, padx=20, pady=20, command=Encode)
        btn1.configure(font=("Helvetica", 20), image=im1, bg="Pink")
        btn1.place(x=500, y=400, anchor="center")

        btn2 = Button(et, borderwidth=0, padx=20, pady=20, command=Decode)
        btn2.configure(font=("Helvetica", 20), image=im2, bg="Pink")
        btn2.place(x=900, y=400, anchor="center")

        btn3 = Button(et, text="REFRESH", borderwidth=0, padx=50, pady=10, command=Ref)
        btn3.configure(font=("Helvetica", 10))
        btn3.place(x=600, y=600, anchor="center")

        btn4 = Button(et, text="BACK TO HOMESCREEN", borderwidth=0, padx=10, pady=10, command=Back)
        btn4.configure(font=("Helvetica", 10))
        btn4.place(x=800, y=600, anchor="center")

def Close():
    root.destroy()

clicked = StringVar()
clicked.set("Caesar Cipher")

lb = Label(root, padx=10, text="Choose The Ciphering Method :", font=("Helvetica", 25), background="Pink")
lb.place(x=480, y=300, anchor="center")

dd = OptionMenu(root, clicked, "Caesar Cipher", "Homophonic Substitution Cipher", "Vigenere Cipher")
dd.configure(font=("Helvetica", 25), bg="Skyblue", width=27)
dd.place(x=1000, y=300, anchor="center")

b1 = Button(root, width=10, text="Select", command=sel)
b1.configure(font=("Helvetica", 25))
b1.place(x=700, y=400, anchor="center")

b2 = Button(root, width=20, text="Close Window", command=Close)
b2.configure(font=("Helvetica", 15))
b2.place(x=700, y=500, anchor="center")

root.mainloop()
