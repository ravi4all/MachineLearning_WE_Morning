import numpy as np

b = np.arange(12).reshape(3,4)
print(b)

print("----------")
print(b.sum(axis = 0))  #sum of each column

print("----------")
print(b.min(axis = 1))  # Min of each row

print("----------")
print(b.cumsum(axis = 0))   # cumulative sum along each row
