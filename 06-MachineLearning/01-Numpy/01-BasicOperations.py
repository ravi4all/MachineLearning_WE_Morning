import numpy as np

a = np.array([[1,1],
             [0,1]])

b = np.array([[2,0],
             [3,4]])

# Elementwise product
print(a*b)

# Matrix Product
print(a.dot(b))

# Another matrix product
print(np.dot(a,b))

"""
Some operations, such as += and *=, act in place to modify
an existing array rather than create a new one.
"""
print("------------------------------------------")
a1 = np.ones((2,3), dtype=int)
b1 = np.random.random((2,3))
a1 *= 3
print(a1)

b1 += a1
print(b1)
