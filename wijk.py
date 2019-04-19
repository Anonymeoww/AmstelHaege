import numpy as np
import random as ran
from math import sqrt

"""
Hier komt een tekst te staan
"""

# TODO:
# neem random huis en verplaats --> simulated annealing
# herhaal een aantal keer.

def plot():
    """
    Plot de initiele wijk
    """

    # initialize Amstelhaege
    n = 16
    m = 18
    houses = 20
    ah = np.array([[0] * n for i in range(m)])

    # plot Amstelhaege
    houses_list = []
    house_id = 1
    while houses > 0:
        i = ran.randint(1, n)
        j = ran.randint(1, (m - 5))

        if ((ah[i-1][j-1] == 0) and (ah[i-1][j] == 0) and (ah[i-1][j+1] == 0)\
            and (ah[i][j-1] == 0) and (ah[i][j+1] == 0) and (ah[i+1][j-1] == 0)\
            and (ah[i+1][j] == 0) and (ah[i+1][j+1] == 0) and ah[i][j] == 0):
            ah[i][j] = house_id
            houses_list.append({'id': house_id, 'x': j, 'y': i, 'o.r.': None, 'waarde': None})
            house_id = house_id + 1
            houses = houses - 1

    # print(houses_list)
    print(ah)

    return ah, houses_list


def visualiseer(Amstelhaege):
    """
    Visualiseert de wijk
    """

    return []


def omlig_ruimte(houses):
    """
    Bepaalt de hoeveelheid omliggende ruimte en voegt toe aan de huizen dict
    """

    for house in houses:
        olr = 24
        x1 = house['x']
        y1 = house['y']
        id = house['id']
        # print(f"ID_1: {id}")

        for other_house in houses:
            if not other_house['id'] == id:
                # print(f"ID_2: {house['id']}")
                x2 = other_house['x']
                y2 = other_house['y']
                dist = sqrt((pow((x2-x1), 2) + pow((y2-y1), 2)))

                # seeks the lowest distance, round to whole meters (-1 bc of mandatory space)
                if dist < olr:
                    olr = int(dist) - 1
                    # print(olr)

        # save surrounding space to the dictionary houses
        house['o.r.'] = olr
        # print(house)

    print(houses)

    return houses


def waarde(houses):
    """
    Bepaalt de waarde van de wijk
    """
    tot_value = 0
    for house in houses:
        olr = house['o.r.']
        house['waarde'] = 610000*(1+0.01*(olr*6))
        tot_value = tot_value + house['waarde']

    print(houses)
    print(tot_value)

    return houses, tot_value


if __name__ == "__main__":
    # initieer wijk
    Amstelhaege, houses = plot()

    # visualiseer huidige wijk
    visualiseer(Amstelhaege)

    # bepaal omliggende ruimte
    houses = omlig_ruimte(houses)

    # bereken waarde wijk
    houses, waarde = waarde(houses)
