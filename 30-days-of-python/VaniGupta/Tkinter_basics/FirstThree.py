from tkinter import *
import requests
import io
import random
from tkinter import ttk
from time import strftime
from tkinter import ttk
from PIL import ImageTk, Image


root = Tk()
root.geometry('1000x600+100+50')
root.title("Cryptographic Algorithms Application")

# ----------------- Partition -------------------#

left_pane = Frame(root, width = 200, height = 600, relief = SUNKEN)
left_pane.pack(side = LEFT)

main_frame = Frame(root, width = 800, height = 50, relief = SUNKEN, borderwidth = 10)
main_frame.pack()

main = Frame(root, width = 800, height = 400, relief = SUNKEN)
main.pack()

time_frame = Frame(root, width = 800, height = 30, relief = SUNKEN)
time_frame.pack(side = BOTTOM)

label = Label(main_frame, text = "A simple cryptography based application for encrypting and decrypting text.",
	 bd = 10, font = ('fixedsys', 20, 'bold'), wraplength = 500, anchor = CENTER, padx = 20, pady = 20)

canvas = Canvas(left_pane)
frame = Frame(canvas)
myscrollbar = Scrollbar(left_pane, orient = VERTICAL, command = canvas.yview)
canvas.configure(yscrollcommand = myscrollbar.set)

def myfunction(event):
    canvas.configure(scrollregion = canvas.bbox("all"), width = 200, height = 600)

myscrollbar.pack(side = RIGHT, fill = Y)
canvas.pack(side = LEFT)
canvas.create_window((0,0), window = frame, anchor = NW)
frame.bind("<Configure>", myfunction)

def localtime():
	curr_time = strftime('%d - %m - %Y  %A  %H:%M:%S %p ') 
	t1 = Label(time_frame, text = curr_time, font = ('arial', 14, 'bold'), anchor = E)
	t1.after(1000, localtime)
	t1.grid(row = 1, column = 0, columnspan = 2)

def remove():

	label.config(text = "")
	for widget in main.winfo_children():
		widget.destroy()

def show():

	remove()
	label.config(text = "A simple cryptography based application for encrypting and decrypting text.")
	label.grid(row = 0, column = 0)
	localtime()


def caesar_cipher():

	remove()

	label.config(text = "Caesar Cipher")
	label.grid(row = 0, column = 0)

	text_label = Label(main, text = "Enter text: ", font = ('fixedsys', 12, 'bold'))
	text_label.grid(row = 0, column = 0, padx = 20, pady = 20)

	scroll_text = ttk.Scrollbar(main, orient = VERTICAL)
	text_box = Text(main, height = 13, width = 40, pady = 10, yscrollcommand = scroll_text.set)
	text_box.grid(row = 1, column = 0, padx = 10, pady = 10)
	scroll_text.config(command = text_box.yview)
	scroll_text.grid(row = 1, column = 1, sticky = 'NS')

	key_label = Label(main, text = "Enter key: ", font = ('fixedsys', 12, 'bold'))
	key_label.grid(row = 4, column = 0, padx = 20, pady = 30)

	list_key = ttk.Combobox(main)
	list_key['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
	list_key.current(0)
	list_key.grid(row = 5, column = 0)

	scroll_text2 = ttk.Scrollbar(main, orient = VERTICAL)
	new_text = Text(main, height = 13, width = 40, pady = 10, yscrollcommand = scroll_text2.set)
	new_text.grid(row = 1, column = 2, columnspan = 2)
	scroll_text2.config(command = new_text.yview)
	scroll_text2.grid(row = 1, column = 4, sticky = 'NS')

	def encrypt():
		new_text.delete('1.0', END)

		txt = text_box.get("1.0", END)
		key = int(list_key.get())
		enc_text = ""

		for index in range(len(txt)):

			if txt[index].isalpha():
				if txt[index].isupper():
					temp = (ord(txt[index]) - ord('A') + key) % 26 + ord('A')
					enc_text += chr(temp)

				elif txt[index].islower():
					temp = (ord(txt[index]) - ord('a') + key) % 26 + ord('a')
					enc_text += chr(temp)

			else:
				enc_text += txt[index]

		new_text.insert(1.0, enc_text)


	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = encrypt)
	enc.grid(row = 0, column = 2, padx = 20, pady = 10)

	def decrypt():
		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = int(list_key.get())
		dec_text = ""

		for index in range(len(txt)):

			if txt[index].isalpha():
				if txt[index].isupper():
					temp = (ord(txt[index]) - ord('A') - key)
					if temp < 0:
						temp += 26
					temp += ord('A')
					dec_text += chr(temp)

				elif txt[index].islower():
					temp = (ord(txt[index]) - ord('a') - key)
					if temp < 0:
						temp += 26
					temp += ord('a')
					dec_text += chr(temp)

			else:
				dec_text += txt[index]

		new_text.insert(1.0, dec_text)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = decrypt)
	dec.grid(row = 0, column = 3, padx = 10, pady = 10)

	localtime()

