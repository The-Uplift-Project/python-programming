from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("Hi")
root.iconbitmap("disneyland.ico")
root.geometry("500x500")

# DataBases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()


def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid="+del_box.get())
    del_box.delete(0, END)

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()

def Submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :add, :city, :state, :zipc)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'add': add.get(),
                'city': city.get(),
                'state': state.get(),
                'zipc': zipc.get()
            })

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()

    # clear TextBoxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    add.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipc.delete(0, END)


def show():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("SELECT*, oid FROM addresses")
    recs = c.fetchall()
    # print(recs)

    # Loop through records
    p = ""
    for rec in recs:
        p += "    Sr. No : "+str(rec[6])+"    Name : "+str(rec[0])+" "+str(rec[1])+"    Address : "+str(rec[2])+\
        "    City : "+str(rec[3])+"    State : "+str(rec[4])+"    ZipCode : "+str(rec[5])+"\n\n "

    q_lbl = Label(root, text=p)
    q_lbl.grid(row=14, column=0, columnspan=2)

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()



# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

add = Entry(root, width=30)
add.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipc = Entry(root, width=30)
zipc.grid(row=5, column=1, padx=20)

del_box = Entry(root, width=30)
del_box.grid(row=9, column=1)


# Create box labels
f_name_lbl = Label(root, text="First Name : ", width=30)
f_name_lbl.grid(row=0, column=0, padx=20)

l_name_lbl = Label(root, text="Last Name : ", width=30)
l_name_lbl.grid(row=1, column=0, padx=20)

add_lbl = Label(root, text="Address : ", width=30)
add_lbl.grid(row=2, column=0, padx=20)

city_lbl = Label(root, text="City : ", width=30)
city_lbl.grid(row=3, column=0, padx=20)

state_lbl = Label(root, text="State : ", width=30)
state_lbl.grid(row=4, column=0, padx=20)

zipc_lbl = Label(root, text="ZipCode : ", width=30)
zipc_lbl.grid(row=5, column=0, padx=20)

del_lbl = Label(root, text="Delete ID : ")
del_lbl.grid(row=9, column=0)

# Create Query Button
q_btn = Button(root, text="Show Records", command=show)
q_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


# Create Submit Btn

submit_btn = Button(root, text="Add Data", command=Submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Create Delete Btn

del_btn = Button(root, text="Delete Record", command=delete)
del_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=137)


# Commit changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()
