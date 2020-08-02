from tkinter import *
from PIL import ImageTk,Image
import random


root = Tk()
root.title("Message Encoder - Decoder")
root.config(bg="skyblue")
root.geometry("1200x1200")
key_table={'A':['D','9'],'B':'X','C':'S','D':'F','E':['Z','7','2','1'],'F':'E','G':'H','H':'C','I':['V','3'],'J':'I','K':'T','L':'P','M':'G','N':['A','5'],'O':['Q','0'],'P':'L','Q':'K','R':'J','S':['R','4'],'T':['U','6'],'U':'O','V':'W','W':'M','X':'Y','Y':'B','Z':'N'}

def caeserencrypt():
    global myLabel
    s = e.get()
    e.delete(0, 'end')
    en=""

    for letter in s:
        if letter.isupper():
             en+= chr((ord(letter) + 3-65) % 26 + 65)
        else:
            en += chr((ord(letter) + 3 - 97) % 26 + 97)
    
    myLabel = Label(root, text=en,font="none 20 bold")
    myLabel.grid(row=3,column=2, padx=5, pady=5)

def caeserdecrypt():
    global myLabel
    s = e1.get()
    e1.delete(0, 'end')
    d=""
    for letter in s:
        if letter.isupper():
             d+= chr((ord(letter) + 23-65) % 26 + 65)
        else:
            d+= chr((ord(letter) + 23 - 97) % 26 + 97)
    myLabel = Label(root, text=d)
    myLabel.grid(row=3,column=2, padx=5, pady=5)

def homoencrypt():
    global myLabel
    msg = e.get().upper()
    e.delete(0, 'end')
    enc=""

    for i in msg:
        if i in key_table:
            if isinstance(key_table[i], list):
                enc+=random.choice(key_table[i])
            else:
                enc+=key_table[i]
        else:
            enc+=i

    myLabel = Label(root, text=enc)
    myLabel.grid(row=3,column=2, padx=5, pady=5)

def homodecrypt():
    global myLabel
    enc = e1.get().upper()
    e1.delete(0, 'end')

    dec=""
    for i in enc:
        if i.isalnum():
            k=0
            for j in key_table.values():
                if i in j:
                    break
                k+=1
            dec+=chr(65+k)
        else:
            dec+=i

    myLabel = Label(root, text=dec)
    myLabel.grid(row=3,column=2, padx=5, pady=5)

def generateKey(msg, key): 
    key = list(key) 
    if len(msg) == len(key): 
        return(key) 
    else: 
        for i in range(len(msg) - 
                       len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 

def vigenerencrypt():
    global myLabel
    msg = e.get().upper()
    e.delete(0, 'end')

    dec1 = Label(root, text="Enter the keyword:", bg="skyblue", fg="black", font="none 20 bold")
    dec1.grid(row=2,column=2)
    keyword = Entry(root, width=10, font=('Helvetica', 30))
    keyword.grid(row=2,column=3, padx=5, pady=5)
    key = generateKey(msg, keyword.get()) 
    enc_list = [] 
    for i in range(len(msg)): 
        x = (ord(msg[i]) + 
             ord(key[i])) % 26
        x += ord('A') 
        enc_list.append(chr(x)) 
    enc="" . join(enc_list)

    myLabel = Label(root, text=enc)
    myLabel.grid(row=3,column=2, padx=5, pady=5)

def vigenerdecrypt():
    global myLabel
    enc = e1.get()
    e1.delete(0, 'end')

    dec1 = Label(root, text="Enter the keyword:", bg="skyblue", fg="black", font="none 20 bold")
    dec1.grid(row=2,column=2, padx=5, pady=5)
    keyword = Entry(root, width=10, font=('Helvetica', 30))
    keyword.grid(row=2,column=3, padx=5, pady=5)
    key = generateKey(msg, keyword.get()) 

    dec_list = [] 
    for i in range(len(enc)): 
        x = (ord(enc[i]) - 
             ord(key[i]) + 26) % 26
        x += ord('A') 
        dec_list.append(chr(x)) 
    dec = "" . join(dec_list)

    myLabel = Label(root, text=dec)
    myLabel.grid(row=3,column=2, padx=5, pady=5)



Title = Label(root, text="Welcome to the Message Encoder-Decoder App!", bg="skyblue", fg="white", font="none 28 bold")
Title.config(anchor=CENTER)

enc = Label(root, text="Enter the message to be encoded:", bg="skyblue", fg="black", font="none 20 bold")
e = Entry(root, width=10, font=('Helvetica', 30))
#e.pack()

Title.grid(row=1,column=0, padx=5, pady=5)
enc.grid(row=2,column=0)
e.grid(row=2,column=1)

myButton = Button(root, text="Encode using Caesar Cipher", command= caeserencrypt, padx=10, pady=5)
myButton1 = Button(root, text="Encode using Homophonic Cipher", command= homoencrypt, padx=10, pady=5)
myButton2 = Button(root, text="Encode using Vigener Cipher", command= vigenerencrypt, padx=10, pady=5)

myButton.grid(row=3,column=0, pady=10)
myButton1.grid(row=4,column=0, pady=10)
myButton2.grid(row=5,column=0, pady=10)

dec = Label(root, text="Enter the message to be decoded:", bg="skyblue", fg="black", font="none 20 bold")
e1 = Entry(root, width=10, font=('Helvetica', 30))
#e.pack()

dec.grid(row=7,column=0)
e1.grid(row=7,column=1)

myButton3 = Button(root, text="Decode using Caesar Cipher", command= caeserdecrypt, padx=10, pady=5)
myButton4 = Button(root, text="Decode using Homophonic Cipher", command= homodecrypt, padx=10, pady=5)
myButton5 = Button(root, text="Decode using Vigener Cipher", command= vigenerdecrypt, padx=10, pady=5)

myButton6 = Button(root, text="Clear Screen", command= vigenerdecrypt, padx=10, pady=5)

myButton3.grid(row=8,column=0, pady=10)
myButton4.grid(row=9,column=0, pady=10)
myButton5.grid(row=10,column=0, pady=10)

myButton6.grid(row=11,column=0, pady=10)

root.mainloop()