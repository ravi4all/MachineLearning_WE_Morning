import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [12,16,8,7,10]
working = [6,5,9,8,10]
eating = [8,7,9,12,6]
playing = [18,12,15,10,11]

plt.plot([],[],color='r',label='Sleeping')
plt.plot([],[],color='b',label='Working')
plt.plot([],[],color='g',label='Eating')
plt.plot([],[],color='c',label='Playing')

plt.stackplot(days,sleeping,working,eating,playing)

plt.legend()
plt.show()