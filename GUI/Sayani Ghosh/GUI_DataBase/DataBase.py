from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("Hi")
root.iconbitmap("disneyland.ico")
root.geometry("200x200")

# DataBases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create Table
c.execute("""CREATE TABLE addresses (
        fname text, 
        lname text,
        ad text,
        city text,
        state text,
        zipcode integer
        )""")

# Commit changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()
