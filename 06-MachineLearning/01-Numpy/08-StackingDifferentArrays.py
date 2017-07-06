import numpy as np

print("Array 1")
a = np.floor(10*np.random.random((2,2)))
print(a)

print("Array 2")
b = np.floor(10*np.random.random((2,2)))
print(b)

print("After stacking both arrays vertically")
print(np.vstack((a,b)))     # Vertical stack


print("After stacking both arrays horizontally")
print(np.hstack((a,b)))     # Horizontal stack
