from tkinter import *

root=Tk()
#adding title of GUI
root.title("learning......")

#creating the widget
frame=LabelFrame(root,text="This is my frame",padx=70,pady=70,bg="#93b5e1")
frame.pack(padx=100,pady=100)

#entry widget
entry=Entry(frame,border=5,width=35)
entry.pack()

#adding the widget to the frame
b=Button(frame,text="Here's your Quote...")
b.pack()

#closing the main_loop
root.mainloop()
