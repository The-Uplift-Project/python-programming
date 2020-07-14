from tkinter import *
root = Tk()

#craeting label widget
mylabel1 = Label(root,text="Hello !")
mylabel2 = Label(root,text="Welcome to tkinter progarmming.")
mylabel3 = Label(root,text="   Sayani!   ")

#grid_system
mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=5)
mylabel3.grid(row=1,column=2)

#coulumn 5 =1 if prev is blank
#code shortened as
mylabel4 = Label(root,text="Hello !").grid(row=2,column=0)
mylabel5 = Label(root,text="Welcome to tkinter progarmming.").grid(row=3,column=0)
mylabel6 = Label(root,text="   Sayani!   ").grid(row=4,column=0)



root.mainloop()
