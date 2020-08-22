# #import sys
# #print(sys.version)
# import tkinter as tk

# import tkinter as tk

# window = tk.Tk()

# import tkinter as tk

# window = tk.Tk()

# frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
# frame1.pack(fill=tk.Y, side=tk.LEFT)

# frame2 = tk.Frame(master=window, width=100, bg="yellow")
# frame2.pack(fill=tk.Y, side=tk.LEFT)

# frame3 = tk.Frame(master=window, width=50,height = 50, bg="blue")
# frame3.pack()

# window.mainloop()


# window.mainloop()
import tkinter as tk

window = tk.Tk()
main_frame = tk.Frame(master=window,
            relief=tk.RAISED,
            borderwidth=1)
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=main_frame,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()
window.mainloop()