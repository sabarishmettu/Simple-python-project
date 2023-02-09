import tkinter as tk
from tkinter import *
import random
import string

root = tk.Tk()

# define the constants
MAX_LENGTH = 10
MAX_SYMBOLS = 10

# generate the random password
pass_length = random.randint(8, MAX_LENGTH)
pass_symbols = random.randint(1, MAX_SYMBOLS)

password_list = []

# add random symbols to the password list
for i in range(pass_symbols):
    password_list.append(chr(random.randint(33, 126)))

# add random numbers and letters to the password list
while len(password_list) < pass_length:
    password_list.append(random.choice(string.ascii_letters + string.digits))

# shuffle the list to randomize the password
random.shuffle(password_list)

# create the password string
password = ''.join(password_list)

# create the GUI
password_label = Label(root, text="Your randomly generated password is:")
password_label.pack()
password_text = Text(root, height=1, width=20)
password_text.pack()
password_text.insert(END, password)

# start the GUI
root.mainloop()
