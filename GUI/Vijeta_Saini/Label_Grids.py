from tkinter import *

root=Tk()

#Creating a Label Widget
#label to print "Hello World"
myLabel1=Label(root,text="Hello World")
#label to print the text value
myLabel2=Label(root,text="I'm Vijeta Saini")

#Showing it onto the screen
#Grid sets the position of the widget
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=2)

#closing the mainloop for the program to end
root.mainloop()