def homophonic_cipher():

	remove()
	label.config(text = "Homophonic Cipher")
	label.grid(row = 0, column = 0)

	key_table = {'A':'D9', 'B':'X', 'C':'S', 'D':'F', 'E':'Z721', 'F':'E', 'G':'H', 'H':'C', 'I':'V3',
	'J':'I', 'K':'T', 'L':'P', 'M':'G', 'N':'A5', 'O':'Q0', 'P':'L', 'Q':'K', 'R':'J', 'S':'R4', 'T':'6U', 
	'U':'O', 'V':'W', 'W':'M', 'X':'Y', 'Y':'B', 'Z':'N', 'a':'d(', 'b':'x', 'c': 's', 'd':'f', 'e':'z&@!', 
	'f':'e', 'g':'h', 'h':'c', 'i':'v#', 'j':'i', 'k':'t', 'l':'p', 'm':'g', 'n':'a%', 'o':'q)', 'p':'l', 
	'q':'k', 'r':'j','s':'r$', 't':'^u', 'u':'o', 'v':'w', 'w':'m', 'x':'y', 'y':'b', 'z':'n'}

	text_label = Label(main, text = "Enter text: ", font = ('fixedsys', 12, 'bold'))
	text_label.grid(row = 0, column = 0, padx = 20, pady = 20)

	scroll_text = ttk.Scrollbar(main, orient = VERTICAL)
	text_box = Text(main, height = 20, width = 40, pady = 10, yscrollcommand = scroll_text.set)
	text_box.grid(row = 1, column = 0, padx = 10, pady = 10)
	scroll_text.config(command = text_box.yview)
	scroll_text.grid(row = 1, column = 1, sticky = 'NS')

	scroll_text2 = ttk.Scrollbar(main, orient = VERTICAL)
	new_text = Text(main, height = 20, width = 40, pady = 10, yscrollcommand = scroll_text2.set)
	new_text.grid(row = 1, column = 2, columnspan = 2)
	scroll_text2.config(command = new_text.yview)
	scroll_text2.grid(row = 1, column = 4, sticky = 'NS')

	def encrypt():

		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		enc_text = ""

		for item in txt:
			if item in key_table:
				enc_text += random.choice(key_table[item])
			else:
				enc_text += item

		new_text.insert(1.0, enc_text)
    	
	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = encrypt)
	enc.grid(row = 0, column = 2, padx = 20, pady = 10)

	def decrypt():

		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		dec_text = ""		
		flag = 1
		words = txt.split(" ")

		lst = []
		for item in words:
			lst += item + " "

		for letter in lst:
			if letter == " ":
				dec_text += " "
			else:
				for item in key_table:
					flag = 1
					if letter in key_table[item]:
						dec_text += item
						flag = 0
						break
				if flag == 1:
					dec_text += letter

		new_text.insert(1.0, dec_text)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = decrypt)
	dec.grid(row = 0, column = 3, padx = 10, pady = 10)

	localtime()

