
#importing the tkinter module 
from tkinter import *
  
# creating tkinter window 
root = Tk() 
  
# counter variable 
counter = 0
  
# function for increasing counter value 
def increase(): 
    global counter 
    counter += 1
    label.config(text = str(counter)) 
  
# function for decreasing counter value 
def decrease(): 
    global counter 
    counter -= 1
    label.config(text = str(counter)) 
  
# creating two buttons for increasing and decreasing counter value 
button1 = Button(root, text = 'Increase', command = increase) 
button2 = Button(root, text = 'Decrease', command = decrease) 
  
# creating a label for showing the counter value 
label = Label(root, width = 10, height = 2, font = ('Helvetica', 30)) 
  
# arranging buttons and label 
button1.pack() 
button2.pack() 
label.pack() 
  
# infinite loop which is required to 
# run tkinter program