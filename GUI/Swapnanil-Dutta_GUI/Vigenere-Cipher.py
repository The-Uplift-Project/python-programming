from tkinter import *
  
root = Tk()
root.title('Vigenere Cipher')
frm = Frame(root)
frm.grid(row = 3, column = 1)
variable1 = StringVar(root) 
variable2 = StringVar(root)
variable3 = StringVar(root) 
var = StringVar(root)

variable1.set("Text") 
variable2.set("Text") 
variable2.set("Text") 

def clear_all() : 
    Text_field.delete(0, END)  
    Keyword_field.delete(0, END)
    Result_field.delete(0, END)

def keygen(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - 
                       len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 

def converter(string, key, encrypt=0):
    result = [] 
    for i in range(len(string)):
        if encrypt==1: 
            x = (ord(string[i]) + ord(key[i])) % 26
        else:
            x = (ord(string[i]) - ord(key[i]) + 26) % 26
        x += ord('A') 
        result.append(chr(x)) 
    return("" . join(result))

def driver():
    choice = var.get()
    text = Text_field.get()
    keyword = Keyword_field.get()
    key = keygen(text, keyword)
    if choice == 'Encrypt':
        result = converter(text, key, 1)
    else:
        result = converter(text, key)

    Result_field.insert(0,result)

if __name__ == "__main__" :
    root.configure(background = 'light grey')  
    root.geometry("400x200")  

    headlabel = Label(root, text = 'Real Time Text Encrypter/Decrypter', fg = 'black', bg='light grey')   
    label1 = Label(root, text = "Text to be converted :", fg = 'black', bg='light grey') 
    label2 = Label(root, text = "Keyword :", fg = 'black', bg='light grey')
    label3 = Label(root, text = "Operation :", fg = 'black', bg='light grey')  
    label4 = Label(root, text = "Converted Text :", fg = 'black', bg='light grey') 

    Text_field = Entry(root)  
    Keyword_field = Entry(root)
    Result_field = Entry(root)

    encrypt= Radiobutton(frm, text='Encrypt', variable=var)
    encrypt.config(indicatoron=0, bd=4, width=8, value='Encrypt')

    decrypt= Radiobutton(frm, text='Decrypt', variable=var)
    decrypt.config(indicatoron=0, bd=4, width=8, value='Decrypt')

    headlabel.grid(row = 0, column = 1, ipady ="5")
    label1.grid(row = 1, column = 0, ipadx ="25", ipady ="5")  
    label2.grid(row = 2, column = 0, ipadx ="25", ipady ="5") 
    label3.grid(row = 3, column = 0, ipadx ="25", ipady ="5")
    label4.grid(row = 4, column = 0, ipadx ="25", ipady ="5") 

    Text_field.grid(row = 1, column = 1, ipadx ="25")  
    Keyword_field.grid(row = 2, column = 1, ipadx ="25")
    Result_field.grid(row = 4, column = 1, ipadx ="25") 

    encrypt.grid(row=3, column=1)    
    decrypt.grid(row=3, column=2)

    button2 = Button(root, text = "Clear", bg = "light blue", fg = "black", command = clear_all) 
    button2.grid(row = 5, column = 0, ipadx ="10", ipady ="5") 

    button1 = Button(root, text = "Convert", bg = "light green", fg = "black", command = driver) 
    button1.grid(row = 5, column = 1, ipadx ="10", ipady ="5")

    root.mainloop() 