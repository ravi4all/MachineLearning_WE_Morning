import matplotlib.pyplot as plt

days = [1,2,3,4]
activities = ['sleeping','eating','working','playing']
cols = ['r','g','b','c']

plt.pie(days,
        labels=activities,
        colors=cols,
        shadow=True,
        explode=(0,0.2,0,0),
        startangle=90,
        autopct='%1.1f%%')

plt.show()