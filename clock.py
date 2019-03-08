from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

def quit(*args):
    root.destroy()

def clock_time():
    time=datetime.datetime.now()
    time1=datetime.datetime.now()
    time=(time.strftime("%I:%M:%S:%p"))
    time1=(time1.strftime("%d/%m/%y"))

    txt.set(time)
    txt1.set(time1)

    root.after(1000,clock_time)

root=Tk()
root.title("DigitalClock")
root.resizable(0,0)
root.attributes("-alpha",0.8)
root.attributes("-toolwindow",1)
root.configure(background='black')
root.bind("x",quit)
root.after(1000,clock_time)

fnt=font.Font(family='Helvetica', size=60, weight='bold')
fnt1=font.Font(family='', size=30, weight='bold')
txt=StringVar()
txt1=StringVar()
lbl=ttk.Label(root, textvariable=txt,font=fnt, foreground="red", background="white", underline=9)
lbl.pack(fill=X)
lbl1=ttk.Label(root, textvariable=txt1, font=fnt1 ,foreground="green", background="white", anchor=CENTER)
lbl1.pack(fill=X)

root.mainloop()

