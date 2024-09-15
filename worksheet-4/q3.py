import numpy as np

# 3.1 Create two 1D arrays
array1 = np.array([2, 4, 6, 8, 10])
array2 = np.array([1, 3, 5, 7, 9])

# 3.2 Perform the specified operations

# Addition
addition = array1 + array2
print("Addition:")
print(addition)

# Subtraction
subtraction = array1 - array2
print("\nSubtraction:")
print(subtraction)

# Element-wise multiplication
multiplication = array1 * array2
print("\nElement-wise Multiplication:")
print(multiplication)

# Element-wise division
division = array1 / array2
print("\nElement-wise Division:")
print(np.round(division, 2))