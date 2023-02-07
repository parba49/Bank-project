from tkinter import *
from tkinter.ttk import *
from time import strftime


root=Tk()
root.title("my clock")

label=Label(root,font=("ds-digital",80),background='black',foreground='cyan')
label.pack(anchor='center')

def mytime():
    string = strftime('%I:%M:%S %p, %A')
    label.config(text=string)
    label.after(1000,mytime)

mytime()
mainloop()