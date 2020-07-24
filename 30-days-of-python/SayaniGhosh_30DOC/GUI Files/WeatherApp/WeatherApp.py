from tkinter import *
from PIL import ImageTk, Image
import requests
import json


root = Tk()
root.title("Weather App")
root.iconbitmap('disneyland.ico')
root.geometry("600x200")
root.configure(background="DeepPink")

# https://api.weatherbit.io/v2.0/current?city=Kolkata,IN&key=620429bf347a484c806cbfe28f59a72c

try:
    api_rq = requests.get("https://api.weatherbit.io/v2.0/current?city=Kolkata,IN&key=620429bf347a484c806cbfe28f59a72c")
    api = json.loads(api_rq.content)
    ap = api["data"]

    mylbl1 = Label(root, background="Pink", padx=70, text="City : " + str(ap[0]['city_name']), font=("Helvetica", 20))
    mylbl1.pack()

    mylbl2 = Label(root, background="Skyblue", padx=3, text="TimeZone : " + str(ap[0]['timezone']),
                   font=("Helvetica", 20))
    mylbl2.pack()

    mylbl3 = Label(root, background="Pink", padx=5, text="Temperature : " + str(ap[0]['temp']) + " deg C",
                   font=("Helvetica", 20))
    mylbl3.pack()

except Exception as e:
    api = "Error"


root.mainloop()
