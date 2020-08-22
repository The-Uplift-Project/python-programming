import tkinter as tk
def click():
  pass
  #write your code here
  # text = text_box.get(1.0,2.1)#index: <line no.>.<char.index>
  # tk.Label(text = text).pack()
  #sortText = sorted(text)
  #text_box.insert(1.0,'Sorted:'+''.join(sortText))

window = tk.Tk()
frame = tk.Frame(window)
frame2 = tk.Frame(window)
button = tk.Button(window,text='Click this!',command = click)

label1 = tk.Label(frame,text='I am in Frame 1',fg='red',bg='black')
button1 = tk.Button(frame,text='Frame 1 Click this!',bg='DEEPPINK',command = click)

label2 = tk.Label(frame2,text='I am in Frame2',fg='red',bg='black')
button2 = tk.Button(frame2,text='Frame 2 Click this!',bg='DEEPPINK',command = click)

button.pack(fill=tk.BOTH,side=tk.LEFT)
# frame.pack(fill=tk.BOTH,side='left')
# label1.pack(fill=tk.X,side=tk.LEFT)
# button1.pack(fill=tk.BOTH,side='left')
# label12 = tk.Label(frame,text='I am in Frame 1.2',fg='red',bg='black',width=30)
# label13 = tk.Label(frame,text='I am in Frame 1.3',fg='red',bg='black',width=30)
# label14 = tk.Label(frame,text='I am in Frame 1.4',fg='red',bg='black',width=30)
# label12.pack()
# label13.pack()
# label14.pack()
# frame2.pack(fill=tk.BOTH,side='left')
# label2.pack(fill=tk.X,side=tk.LEFT)
# button2.pack(fill=tk.BOTH,side='left')
window.mainloop()

#text->sort, Sorted:text
#python->Sorted:hnopty

"""
1.2
python
2.1
is
amazing
"""