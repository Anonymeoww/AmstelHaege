import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

def linegraph(list):
    plt.plot(list)
    plt.ylabel('Waarde')
    plt.xlabel('Iteraties')
    plt.show()

def grid(houses_list, worth):

    x = []
    y = []
    id = []
    type = []
    width = []
    depth = []

    for house in houses_list:
        x.append(house.x)
        y.append(house.y)
        id.append(house.id)
        type.append(house.type)
        width.append(house.width)
        depth.append(house.depth)
        print(house.width)
    plt.figure()
    plt.title(worth)
    plt.axis([0, 16, 0, 18])

    i = 0
    for point in x:
        currentAxis = plt.gca()
        if type[i] == 'eensgezinswoning':
            color = 'blue'
        elif type[i] == 'bungalow':
            color = 'red'
        elif type[i] == 'maison':
            color = 'yellow'
        currentAxis.add_patch(Rectangle((x[i], y[i]), width[i], depth[i], color=color))
        currentAxis.annotate(id[i], (x[i], y[i]))
        i=i+1
    plt.show()

def SA(temp, chance, xen, nenc):
    # np.random.seed(19680801)
    # data = np.random.randn(2, 100)

    fig, axs = plt.subplots(2, 2, figsize=(5, 5))
    axs[0, 0].plot(temp)
    axs[0, 0].set_title('temperature')
    axs[1, 0].plot(chance)
    axs[1, 0].set_title("chance")
    axs[0, 1].plot(xen)
    axs[0, 1].set_title("X")
    axs[1, 1].plot(nenc)
    axs[1, 1].set_title("N-C")

    plt.show()
