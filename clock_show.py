from tkinter import *
from tkinter.ttk import *

from time import strftime

R1=Tk()
R1.title("CLOCK")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
    
    
label=Label(R1 , font =("ds-digital",80), background="black" ,foreground="green")
label.pack(anchor='center')
time()

mainloop()   