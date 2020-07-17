import tkinter as tk

# temperature converter logic
def temp_converter():
    FAHRENHEIT = entry.get()
    CELSIUS = round((float(FAHRENHEIT)-32)*(5/9))
    lbl_result['text'] = str(CELSIUS)+lbl_result['text']

#defining window and its attributes
window = tk.Tk()
window.title("Temperature Converter")

frame = tk.Frame(master=window)
entry = tk.Entry(master=frame, width=10)
lbl_temp = tk.Label(master=frame, text="\N{DEGREE FAHRENHEIT}")

#arranging in grid
entry.grid(row=0, column=0, sticky='e')
lbl_temp.grid(row=0, column=1, sticky='w', padx=10)
frame.grid(row=0, column=0, padx=10, pady=10)

#button
button = tk.Button(
    master=frame,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=temp_converter
)

#defining and arranging label that will display result
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
button.grid(row=0,column=2, sticky='w', padx=10, pady=10)
lbl_result.grid(row=0, column=3, sticky='w')


window.mainloop()
