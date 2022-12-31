import tkinter 

from tkinter import *

#Creating the window
window = Tk()
window.title("Gaussian Elimination Calculator")
window.geometry("500x500")

#Creating the labels
Label(window, text="Gaussian Elimination Calculator", font =("helvetica", 20)).grid(row=0, column=0, columnspan=3)
Label(window, text="Matrix Size:").grid(row=1, column=0)
Label(window, text="Number of Variables:").grid(row=2, column=0)

#Creating entry boxes
e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

#Creating the function to do the calculation
def calculate():
	row = int(e1.get())
	column = row + 1
	num_vars = int(e2.get())

	#Creating the labels for the matrix
	for i in range(row):
		Label(window, text="Row" + str(i+1)).grid(row=3+i, column=0)

	#Creating the entry boxes for the matrix
	entry_boxes = []
	for i in range(row):
		for j in range(column):
			entry_boxes.append(Entry(window, width=5))
			entry_boxes[-1].grid(row=3+i, column=1+j)

	#Creating the button to perform the calculation
	Button(window, text="Calculate", command=calculate_gaussian).grid(row=3+row, column=0, columnspan=column)

#Function to perform the Gaussian elimination
def calculate_gaussian():
	row = int(e1.get())
	column = row + 1
	num_vars = int(e2.get())

	#Retrieving the matrix
	matrix = []
	for i in range(row):
		matrix.append([])
		for j in range(column):
			matrix[-1].append(float(entry_boxes[i*column + j].get()))

	#Performing the elimination
	for i in range(num_vars-1):
		for j in range(row-i-1):
			if matrix[i+j+1][i] != 0:
				ratio = matrix[i+j][i]/matrix[i+j+1][i]
				for k in range(column):
					matrix[i+j+1][k] *= ratio
					matrix[i+j+1][k] -= matrix[i+j][k]

	#Creating the labels for the solution
	for i in range(num_vars):
		Label(window, text="x" + str(i+1)).grid(row=3+row+1+i, column=0)

	#Creating the entry boxes for the solution
	solution = []
	for i in range(num_vars):
		solution.append(Entry(window, width=5))
		solution[-1].grid(row=3+row+1+i, column=1)

	#Calculating the solution
	for i in range(num_vars-1,-1,-1):
		sum = 0
		for j in range(num_vars-i,num_vars):
			sum += matrix[i][j] * float(solution[j].get())
		solution[i].delete(0, END)
		solution[i].insert(0, round((matrix[i][column-1] - sum) / matrix[i][i],3))

#Creating the button to proceed
Button(window, text="Proceed", command=calculate).grid(row=3, column=0, columnspan=2)

#Running the window
window.mainloop()
