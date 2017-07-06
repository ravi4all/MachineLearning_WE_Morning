import numpy as np

a = np.floor(10*np.random.random((2,12)))
print("Original Array")
print(a)

print("Array after split")
print(np.hsplit(a,3))       # Split a into 3

print("Spliting with condition")
print(np.hsplit(a,(3,4)))       # Split a after the third and the fourth column
