import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.ticker as ticker
import locale

def linegraph(iter, list):
    """
    Generates a linegraph that visualizes the HC or SA process
    """

    iterations = [item for item in range(0, iter+1)]
    maxval = max(list)
    minval = min(list)
    plt.plot(iterations, list)
    plt.ylabel('Waarde x 1.000.000')
    plt.xlabel('Iteraties')
    plt.axis([0, iter, minval - 0.5, maxval + 0.5])
    plt.show()

def linegraph_compare(iter, list1, list2):
    """
    Generates a linegraph containing outputs for HC and SA
    """
    iterations = [item for item in range(0, iter)]
    maxval = max([max(list1), max(list2)])
    minval = min([min(list1), min(list2)])
    plt.title("HC and SA compared")
    plt.plot(iterations, list1, label='HillClimber')
    plt.plot(iterations, list2, label='Simulated Annealing')
    plt.legend(loc='upper left')
    plt.ylabel('Waarde x 1.000.000')
    plt.xlabel('Iteraties')
    plt.axis([0, iter, minval - 0.5, maxval + 0.5])
    plt.show()

def grid(water_list, houses_list, worth, method):
    """
    Visualizes the neighbourhood
    """

    locale.setlocale(locale.LC_ALL, 'nl_NL')
    value = locale.currency(worth, grouping=True)

    fig, ax = plt.subplots()
    plt.title(f"{method}: Totale wijkwaarde: {value}")
    plt.axis([0, 320, 0, 360])
    ax.set_facecolor('#DBFEB8')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(40))

    for water in water_list:
        currentAxis = plt.gca()
        color = '#4286f4'
        outer_x = water.xmin - water.minvr
        outer_y = water.ymin - water.minvr
        currentAxis.add_patch(Rectangle((water.xmin, water.ymin), water.width, water.depth, color=color))
        currentAxis.annotate(water.id, (water.xmin + water.depth/2, water.ymin))

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

def SA(SA_values):
    """
    Visualizes the outputs used in simulated annealing
    """

    fig, axs = plt.subplots(2, 2, figsize=(5, 5))
    axs[0, 0].plot(SA_values['temperature'])
    axs[0, 0].set_title('temperature')
    axs[1, 0].plot(SA_values['chance'])
    axs[1, 0].set_title('chance')
    axs[0, 1].plot(SA_values['X'])
    axs[0, 1].set_title('X')
    axs[1, 1].plot(SA_values['N-C'])
    axs[1, 1].set_title('N-C')

    plt.show()
