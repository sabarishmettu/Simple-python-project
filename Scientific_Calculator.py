import tkinter as tk
import math

def button_click(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, tk.END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_equal():
    second_number = e.get()
    e.delete(0, tk.END)

    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "division":
        e.insert(0, f_num / float(second_number))

def button_sin():
    first_number = e.get()
    e.delete(0, tk.END)
    e.insert(0, math.sin(float(first_number)))

def button_cos():
    first_number = e.get()
    e.delete(0, tk.END)
    e.insert(0, math.cos(float(first_number)))

def button_tan():
    first_number = e.get()
    e.delete(0, tk.END)
    e.insert(0, math.tan(float(first_number)))

def button_log():
    first_number = e.get()
    e.delete(0, tk.END)
    e.insert(0, math.log10(float(first_number)))

def button_power():
    first_number = e.get()
    global f_num
    global math
    math = "power"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_equal_power():
    global e
    second_number = e.get()
    e.delete(0, tk.END)
    e.insert(0, f_num ** float(second_number))

root = tk.Tk()
root.title("Scientific Calculator")

e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create a frame for the numbers
number_frame = tk.Frame(root)
number_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=4)

# Create a frame for the operations
operation_frame = tk.Frame(root)
operation_frame.grid(row=2, column=0, padx=10, pady=10, columnspan=4)

# Create a frame for the trigonometric functions
trigonometric_frame = tk.Frame(root)
trigonometric_frame.grid(row=3, column=0, padx=10, pady=10, columnspan=4)

# Create a frame for the logarithmic function and exponential function
other_frame = tk.Frame(root)
other_frame.grid(row=4, column=0, padx=10, pady=10, columnspan=4)

# Create buttons for the numbers and add them to the number frame
button_1 = tk.Button(number_frame, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(number_frame, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(number_frame, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(number_frame, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(number_frame, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(number_frame, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(number_frame, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(number_frame, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(number_frame, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(number_frame, text="0", padx=40, pady=20, command=lambda: button_click(0))

# Create buttons for the operations and add them to the operation frame
button_add = tk.Button(operation_frame, text="+", padx=39, pady=20, command=button_add)
button_subtract = tk.Button(operation_frame, text="-", padx=41, pady=20, command=button_subtract)
tract = tk.Button(operation_frame, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = tk.Button(operation_frame, text="*", padx=40, pady=20, command=button_multiply)
button_divide = tk.Button(operation_frame, text="/", padx=41, pady=20, command=button_divide)

# Create a button for clearing the screen and add it to the operation frame
button_clear = tk.Button(operation_frame, text="AC", padx=38, pady=20, command=button_clear)

# Create a button for equal and add it to the operation frame
button_equal = tk.Button(operation_frame, text="=", padx=91, pady=20, command=button_equal)

# Add the number buttons to the number frame
button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)

button_4.grid(row=1, column=0)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=3, column=0)
button_clear.grid(row=3, column=1, columnspan=2)

# Add the operation buttons to the operation frame
button_add.grid(row=0, column=0)
button_subtract.grid(row=0, column=1)
button_multiply.grid(row=0, column=2)
button_divide.grid(row=1, column=0)
button_equal.grid(row=1, column=1, columnspan=2)

# Create buttons for trigonometric functions and add them to the trigonometric frame
button_sin = tk.Button(trigonometric_frame, text="sin", padx=35, pady=20, command=button_sin)
button_cos = tk.Button(trigonometric_frame, text="cos", padx=35, pady=20, command=button_cos)
button_tan = tk.Button(trigonometric_frame, text="tan", padx=35, pady=20, command=button_tan)

# Add the trigonometric buttons to the trigonometric frame
button_sin.grid(row=0, column=0)
button_cos.grid(row=0, column=1)
button_tan.grid(row=0, column=2)

# Create a button for the logarithmic function and add it to the other frame
button_log = tk.Button(other_frame, text="log", padx=35, pady=20, command=button_log)

# Create buttons for the exponential function and add them to the other frame
button_power = tk.Button(other_frame, text="^", padx=35, pady=20, command=button_power)
button_equal_power = tk.Button(other_frame, text="=", padx=35, pady=20, command=button_equal_power)

# Add the logarithmic and exponential buttons to the other frame
button_log.grid(row=0, column=0)
button_power.grid(row=0, column=1)
button_equal_power.grid(row=0, column=2)

root.mainloop()

