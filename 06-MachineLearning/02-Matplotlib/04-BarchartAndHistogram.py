import matplotlib.pyplot as plt
import numpy as np

population_ages = [22, 55, 30, 15, 35, 40, 90, 25, 38, 48,  50, 67, 88, 55, 30, 15, 35, 40, 90, 25, 38, 48,  50, 67, 88]

bins = [1,10,20,30,40,50,60,70,80,90,100]

plt.hist(population_ages, bins, histtype='bar', rwidth = 0.5)

plt.legend()
plt.show()
