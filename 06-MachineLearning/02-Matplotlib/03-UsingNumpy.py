import numpy as np
import matplotlib.pyplot as plt

x = np.arange(5,20,2)
y = np.arange(20,35,2)

print(x)
print(y)

plt.bar(x,y)
plt.show()