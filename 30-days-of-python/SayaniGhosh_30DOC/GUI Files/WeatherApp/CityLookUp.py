from tkinter import *
from PIL import ImageTk, Image
import requests
import json


root = Tk()
root.title("Weather App")
root.iconbitmap('disneyland.ico')
root.geometry("400x200")
root.configure(background="DeepPink")

global c
# create zlook
def clook():
    #c = c.get()
    #cl = Label(root, text=c)
    #cl.grid(row=1, column=0, columnspan=2)

    # https://api.weatherbit.io/v2.0/current?city=Kolkata,IN&key=620429bf347a484c806cbfe28f59a72c

    try:
        api_rq = requests.get("https://api.weatherbit.io/v2.0/current?city="+c.get()+",IN&key=620429bf347a484c806cbfe28f59a72c")
        api = json.loads(api_rq.content)
        ap = api["data"]

        mylbl1 = Label(root, background="Pink", text="City : " + str(ap[0]['city_name']),
                       font=("Helvetica", 20))
        mylbl1.grid(row=1, column=0, columnspan=2, stick=N+W+E+S)

        mylbl2 = Label(root, background="Skyblue", text="TimeZone : " + str(ap[0]['timezone']),
                       font=("Helvetica", 20))
        mylbl2.grid(row=2, column=0, columnspan=2, stick=N+W+E+S)

        mylbl3 = Label(root, background="Pink", text="Temperature : " + str(ap[0]['temp']) + " deg C",
                       font=("Helvetica", 20))
        mylbl3.grid(row=3, column=0, columnspan=2, stick=N+W+E+S)

    except Exception as e:
        api = "Error"


c = Entry(root)
c.grid(row=0, column=0, stick=N+W+E+S)

c_Btn = Button(root, text="Lookup City", command=clook)
c_Btn.grid(row=0, column=1, stick=N+W+E+S)

root.mainloop()
