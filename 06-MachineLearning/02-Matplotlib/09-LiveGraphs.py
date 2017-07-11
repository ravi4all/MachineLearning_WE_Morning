import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('ggplot')

fig = plt.figure()

ax1 = plt.subplot()

def animate(i):
    file = open('coords.txt','r').read()
    # print(file)
    lines = file.split('\n')

    xs = []
    ys = []

    for line in lines:
        x,y = line.split(',')
        xs.append(x)
        ys.append(y)

    ax1.clear()
    ax1.plot(xs,ys)

anim = animation.FuncAnimation(fig,animate)
plt.show()
