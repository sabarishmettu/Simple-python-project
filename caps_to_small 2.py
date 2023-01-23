import tkinter as tk

def convert_to_lowercase(string):
    return string.lower()

def on_submit():
    original_string = input_box.get()
    lowercase_string = convert_to_lowercase(original_string)
    output_box.config(state='normal')
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "The lowercase version of the string is: " + lowercase_string)
    output_box.config(state='disabled')
    
root = tk.Tk()
root.title("Caps to Small Letters Converter")

input_label = tk.Label(root, text="Enter a string in uppercase:")
input_label.grid(row=0, column=0)

input_box = tk.Entry(root)
input_box.grid(row=0, column=1)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=1, column=1)

output_label = tk.Label(root, text="Output:")
output_label.grid(row=2, column=0)

output_box = tk.Text(root, height=3, width=30)
output_box.grid(row=2, column=1)
output_box.config(state='disabled')

root.mainloop()
