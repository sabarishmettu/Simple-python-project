from tkinter import *

def change_color():
    text = entry.get()
    txt.configure(fg=text)

window = Tk()
window.title("Colored Text")

frame = Frame(window)

label = Label(frame, text="Enter a color:")
label.pack()

entry = Entry(frame)
entry.pack()

button = Button(frame, text="Change Color", command=change_color)
button.pack()

frame.pack()

txt = Label(window, text="This text will change color")
txt.pack()

window.mainloop()