def vignere_cipher():

	remove()
	label.config(text = "Vignere Cipher")
	label.grid(row = 0, column = 0)

	text_label = Label(main, text = "Enter text: ", font = ('fixedsys', 12, 'bold'))
	text_label.grid(row = 0, column = 0, padx = 20, pady = 20)

	scroll_text = ttk.Scrollbar(main, orient = VERTICAL)
	text_box = Text(main, height = 13, width = 40, pady = 10, yscrollcommand = scroll_text.set)
	text_box.grid(row = 1, column = 0, padx = 10, pady = 10)
	scroll_text.config(command = text_box.yview)
	scroll_text.grid(row = 1, column = 1, sticky = 'NS')

	key_label = Label(main, text = "Enter key: ", font = ('fixedsys', 12, 'bold'))
	key_label.grid(row = 2, column = 0)

	key_text = Entry(main, width = 40)
	key_text.grid(row = 3, column = 0, padx = 10, pady = 10)	

	scroll_text2 = ttk.Scrollbar(main, orient = VERTICAL)
	new_text = Text(main, height = 13, width = 40, pady = 10, yscrollcommand = scroll_text2.set)
	new_text.grid(row = 1, column = 2, columnspan = 2)
	scroll_text2.config(command = new_text.yview)
	scroll_text2.grid(row = 1, column = 4, sticky = 'NS')

	def encrypt():

		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = key_text.get()
		enc_text = ""	

		if len(key) > len(txt):
			key = key[: len(key) - len(txt) - 1]
		elif len(key) < len(txt):
			key = (key * ((len(txt) // len(key)) + 1))[:len(txt)]

		for i in range(len(txt)):
			if txt[i].isupper(): 
				v = 'A'
			elif txt[i].islower(): 
				v = 'a'
			else:
				enc_text += txt[i]
				continue

			enc_text += (chr(((ord(txt[i]) - 2 * ord(v) + ord(key[i])) % 26) + ord(v)))

		new_text.insert(1.0, enc_text)

	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = encrypt)
	enc.grid(row = 0, column = 2, padx = 20, pady = 10)

	def decrypt():
	
		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = key_text.get()
		dec_text = ""

		if len(key) > len(txt):
			key = key[: len(key) - len(txt) - 1]
		elif len(key) < len(txt):
			key = (key * ((len(txt) // len(key)) + 1))[:len(txt)]

		for i in range(len(txt)):
			if txt[i].isupper(): 
				v = 'A'
			elif txt[i].islower(): 
				v = 'a'
			else:
				dec_text += txt[i]
				continue

			s = ord(txt[i]) - ord(key[i])
			if s < 0: 
				s += 26

			dec_text += chr(s + ord(v))
		
		new_text.insert(1.0, dec_text)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = decrypt)
	dec.grid(row = 0, column = 3, padx = 10, pady = 10)	

	localtime()

def autokey_cipher():

	remove()
	label.config(text = "Autokey Cipher")
	label.grid(row = 0, column = 0)

	text_label = Label(main, text = "Enter text: ", font = ('fixedsys', 12, 'bold'))
	text_label.grid(row = 0, column = 0, padx = 20, pady = 20)

	scroll_text = ttk.Scrollbar(main, orient = VERTICAL)
	text_box = Text(main, height = 13, width = 40, pady = 10, yscrollcommand = scroll_text.set)
	text_box.grid(row = 1, column = 0, padx = 10, pady = 10)
	scroll_text.config(command = text_box.yview)
	scroll_text.grid(row = 1, column = 1, sticky = 'NS')

	key_label = Label(main, text = "Enter key/primer: ", font = ('fixedsys', 12, 'bold'))
	key_label.grid(row = 2, column = 0)

	key_text = Entry(main, width = 40)
	key_text.grid(row = 3, column = 0, padx = 10, pady = 10)	

	scroll_text2 = ttk.Scrollbar(main, orient = VERTICAL)
	new_text = Text(main, height = 13, width = 40, pady = 10, yscrollcommand = scroll_text2.set)
	new_text.grid(row = 1, column = 2, columnspan = 2)
	scroll_text2.config(command = new_text.yview)
	scroll_text2.grid(row = 1, column = 4, sticky = 'NS')

	def encrypt():

		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = key_text.get()
		enc_text = ""

		if len(key) < len(txt):
			key = (key + txt)[: len(txt)]
		elif len(key) > len(txt):
			key = key[: len(txt)]
		
		for i in range(len(txt)):
			if txt[i].isalpha():
				if txt[i].isupper():
					v = 'A'
				else:
					v = 'a'
				s = (ord(txt[i]) - ord(v) + ord(key[i]) - ord(v)) % 26
				enc_text += chr(s + ord(v))
			else:
				enc_text += txt[i]
		new_text.insert(1.0, enc_text)

	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = encrypt)
	enc.grid(row = 0, column = 2, padx = 20, pady = 10)

	def decrypt():

		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = key_text.get()
		dec_text = ""

		if len(key) < len(txt):
			key = (key + txt)[: len(txt)]
		elif len(key) > len(txt):
			key = key[: len(txt)]	

		for i in range(len(txt)):
			if txt[i].isalpha():
				if txt[i].isupper():
					v = 'A'
				else:
					v = 'a'
				s = ord(txt[i]) - ord(key[i])
				if s < 0:
					s += 26
				dec_text += chr(s + ord(v))
			else:
				dec_text += txt[i]
		new_text.insert(1.0, dec_text)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = decrypt)
	dec.grid(row = 0, column = 3, padx = 10, pady = 10)	

	localtime()

def railfence_cipher():

	remove()
	label.config(text = "Railfence Cipher")
	label.grid(row = 0, column = 0)

	text_label = Label(main, text = "Enter text: ", font = ('fixedsys', 12, 'bold'))
	text_label.grid(row = 0, column = 0, padx = 20, pady = 20)

	scroll_text = ttk.Scrollbar(main, orient = VERTICAL)
	text_box = Text(main, height = 13, width = 40, pady = 10, yscrollcommand = scroll_text.set)
	text_box.grid(row = 1, column = 0, padx = 10, pady = 10)
	scroll_text.config(command = text_box.yview)
	scroll_text.grid(row = 1, column = 1, sticky = 'NS')

	key_label = Label(main, text = "Enter key: ", font = ('fixedsys', 12, 'bold'))
	key_label.grid(row = 4, column = 0, padx = 20, pady = 30)

	list_key = ttk.Combobox(main)
	list_key['values'] = (2, 3, 4, 5, 6, 7, 8)
	list_key.current(0)
	list_key.grid(row = 5, column = 0)

	scroll_text2 = ttk.Scrollbar(main, orient = VERTICAL)
	new_text = Text(main, height = 13, width = 40, pady = 10, yscrollcommand = scroll_text2.set)
	new_text.grid(row = 1, column = 2, columnspan = 2)
	scroll_text2.config(command = new_text.yview)
	scroll_text2.grid(row = 1, column = 4, sticky = 'NS')

	def encrypt():

		new_text.delete('1.0', END)
		string = (text_box.get("1.0", END)).strip()
		key = int(list_key.get())

		a = [[None for i in range(len(string))] for j in range(key)]

		curr = 0
		findex = 0
		sindex = 0
		enc_text = ""

		while curr < len(string):
			if findex < key:
				while findex < key and curr < len(string):
					a[findex][sindex] = string[curr]
					curr += 1
					findex += 1
					sindex += 1
			if findex == key:
				findex -= 1
				while findex > 0 and curr < len(string):
					findex -= 1
					a[findex][sindex] = string[curr]
					curr += 1
					sindex += 1
				findex += 1

		for i in a:
			l = [x for x in i if x is not None]
			enc_text += "".join(l)
		new_text.insert(1.0, enc_text)

	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = encrypt)
	enc.grid(row = 0, column = 2, padx = 20, pady = 10)

	def decrypt():

		new_text.delete('1.0', END)
		string = (text_box.get("1.0", END)).strip()
		key = int(list_key.get())

		a = [[None for i in range(len(string))] for j in range(key)]

		curr = 0
		findex = 0
		sindex = 0
		dec_text = ""

		while curr < len(string):
			if findex < key:
				while findex < key and curr < len(string):
					a[findex][sindex] = "0"
					curr += 1
					findex += 1
					sindex += 1

			if findex == key:
				findex -= 1
				while findex > 0 and curr < len(string):
					findex -= 1
					a[findex][sindex] = "0"
					curr += 1
					sindex += 1
				findex += 1

		curr = 0

		for i in a:
			for j in range(len(i)):
				if i[j] == "0":
					i[j] = string[curr]
					curr += 1

		curr = 0
		findex = 0
		sindex = 0

		while curr < len(string):
			if findex < key:
				while findex < key and curr < len(string):
					dec_text += a[findex][sindex]
					curr += 1
					findex += 1
					sindex += 1

			if findex == key:
				findex -= 1
				while findex > 0 and curr < len(string):
					findex -= 1
					dec_text += a[findex][sindex]
					curr += 1
					sindex += 1
				findex += 1
		new_text.insert(1.0, dec_text)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = decrypt)
	dec.grid(row = 0, column = 3, padx = 10, pady = 10)	

	localtime()

