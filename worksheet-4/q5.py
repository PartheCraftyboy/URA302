import numpy as np

# 5.1
array_2d = np.arange(10, 26).reshape(4, 4)
print("Original 2D Array (4x4):")
print(array_2d)

# 5.2 
second_row = array_2d[1, :]
last_column = array_2d[:, -1]
print("\nSecond Row:")
print(second_row)
print("\nLast Column:")
print(last_column)

# 5.3 
array_2d[0, :] = 0
print("\nArray after replacing the first row with zeros:")
print(array_2d)