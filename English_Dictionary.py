

import tkinter
from tkinter import *

# creating main window
window = tkinter.Tk()
window.title("English Dictionary")
window.geometry("400x400")

# creating a label

lb1 = Label(window, text="Welcome to English Dictionary", font=("Ariel", 15))
lb1.pack()

# creating a entry

entry = Entry(window, width=20, bg="light green")
entry.pack()

# defining a function

def search():
    search_term = entry.get()
    # creating a dictionary
    dict = {
        "apple": "A fruit that grows on trees",
        "cat": "A small animal often kept as pet"
    }
    output = dict[search_term]
    lb2 = Label(window, text=output)
    lb2.pack()

# creating a button

btn = Button(window, text="Search", command=search)
btn.pack()

# running the main window
window.mainloop()