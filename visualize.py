import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def linegraph(list):
    plt.plot(list)
    # plt.plot(list1)
    # plt.plot(list2)
    # plt.plot(list3)
    plt.ylabel('Waarde')
    plt.xlabel('Iteraties')
    plt.show()


def grid(houses_list):

    x = []
    y = []

    for house in houses_list:
        x.append(house["x"])
        y.append(house["y"])
    plt.figure()
    plt.axis([0, 16, 0, 18])

    i = 0
    for point in x:
        currentAxis = plt.gca()
        currentAxis.add_patch(Rectangle((x[i], y[i]), 1, 1))
        i=i+1
    plt.show()

if __name__ == "__main__":
    linegraph(list)
