import numpy as np

def f(x,y):
    return 10*x+y


b = np.fromfunction(f,(5,4),dtype=int)
print(b)

print(b[2,3])

print(b[0:5, 1])    # each row in the second column of b
print(b[ : , 1])    # Same to the previous one

print(b[1:3, : ])    # each column in the second and third row of b

print(b[-1])    # The last row

