import numpy as np

# 1.1 
array_1d = np.arange(5, 26)

# 2.1 
print(f"1D Array: {array_1d}")
print("Shape:", array_1d.shape)
print("Size:", array_1d.size)
print("Data type:", array_1d.dtype)

# 1.2 
array_2d = np.random.randint(10, 51, size=(3, 4))

print()

# 2.2 
print(f"2D Array: {array_2d}")
print("Shape:", array_2d.shape)
print("Size:", array_2d.size)
print("Data type:", array_2d.dtype)