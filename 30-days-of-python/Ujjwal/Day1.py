# This Code displays the variety of reliefs in frames. 
# Reliefs are like giving Graphical attributes to your frame

import tkinter as tk

window = tk.Tk()

reliefs = {
    "flat": tk.FLAT,

    "sunken": tk.SUNKEN,

    "raised": tk.RAISED,

    "groove": tk.GROOVE,

    "ridge": tk.RIDGE,


}

for r, feature in reliefs.items():
    frame = tk.Frame(master=window, relief = feature, borderwidth = 5, width = 50, height = 40)
    frame.pack()
    text = tk.Label(master=frame, text = r)
    text.pack()

window.mainloop()