import numpy as np
import random as ran
from math import sqrt
# import Dilisha
import SA
import visualize as vis

"""
Hier komt een tekst te staan
"""

HOUSES_NUMBER = 10
BREADTH = 16
HEIGHT = 18
ITERATIONS = 2000

def init(houses_number, n, m):
    """
    Initialiseert en plot de eerste wijk
    """

    # initialize Amstelhaege
    ah = np.array([[0] * n for i in range(m)])

    # plot Amstelhaege
    houses_list = []
    house_id = 1
    while houses_number > 0:
        i = ran.randint(1, n)
        j = ran.randint(1, (m - 5))

        old_y = old_x = 0

        if check_surr(ah, i, j, house_id, old_y, old_x):
            ah[i][j] = house_id
            houses_list.append({'id': house_id, 'x': j, 'y': i, 'o.r.': None, 'waarde': None})
            house_id = house_id + 1
            houses_number = houses_number - 1

    return ah, houses_list


def plot(ah, houses_list):
    """
    Plot de wijk
    """

    for house in houses_list:
        j = house['x']
        i = house['y']
        ah[i][j] = house['id']
    # print(ah)


def visualiseer(Amstelhaege):
    """
    Visualiseert de wijk
    """

    return []


def waarde(houses):
    """
    Bepaalt de waarde van de wijk
    """
    tot_value = 0
    for house in houses:
        olr = house['o.r.']
        house['waarde'] = 610000*(1+0.01*(olr*6))
        tot_value = tot_value + house['waarde']

    # print(houses)

    return houses, tot_value


def random_replace(ah, houses_number, houses_list):
    """
    verplaatst random een houses_list
    """

    # selecteer een willekeurig huis
    house_id = ran.randint(1, houses_number)
    # print(f"house_id: {house_id}")

    # bepaal nieuwe coordinaten:
    for house in houses_list:
        if house['id'] == house_id:
            # print(f"Old x: {house['x']}")
            # print(f"Old y: {house['y']}")
            new_x = house['x'] + ran.randint(-1, 1)
            new_y = house['y'] + ran.randint(-1, 1)

    # print(f"New x: {new_x}")
    # print(f"New y: {new_y}")

    # voer de verandering door
    return change(ah, houses_list, house_id, new_x, new_y)


def check_surr(ah, i, j, house_id, old_y, old_x):
    """
    Checkt of het huis de juiste omliggende ruimte heeft
    """
    # print(house_id)
    house_id = (0 or house_id)
    if ah[i-1][j-1] == ah[i-1][j] == ah[i-1][j+1] == ah[i][j-1] == ah[i][j+1] ==\
        ah[i+1][j-1] == ah[i+1][j] == ah[i+1][j+1] == ah[i][j] == 0:
        return True

    ah[old_y][old_x] = 0
    # print(i)
    # print(j)
    if old_y < 15 and old_y > 1 and old_x < 13 and old_x > 1:
        if ah[i-1][j-1] == ah[i-1][j] == ah[i-1][j+1] == ah[i][j-1] == ah[i][j+1] ==\
            ah[i+1][j-1] == ah[i+1][j] == ah[i+1][j+1] == ah[i][j] == 0:
            return True
        else:
            return False
    else:
        return False


def change(ah, houses_list, house_id, new_x, new_y):
    """
    Veranderd de positie van het huis en plot de nieuwe wijk
    """

    for house in houses_list:
        if house['id'] == house_id:
            old_y = house['y']
            old_x = house['x']
            if check_surr(ah, new_y, new_x, house_id, old_y, old_x):
                ah[house['y']][house['x']] = 0
                ah[int(new_y)][int(new_x)] = house['id']
                house['x'] = int(new_x)
                house['y'] = int(new_y)
                # print("VERANDERD!!!")

    return ah, houses_list


def omlig_ruimte(houses):
    """
    Bepaalt de hoeveelheid omliggende ruimte en voegt toe aan de huizen dict
    """

    for house in houses:
        olr = 24
        x1 = house['x']
        y1 = house['y']
        id = house['id']

        for other_house in houses:
            if not other_house['id'] == id:
                # print(f"ID_2: {house['id']}")
                x2 = other_house['x']
                y2 = other_house['y']
                dist = sqrt((pow((x2-x1), 2) + pow((y2-y1), 2)))

                # seeks the lowest distance, round to whole meters (-1 bc of mandatory space)
                if dist < olr:
                    olr = int(dist) - 1

        # save surrounding space to the dictionary houses
        house['o.r.'] = olr

    return houses


if __name__ == "__main__":

    # initieer wijk, plot , visualiseer en geef waarde aan huizen en wijk
    Amstelhaege, houses_list = init(HOUSES_NUMBER, BREADTH, HEIGHT)
    houses_list = omlig_ruimte(houses_list)
    houses_list, curr_waarde = waarde(houses_list)
    plot(Amstelhaege, houses_list)
    # print(f"Waarde wijk: {curr_waarde}")
    best_worth = curr_waarde
    vis.grid(houses_list)
    # print(Amstelhaege)

    # verander random positie huis annealing en plot
    done_iterations = 0
    waardes = []
    while done_iterations <= ITERATIONS:
        buur_Amstelhaege, buur_houses_list = random_replace(Amstelhaege, HOUSES_NUMBER, houses_list)
        plot(buur_Amstelhaege, buur_houses_list)
        buur_houses_list = omlig_ruimte(buur_houses_list)
        buur_houses_list, buur_waarde = waarde(buur_houses_list)

        done_iterations = done_iterations + 1

        # doorsturen naar SA.py
        # print(buur_waarde)
        if SA.sim_an(curr_waarde, buur_waarde, done_iterations, best_worth):
          Amstelhaege = buur_Amstelhaege
          houses_list = buur_houses_list
          curr_waarde = buur_waarde
          if best_worth < curr_waarde:
              best_worth = curr_waarde

        waardes.append(curr_waarde)
        print(waardes)

        print(f"Waarde wijk: {buur_waarde}")
        print(f"Done Iterations = {done_iterations}")
    # print(houses_list)
    vis.linegraph(waardes)
    vis.grid(houses_list)
    # print(Amstelhaege)

    # print(f"Done Iterations = {done_iterations}")
    # print(f"Waarde wijk: {curr_waarde}")
    # plot(Amstelhaege, houses_list)
