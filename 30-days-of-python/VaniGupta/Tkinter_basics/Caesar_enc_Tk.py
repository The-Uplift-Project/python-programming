from tkinter import *

root = Tk()

def encrypt():
    txt = text.get("1.0", END)
    key = int(enter_key.get())
    enc_text = ""

    for index in range(len(txt)):

        if txt[index].isalpha():
            if txt[index].isupper():
                temp = (ord(txt[index]) - ord('A') + key) % 26 + ord('A')
                enc_text += chr(temp)

            elif txt[index].islower():
                temp = (ord(txt[index]) - ord('a') + key) % 26 + ord('a')
                enc_text += chr(temp)
        else:
            enc_text += txt[index]

    encr_text.insert(1.0, enc_text)


enter_label = Label(root, text = "Enter text: ")
enter_label.grid(row = 3, column = 0)

text = Text(root, width = 20, height = 10, bg = "light cyan")
text.grid(row = 3, column = 1, columnspan = 2)

key_label = Label(root, text = "Enter key: ")
key_label.grid(row = 4, column = 0, padx = 10, pady = 10)

enter_key = Entry(root, width = 5)
enter_key.grid(row = 4, column = 1)

enc = Button(root, text = "Encrypt", command = encrypt)
enc.grid(row = 5, column = 1)

encr_text = Text(root, width = 20, height = 10, bg = "light yellow")
encr_text.grid(row = 6, column = 1, columnspan = 2, padx = 10, pady = 10)


root.mainloop()
