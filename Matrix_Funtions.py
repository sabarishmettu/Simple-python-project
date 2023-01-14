import numpy as np

def add_matrices(mat1, mat2):
    return np.add(mat1, mat2)

def sub_matrices(mat1, mat2):
    return np.subtract(mat1, mat2)

def mul_matrices(mat1, mat2):
    return np.dot(mat1, mat2)

def div_matrices(mat1, mat2):
    return np.divide(mat1, mat2)

# Get user input for the dimensions of the matrices
rows1 = int(input("Enter the number of rows for matrix 1: "))
cols1 = int(input("Enter the number of columns for matrix 1: "))
rows2 = int(input("Enter the number of rows for matrix 2: "))
cols2 = int(input("Enter the number of columns for matrix 2: "))

# Initialize the matrices with user input
mat1 = np.zeros((rows1, cols1))
mat2 = np.zeros((rows2, cols2))

print("Enter the elements of matrix 1:")
for i in range(rows1):
    for j in range(cols1):
        mat1[i][j] = float(input())

print("Enter the elements of matrix 2:")
for i in range(rows2):
    for j in range(cols2):
        mat2[i][j] = float(input())

# Perform matrix operations
print("Matrix 1 + Matrix 2 = \n", add_matrices(mat1, mat2))
print("Matrix 1 - Matrix 2 = \n", sub_matrices(mat1, mat2))
print("Matrix 1 * Matrix 2 = \n", mul_matrices(mat1, mat2))
print("Matrix 1 / Matrix 2 = \n", div_matrices(mat1, mat2))
