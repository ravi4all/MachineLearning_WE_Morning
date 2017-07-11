import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [3,5,9,2,4]

x2 = [3,5,7,9,11]
y2 = [5,8,6,1,2]

plt.bar(x,y, color='r')
plt.bar(x2,y2, color='b')

plt.show()