def playfair_cipher():
	
	remove()
	label.config(text = "Playfair Cipher")
	label.grid(row = 0, column = 0)

	text_label = Label(main, text = "Enter text: ", font = ('fixedsys', 12, 'bold'))
	text_label.grid(row = 0, column = 0, padx = 20, pady = 20)

	scroll_text = ttk.Scrollbar(main, orient = VERTICAL)
	text_box = Text(main, height = 13, width = 40, pady = 10, yscrollcommand = scroll_text.set)
	text_box.grid(row = 1, column = 0, padx = 10, pady = 10)
	scroll_text.config(command = text_box.yview)
	scroll_text.grid(row = 1, column = 1, sticky = 'NS')

	key_label = Label(main, text = "Enter key: ", font = ('fixedsys', 12, 'bold'))
	key_label.grid(row = 2, column = 0)

	key_text = Entry(main, width = 40)
	key_text.grid(row = 3, column = 0, padx = 10, pady = 10)	

	scroll_text2 = ttk.Scrollbar(main, orient = VERTICAL)
	new_text = Text(main, height = 13, width = 40, pady = 10, yscrollcommand = scroll_text2.set)
	new_text.grid(row = 1, column = 2, columnspan = 2)
	scroll_text2.config(command = new_text.yview)
	scroll_text2.grid(row = 1, column = 4, sticky = 'NS')

	msg, new_msg = "", ""
	a = [[0 for i in range(5)]for i in range(5)]
	def input_f(text, key):
		inp = []
		lst_inp = key.split()
		for item in lst_inp:
			inp += item

		a = key_table(inp)

		c_msg = text
		msg = ""
		for i in c_msg:
			msg += i

		new_msg = "".join([i for i in c_msg])

		if 'j' in msg:
			msg = msg.replace('j', 'i')
		if 'J' in msg:
			msg = msg.replace('J', 'I')

		chunks = converted_chunks(msg)

		return chunks, a

	def key_table(inp):
		key = list(dict.fromkeys(inp))
		k = 0
		x = 65
		a = [[0 for i in range(5)]for i in range(5)]
		for i in range(5):
			for j in range(5):
				if k < len(key):
					a[i][j] = key[k].upper()
					k += 1
				elif not any(chr(x) in y for y in a) and chr(x) != 'J':
					a[i][j] = chr(x)
					x += 1
				else:
					while any(chr(x) in y for y in a) or chr(x) == 'J':
						x += 1
					a[i][j] = chr(x)
		return a

	def converted_chunks(msg):
		msg_list =  []
		for item in msg:
			msg_list += item
	
		chunks = []
		i = 0
		while i < len(msg_list):
			if i == len(msg_list)-1:
				chunks.append([msg_list[i].upper(), 'X'])
			elif msg_list[i] != msg_list[i + 1]:
				chunks.append([msg_list[i].upper(), msg_list[i+1].upper()])
				i += 1
			else:
				chunks.append([msg_list[i].upper(), 'X'])
			i += 1
		return chunks

	def find_coord(c, a):
		for i in range(5):
			for j in range(5):
				if a[i][j] == c:
					return i, j

	def check_num_spl(item):
		return item[0].isalpha() and item[1].isalpha()

	def encrypt():

		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = key_text.get()
		chunks, a = input_f(txt, key)
		enc_text = ""
		for item in chunks:
			if not check_num_spl(item):
				enc_text += item[0] + item[1]
			else:
				st = ""
				x1, y1 = find_coord(item[0], a)
				x2, y2 = find_coord(item[1], a)
				if y1 == y2:
					enc_text += a[(x1+1)%5][y1] + a[(x2+1)%5][y1]
				elif x1 == x2:
					enc_text += a[x1][(y1+1)%5] + a[x2][(y2+1)%5]
				else:
					st += a[x2][y1] + a[x1][y2]
					enc_text += st[::-1]
		new_text.insert(1.0, enc_text)

	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = encrypt)
	enc.grid(row = 0, column = 2, padx = 20, pady = 10)

	def decrypt():
		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = key_text.get()

		chunks, a = input_f(txt, key)

		dec_text = ""

		for item in chunks:
			if not check_num_spl(item):
				dec_text += item[0] + item[1]
			else:
				st = ""
				x1, y1 = find_coord(item[0], a)
				x2, y2 = find_coord(item[1], a)
				if y1 == y2:
					dec_text += a[x1-1][y1] + a[x2-1][y1]
				elif x1 == x2:
					dec_text += a[x1][y1-1] + a[x2][y2-1]
				else:
					dec_text += a[x1][y2] + a[x2][y1]
		if 'X' in dec_text:
			dec_text = dec_text.replace('X', '')
		
		new_text.insert(1.0, dec_text)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = decrypt)
	dec.grid(row = 0, column = 3, padx = 10, pady = 10)	

	localtime()

