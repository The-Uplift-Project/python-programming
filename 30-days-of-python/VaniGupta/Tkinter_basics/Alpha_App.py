from tkinter import *
import pygame
import pyttsx3
from PIL import ImageTk, Image


# pygame.init()
engine = pyttsx3.init()
root = Tk()

root.title("Alphabet application")
root.geometry('1038x587+100+100')

root.config(background = 'white')
str1 = StringVar()

str1.set('Alphabet application for kids!')
frame1 = Frame(root, bg = 'white')
frame1.grid()

disp = Canvas(frame1, width = 135, height = 120)
disp.grid(row = 1, column = 3)
img = ImageTk.PhotoImage(Image.open("pic.jpg"))
image = disp.create_image(80, 160, image = img)

#=============================Button===========================#

def alpha(s):

	str1.set("Letter pressed: {}".format(s))
	engine.say("Letter pressed: {}".format(s))
	engine.runAndWait()

def clear():

	str1.set('Alphabet application for kids!')
	engine.say('Alphabet application for kids!')
	engine.runAndWait()
  
#==========================Main Screen=========================#

display = Entry(frame1, text = str1, font = ('chiller', 44, 'bold'),\
	bg = 'light yellow', fg = 'black', bd = 14, justify = CENTER, width = 36)
display.grid(row = 0, column = 0, columnspan = 7)

