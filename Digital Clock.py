from tkinter import *
import time


# This function shows and changes the time
def t():
    c_t = time.strftime("%I : %M : %S")
    l_2.config(text=c_t)
    l_2.after(100, t)


root = Tk()

l_1 = Label(root, text="Digital Clock", font="times 20 ", fg="purple" , bg="pink")
l_1.grid(row=15, column=15)  # l_1 will be displayed in first column of first row

l_2 = Label(root, font="times 60" ,fg="black" )
l_2.grid(row=30, column=15)  # l_2 will be displayed in first column of second row
t()

l_3 = Label(root, text="Hour   Minute   Second", font="times 25 bold" , fg="gray")
l_3.grid(row=60, column=15)  # l_3 will be displayed in first column of third row

root.mainloop()
