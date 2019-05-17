import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

def linegraph(list):
    plt.plot(list)
    plt.ylabel('Waarde')
    plt.xlabel('Iteraties')
    plt.show()

def grid(houses_list, worth):

    plt.figure()
    plt.title(worth)
    plt.axis([0, 320, 0, 360])

    # i = 0
    for house in houses_list:
        currentAxis = plt.gca()
        if house.type == 'eensgezinswoning':
            color = 'blue'
        elif house.type == 'bungalow':
            color = 'red'
        elif house.type == 'maison':
            color = 'yellow'
        outer_x = house.x - house.minvr
        print(house.x)
        print(outer_x)
        currentAxis.add_patch(Rectangle((house.x, house.y), house.width, house.depth, color=color))
        currentAxis.add_patch(Rectangle((house.x, house.y), house.width, house.depth, color=color))
        currentAxis.annotate(house.id, (house.x, house.y))
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
