import numpy as np

# Define a matrix
matrix = np.array([[2, 1, 3],
                   [0, 5, 6],
                   [7, 8, 9]])

# Calculate the determinant of the matrix
determinant = np.linalg.det(matrix)

# P1.1
print("Matrix:")
print(matrix)
print("\nDeterminant of the matrix:")
print(determinant)

# 1.2
if determinant != 0:
    inverse_A = np.linalg.inv(matrix)
    print("\nInverse of Matrix:")
    print(inverse_A)
else:
    print("\nMatrix A is not invertible (determinant is zero).")

eigenvalues, eigenvectors = np.linalg.eig(matrix)

print("\nEigenvalues of Matrix:")
print(eigenvalues)

print("\nEigenvectors of Matrix:")
print(eigenvectors)