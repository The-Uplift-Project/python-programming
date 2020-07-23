from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Hello")
root.iconbitmap("disneyland.ico")
root.geometry("200x200")


def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 200)
    plt.show()
    # can also be polar or pie etc.


btn = Button(root, text="Create Graph", command=graph)
btn.pack()

root.mainloop()
