from tkinter import *
import time

master = Tk()

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200, tick)

clock = Label(master, font=('times', 20, 'bold'), bg='orange')
clock.grid(row=0, column=1)
tick()
