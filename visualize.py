import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.ticker as ticker
#  yeet
import locale

def linegraph(iter, list):

    iterations = [item for item in range(0, iter)]
    maxval = max(list)
    plt.plot(iterations, list)
    plt.ylabel('Waarde x 1.000.000')
    plt.xlabel('Iteraties')
    plt.axis([0,iter,0,maxval+5])
    plt.show()

def grid(houses_list, worth):

    locale.setlocale(locale.LC_ALL, '')
    value = locale.currency(worth, grouping=True)

    fig, ax = plt.subplots()
    plt.title("Totale wijkwaarde: {}".format(value))
    plt.axis([0, 320, 0, 360])
    ax.set_facecolor('#DBFEB8')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(40))

    for house in houses_list:
        currentAxis = plt.gca()
        if house.type == 'eensgezinswoning':
            color = '#A1ADB4'
        elif house.type == 'bungalow':
            color = '#C0A0C1'
        elif house.type == 'maison':
            color = '#FCB0B3'
        outer_x = house.xmin - house.minvr
        outer_y = house.ymin - house.minvr
        currentAxis.add_patch(Rectangle((house.xmin, house.ymin), house.width, house.depth, color=color))
        currentAxis.add_patch(Rectangle((outer_x, outer_y), house.width + 2*house.minvr, house.depth + 2*house.minvr, fill = False, color='black'))
        currentAxis.annotate(house.id, (house.xmin + house.depth/2, house.ymin))

    plt.grid(linestyle="--")
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
