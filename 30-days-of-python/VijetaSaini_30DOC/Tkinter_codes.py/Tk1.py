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
button.pack(side="left",fill="x",expand=True)

label=tk.Label(frame,text="This is a label",bg="#6c84b8")
label.pack(side="right",fill="both")

entry=tk.Entry(frame,bg="gray")
entry.pack(side="bottom",fill="both")

root.mainloop()
