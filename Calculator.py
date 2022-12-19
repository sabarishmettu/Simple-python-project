
import tkinter

def on_click(key):
    if key == "=":
        result = eval(display.get())
        s = str(result)
        display.insert(tkinter.END, "=" + s)
    elif key == "C":
        display.delete(0, tkinter.END)
        display.insert(tkinter.END, "")
    else:
        display.insert(tkinter.END, key)

root = tkinter.Tk()
root.title("Calculator")

display = tkinter.Entry(root, width = 40, borderwidth = 5)
display.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

# first row
btn1 = tkinter.Button(root, text = "1", padx = 40, pady = 20, command = lambda: on_click("1"))
btn2 = tkinter.Button(root, text = "2", padx = 40, pady = 20, command = lambda: on_click("2"))
btn3 = tkinter.Button(root, text = "3", padx = 40, pady = 20, command = lambda: on_click("3"))
btn4 = tkinter.Button(root, text = "+", padx = 39, pady = 20, command = lambda: on_click("+"))

# second row
btn5 = tkinter.Button(root, text = "4", padx = 40, pady = 20, command = lambda: on_click("4"))
btn6 = tkinter.Button(root, text = "5", padx = 40, pady = 20, command = lambda: on_click("5"))
btn7 = tkinter.Button(root, text = "6", padx = 40, pady = 20, command = lambda: on_click("6"))
btn8 = tkinter.Button(root, text = "-", padx = 40, pady = 20, command = lambda: on_click("-"))

# third row
btn9 = tkinter.Button(root, text = "7", padx = 40, pady = 20, command = lambda: on_click("7"))
btn10 = tkinter.Button(root, text = "8", padx = 40, pady = 20, command = lambda: on_click("8"))
btn11 = tkinter.Button(root, text = "9", padx = 40, pady = 20, command = lambda: on_click("9"))
btn12 = tkinter.Button(root, text = "*", padx = 40, pady = 20, command = lambda: on_click("*"))

# fourth row
btn13 = tkinter.Button(root, text = "C", padx = 40, pady = 20, command = lambda: on_click("C"))
btn14 = tkinter.Button(root, text = "0", padx = 40, pady = 20, command = lambda: on_click("0"))
btn15 = tkinter.Button(root, text = "=", padx = 40, pady = 20, command = lambda: on_click("="))
btn16 = tkinter.Button(root, text = "/", padx = 40, pady = 20, command = lambda: on_click("/"))

# put the buttons on the screen
btn1.grid(row = 1, column = 0)
btn2.grid(row = 1, column = 1)
btn3.grid(row = 1, column = 2)
btn4.grid(row = 1, column = 3)

btn5.grid(row = 2, column = 0)
btn6.grid(row = 2, column = 1)
btn7.grid(row = 2, column = 2)
btn8.grid(row = 2, column = 3)

btn9.grid(row = 3, column = 0)
btn10.grid(row = 3, column = 1)
btn11.grid(row = 3, column = 2)
btn12.grid(row = 3, column = 3)

btn13.grid(row = 4, column = 0)
btn14.grid(row = 4, column = 1)
btn15.grid(row = 4, column = 2)
btn16.grid(row = 4, column = 3)

root.mainloop()