# ----------------- Home Screen -------------------#

show()

# ----------------- Pane buttons -------------------#

home_button = Button(frame, padx = 20, bd = 10, text = 'Home', width = 20, height = 3, command = show)
home_button.grid(row = 0, column = 0)

caesar = Button(frame, padx = 20, bd = 10, text = 'Caesar Cipher', width = 20, height = 3, command = caesar_cipher)
caesar.grid(row = 1, column = 0)

homophonic = Button(frame, padx = 20, bd = 10, text = 'Homophonic Cipher', width = 20, height = 3, command = homophonic_cipher)
homophonic.grid(row = 2, column = 0)

vignere = Button(frame, padx = 20, bd = 10, text = 'Vignere Cipher', width = 20, height = 3, command = vignere_cipher)
vignere.grid(row = 3, column = 0)

autokey = Button(frame, padx = 20, bd = 10, text = 'Autokey Cipher', width = 20, height = 3, command = autokey_cipher)
autokey.grid(row = 4, column = 0)

railfence = Button(frame, padx = 20, bd = 10, text = 'Railfence Cipher', width = 20, height = 3, command = railfence_cipher)
railfence.grid(row = 5, column = 0)

playfair = Button(frame, padx = 20, bd = 10, text = 'Playfair Cipher', width = 20, height = 3, command = playfair_cipher)
playfair.grid(row = 6, column = 0)

C4 = Button(frame, padx = 20, bd = 10, text = 'Cipher', width = 20, height = 3)
C4.grid(row = 7, column = 0)

C5 = Button(frame, padx = 20, bd = 10, text = 'Cipher', width = 20, height = 3)
C5.grid(row = 8, column = 0)

C6 = Button(frame, padx = 20, bd = 10, text = 'Cipher', width = 20, height = 3)
C6.grid(row = 9, column = 0)


root.mainloop()
