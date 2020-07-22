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


def edit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    rid = del_box.get()

    c.execute("""UPDATE addresses SET
        fname = :first,
        lname = :last,
        ad = :add,
        city = :city,
        state = :state,
        zipcode = :zipc
    
        WHERE oid = :oid""",
        {
        'first': f_namee.get(),
        'last': l_namee.get(),
        'add': adde.get(),
        'city': citye.get(),
        'state': statee.get(),
        'zipc': zipce.get(),

        'oid': rid
        })

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()
    ed.destroy()

def update():
    global ed
    ed = Tk()
    ed.title("Update Record")
    ed.iconbitmap("disneyland.ico")
    ed.geometry("500x500")

    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    rid = del_box.get()
    # Insert into table
    c.execute("SELECT* FROM addresses WHERE oid="+rid)
    recs = c.fetchall()

    # Create Global
    global f_namee
    global l_namee
    global adde
    global citye
    global statee
    global zipce

    # Create Text Boxes
    f_namee = Entry(ed, width=30)
    f_namee.grid(row=0, column=1, padx=20)

    l_namee = Entry(ed, width=30)
    l_namee.grid(row=1, column=1, padx=20)

    adde = Entry(ed, width=30)
    adde.grid(row=2, column=1, padx=20)

    citye = Entry(ed, width=30)
    citye.grid(row=3, column=1, padx=20)

    statee = Entry(ed, width=30)
    statee.grid(row=4, column=1, padx=20)

    zipce = Entry(ed, width=30)
    zipce.grid(row=5, column=1, padx=20)



    # Create box labels
    f_name_lbl = Label(ed, text="First Name : ", width=30)
    f_name_lbl.grid(row=0, column=0, padx=20)

    l_name_lbl = Label(ed, text="Last Name : ", width=30)
    l_name_lbl.grid(row=1, column=0, padx=20)

    add_lbl = Label(ed, text="Address : ", width=30)
    add_lbl.grid(row=2, column=0, padx=20)

    city_lbl = Label(ed, text="City : ", width=30)
    city_lbl.grid(row=3, column=0, padx=20)

    state_lbl = Label(ed, text="State : ", width=30)
    state_lbl.grid(row=4, column=0, padx=20)

    zipc_lbl = Label(ed, text="ZipCode : ", width=30)
    zipc_lbl.grid(row=5, column=0, padx=20)

    del_lbl = Label(ed, text="Select ID : ")
    del_lbl.grid(row=9, column=0)

    # Loop through results
    for rec in recs:
        f_namee.insert(0, rec[0])
        l_namee.insert(0, rec[1])
        adde.insert(0, rec[2])
        citye.insert(0, rec[3])
        statee.insert(0, rec[4])
        zipce.insert(0, rec[5])

    # Create Save Btn
    s_btn = Button(ed, text="Save", command=edit)
    s_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=137)



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

del_lbl = Label(root, text="Select ID : ")
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

# Create Edit Btn
ed_btn = Button(root, text="Update Record", command=update)
ed_btn.grid(row=12, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# Commit changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()
