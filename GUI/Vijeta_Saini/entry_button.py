from tkinter import *

root=Tk()

#label is used here to take the input from the user
entry=Entry(root,fg="#050505",bg="#b2ebf2",border=4,width=35)
#pack to dispaly it on screen
entry.pack()
#to write a placeholder
entry.insert(0,"Enter your quote here")

def myClick():
    text_print="Your Quote:  "+ entry.get()     #entry.get takes the value entered by the user
    myLabel=Label(root,text=text_print)
    myLabel.pack()

# function def is called in button ,so that on clicking the button 
#it performs the operations written inside the function
myButton=Button(root,text="Click Here!",fg="white",bg="#322f3d",command=myClick)

#pack() is used to display the button on the screen
myButton.pack()

root.mainloop()
