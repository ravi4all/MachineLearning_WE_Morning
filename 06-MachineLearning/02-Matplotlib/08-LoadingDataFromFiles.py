import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib import style

style.use('ggplot')

# x = []
# y = []
#
# with open("coords.csv",'r') as csv_file:
#     reader = csv.reader(csv_file, delimiter=',')
#
#     for row in reader:
#         x.append(row[0])
#         y.append(row[1])
#
# plt.plot(x,y)
# plt.show()

x,y = np.loadtxt('coords.csv',delimiter=',',unpack=True)
plt.plot(x,y)
plt.show()