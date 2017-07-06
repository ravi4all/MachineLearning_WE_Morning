import numpy as np

a = np.floor(10*np.random.random((3,4)))
print(a)

print(a.shape)

print("Flattened Array")
print(a.ravel())    # returns the array, flattened


print("Reshaped Array")
print(a.reshape(6,2))   # returns the array with a modified shape

print("Transpose")
print(a.T)      # returns the array, transposed

print("Transposed shape")
print(a.T.shape)

print("Original Shape")
print(a.shape)  #following three commands all return a modified array, but do not change the original array
