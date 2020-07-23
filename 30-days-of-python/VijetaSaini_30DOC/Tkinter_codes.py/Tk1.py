#button,labels,entry,frame


import tkinter as tk

HEIGHT=700
WIDTH=800

root=tk.Tk()
canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

frame=tk.Frame(root,bg="#80c1ff")
frame.place(relwidth=0.5,relheight=0.5,relx=0.1,rely=0.1)


button=tk.Button(frame,text="Test button",bg='gray',fg='black')
button.grid(row=5,column=9)

label=tk.Label(frame,text="This is a label",bg="#6c84b8")
label.grid(row=10,column=9)

entry=tk.Entry(frame,bg="gray")
entry.grid(row=15,column=9)

root.mainloop()
