from tkinter import *
import time
from tkinter import ttk

root = Tk()
root.geometry('1600x800+0+0')
root.title("Hotel management system")

def btn(numbers):
    global operator
    operator = operator + str(numbers)
    txt_input.set(operator)

def clear():
    global operator
    operator = ''
    txt_input.set('')
    display.insert(0, 'Start calculating...')

def equal():
    global operator
    sumup = float(eval(operator))
    txt_input.set(sumup)
    operator = ''

def totalcost():
    varme1 = meal_box.get()
    varme2 = meal1.get()
    if varme1 == 'Noodles':
        varme3 = (varme2*1.8)
        cost.set(varme3)
    elif varme1 == 'Pizza':
        varme3 = (varme2*2.2)
        cost.set(varme3)
    elif varme1 == 'Springroll':
        varme3 = (varme2*1.5)
        cost.set(varme3)
    elif varme1 == 'Burger':
        varme3 = (varme2*1.3)
        cost.set(varme3)
    else:
        varme3 = varme2*0.0
        cost.set(varme3)

    vardi1 = drink_box.get()
    vardi2 = drink1.get()
    if vardi1 == 'Pepsi':
        vardi3 = (vardi2*1.8)
        drink.set(vardi3)
    elif vardi1 == 'Water':
        vardi3 = (vardi2*2.2)
        drink.set(vardi3)
    elif vardi1 == 'Lemonade':
        vardi3 = (vardi2*1.5)
        drink.set(vardi3)
    elif vardi1 == 'Frooti':
        vardi3 = (vardi2*1.3)
        drink.set(vardi3)
    else:
        vardi3 = vardi2*0.0
        drink.set(vardi3)

    num1 = float(cost.get())
    num2 = float(drink.get())
    deli = (num1 + num2)*0.5


    room1 = v.get()
    null = 0.0
    rvip = 10
    rvip1 = deli/(10*0.5)
    rnormal = 5
    rnormal1 = deli/(5*2.5)

    if room1 == 1:
        if chkbx1.get() == 1:
            service.set(rvip1)
            room.set(10.0)
            delivery.set(deli)
        else:
            service.set(null)
            delivery.set(null)
            room.set(10.0)
    if room1 == 2:
        if chkbx1.get() == 1:
            service.set(rnormal)
            room.set(5.0)
            delivery.set(deli)
        else:
            service.set(null)
            delivery.set(null)
            room.set(5.0)
    if room1 == 3:
        if chkbx1.get() == 1:
            service.set(null)
            room.set(null)
            delivery.set(null)
        else:
            service.set(null)
            delivery.set(null)
            room.set(null)

    num3 = float(delivery.get())
    num4 = float(room.get())
    num5 = float(service.get())
    mytotal = num1+num2+num3+num4+num5
    total.set(mytotal) 
    finaltotal = "Total  = " + str(mytotal) + "$"

    num6 = texttot.get()
    display.delete(0, END)
    display.insert(0, finaltotal)
    if num6 <= '0.0':
        display.delete(0, END)
        display.insert(0, 'Please make an order.')


def convert():
    var2 = indicator.get()
    var3 = var1.get()

    if var2 == 'India':
        display.delete(0, END)
        var4 = ('INR', (var3 * 72.00))
        display.insert(0, var4)
    elif var2 == 'France':
        display.delete(0, END)
        var4 = ('Euro', (var3 * 0.8))
        display.insert(0, var4)
    elif var2 == 'Nigeria':
        display.delete(0, END)
        var4 = ('Naira', (var3 * 365.00))
        display.insert(0, var4)
    else:
        display.insert(0, 'Error: Select a country!')

def clearScreen():
    display.delete(0, END)
    room.set('')
    total.set('')
    service.set('')
    drink.set('')
    cost.set('')
    delivery.set('')
    txtQty.set('')
    txtQty1.set('')

def stop():
    root.destroy()

def exit():
    display.delete(0, END)
    display.insert(0, 'Thanks for patronage...')
    display.after(2000, stop)

def hotel():
    display.delete(0, END)
    display.insert(0, "-- Hotel Tkinter --")

def powered():
    display.delete(0, END)
    display.insert(0, 'Powered by python...')

def reset():
    display.delete(0, END)
    display.insert(0, 'System resetting..')
    display.after(2000, hotel)
    display.after(4000, powered)
    display.after(6000, rst)

def rst():
    clear()
    display.delete(0, END)
    display.insert(0, 'Hotel management')
    meal_box.set(value = 'Food items')
    drink_box.set(value = 'Fresh Drinks')
    indicator.set(value = 'Select a country')
    txtQty.delete(0, END)
    txtQty.insert(0, 0)
    txtQty1.delete(0, END)
    txtQty1.insert(0, 0)
    txtamnt.delete(0, END)
    txtamnt.insert(0, 0)
    room.set(0.0)
    total.set(0.0)
    service.set(0.0)
    drink.set(0.0)
    cost.set(0.0)
    chkbx1.set(0)
    v.set(3)
    delivery.set(0.0)
