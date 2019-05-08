import numpy as np
import random as ran
from math import sqrt
import SA
import visualize as vis
import math

"""
Hier komt een tekst te staan
"""

HOUSES_NUMBER = 10
BREADTH = 18
HEIGHT = 16
ITERATIONS = 1000

def init(houses_number, n, m):
    """
    Initialiseert de eerste random wijk
    """

    houses_list = []
    house_id = 1
    for number in range(houses_number):
        house = {'id': house_id, 'type': None, 'x': None, 'y': None, 'o.r.': None, 'waarde': None}
        houses_list.append(house)
        houses_number = houses_number + 1

        placed = False
        while placed == False:
            i = ran.randint(1, n)
            j = ran.randint(1, (m - 5))
            print(i)

            old_y = old_x = 0

            if check_surr(i, j, house_id, houses_list):
                house['y'] = i
                house['x'] = j
                print("PLACED")
                placed = True
                house_id = house_id + 1

    return houses_list


def waarde(houses):
    """
    Bepaalt de waarde van de wijk
    """
    tot_value = 0
    for house in houses:
        olr = house['o.r.']
        house['waarde'] = 610000*(1+0.01*(olr*6))
        tot_value = tot_value + house['waarde']

    return houses, tot_value


def random_replace(houses_number, houses_list):
    """
    verplaatst random een houses_list
    """

    # selecteer een willekeurig huis
    house_id = ran.randint(1, houses_number)

    # bepaal nieuwe coordinaten:
    for house in houses_list:
        if house['id'] == house_id:
            new_x = house['x'] + ran.randint(-1, 1)
            new_y = house['y'] + ran.randint(-1, 1)
            if check_surr(new_y, new_x, house_id, houses_list):
                house['x'] = new_x
                house['y'] = new_y
                print("VERANDERD!!!")

    return houses_list


def check_surr(new_y, new_x, house_id, houses_list):
    """
    Checkt of het huis de juiste omliggende ruimte heeft
    """

    if new_x > BREADTH - 1 or new_x < 1 or new_y > HEIGHT - 1 or new_y < 1:
        return False

    neigh_sol = houses_list
    for house in neigh_sol:
        if house['id'] == house_id:
            house['x'] = new_x
            house['y'] = new_y

    neigh_sol = omlig_ruimte(neigh_sol)
    for house in neigh_sol:
        # print(house['id'])
        if house['id'] == house_id:
            print(f"ID: {house_id}")
            print(f"OR: {house['o.r.']}")
            if house['o.r.'] > 1:
                return True
            else:
                return False


def omlig_ruimte(houses):
    """
    Bepaalt de hoeveelheid omliggende ruimte en voegt toe aan de huizen dict
    """

    olr = BREADTH*HEIGHT
    for house in houses:
        x1 = house['x']
        y1 = house['y']
        id = house['id']

        for other_house in houses:
            if not other_house['id'] == id:
                # print(f"ID_2: {house['id']}")
                x2 = other_house['x']
                y2 = other_house['y']
                dist = sqrt((pow((x2-x1), 2) + pow((y2-y1), 2)))

                # seeks the lowest distance
                if dist < olr:
                    olr = int(dist)

        #check distance to border, if smaller than current olr, change
        dist_to_border = 0.5*BREADTH
        if x1 < olr:
            olr = x1
        elif y1 < olr:
            olr = y1
        elif BREADTH - x1 < olr:
            olr = BREADTH - x1
        elif HEIGHT - y1 < olr:
            olr = HEIGHT - y1

        # save surrounding space to the dictionary houses
        house['o.r.'] = olr

    return houses


if __name__ == "__main__":

    # initieer wijk, plot , visualiseer en geef waarde aan huizen en wijk
    houses_list = init(HOUSES_NUMBER, BREADTH, HEIGHT)
    houses_list = omlig_ruimte(houses_list)
    houses_list, curr_waarde = waarde(houses_list)
    print(f"Waarde wijk: {curr_waarde}")
    best_worth = curr_waarde
    vis.grid(houses_list)

    # verander random positie huis annealing en plot
    done_iterations = 0
    waardes = []
    temp = []
    chance = []
    xen = []
    nenc = []

    while done_iterations < ITERATIONS:
        buur_houses_list = random_replace(HOUSES_NUMBER, houses_list)
        buur_houses_list = omlig_ruimte(buur_houses_list)
        buur_houses_list, buur_waarde = waarde(buur_houses_list)

        # doorsturen naar SA.py
        # print(buur_waarde)
        temp.append(SA.calc_temp(done_iterations, ITERATIONS))
        if curr_waarde > buur_waarde:
            chance.append(math.e ** ((buur_waarde-curr_waarde)/SA.calc_temp(done_iterations, ITERATIONS)))
            xen.append((buur_waarde-curr_waarde)/SA.calc_temp(done_iterations, ITERATIONS))
            nenc.append(buur_waarde-curr_waarde)
            print(f"CURR: {curr_waarde}")
            print(f"BUUR: {buur_waarde}")

        if SA.sim_an(curr_waarde, buur_waarde, done_iterations, best_worth, ITERATIONS):
          houses_list = buur_houses_list
          curr_waarde = buur_waarde
          if best_worth < curr_waarde:
              best_worth = curr_waarde

        waardes.append(curr_waarde)
        done_iterations = done_iterations + 1
        # print(waardes)

        print(f"Waarde wijk: {buur_waarde}")
        print(f"Done Iterations = {done_iterations}")
    print(houses_list)
    vis.linegraph(waardes)
    vis.grid(houses_list)
    # vis.linegraph(temp)
    # vis.linegraph(xen)
    # vis.linegraph(nenc)
    vis.SA(temp, chance, xen, nenc)

    # print(f"Done Iterations = {done_iterations}")
    # print(f"Waarde wijk: {curr_waarde}")
