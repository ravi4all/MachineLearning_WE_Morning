import numpy as np

arr = np.array([x for x in range(1,15)])
print(arr)
# np.array - Will create an array within range of 1,15

arr = np.arange(15)
print(arr)
# np.arange(15) - Will create an array equivalent to above

arr = np.arange(5,15)
print(arr)
# np.arange(5,15) - Will create an array from 5 to 14

arr = np.arange(5,15,2)
print(arr)
# np.arange(5,15,2) - Will create an array from 5 to 14 with step of 2

arr = np.arange(5,15,2,dtype=float)
print(arr)
# np.arange(5,15,2,dtype=float) - Will create float type of elements

arr = np.linspace(1,5)
print(arr)
# np.linspace(1,5) - Will give 50 values between 1 to 5

arr = np.linspace(1,5,5)
print(arr)
# np.linspace(1,5,5) - Will give only 5 values between 1 to 5

arr,spacing = np.linspace(1,5,retstep=True)
print(spacing)
# np.linspace(1,5,retstep=True) - Will return the spacing between array elements

arr = np.linspace(1,5, endpoint=False,retstep=True)
print(arr)
# np.linspace(1,5, endpoint=False,retstep=True) - Will not return array last index

arr = np.ndarray(10)
print(arr)
# np.ndarray(10) -  Will create 1D array of 10 random elements

arr = np.ndarray([10,2])
print(arr)
# np.ndarray([10,2]) - Will create 2D Array

arr = np.ndarray([10,1,1])
print(arr)
# np.ndarray([10,1]) - Will create 3D Array

# np.ndim(arr) - Dimensions(rank) of an array
# np.nshape(arr) - Shape of an array
# np.dtype(arr) - Datatype of the array