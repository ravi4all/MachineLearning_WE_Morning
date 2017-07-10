import matplotlib.pyplot as plt

x_1 = [12,23,83]
y_1 = [33,34,45]

x_2 = [32,56,88]
y_2 = [99,67,23]

plt.plot(x_1, y_1, label='First Line')
plt.scatter(x_2, y_2, label = 'Second Line')

plt.legend()

plt.show()