import numpy as np

# 8.1 
matrix_A = np.array([[1, 2], [3, 4]])
matrix_B = np.array([[5, 6], [7, 8]])

# 8.2

# Matrix Multiplication
matrix_multiplication = np.dot(matrix_A, matrix_B)
print("Matrix Multiplication (A * B):")
print(matrix_multiplication)

print()

# Transpose of Matrix A
transpose_A = np.transpose(matrix_A)
print("\nTranspose of Matrix A:")
print(transpose_A)