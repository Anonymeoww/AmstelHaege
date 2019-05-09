import random as ran
from math import sqrt
import SA
import visualize as vis
import math

import start
import helpers

"""
Hier komt een tekst te staan
"""

HOUSES_NUMBER = 10
BREADTH = 18
HEIGHT = 16
ITERATIONS = 1000

if __name__ == "__main__":

    # initieer wijk, plot , visualiseer en geef waarde aan huizen en wijk
    houses_list = start.init(HOUSES_NUMBER, BREADTH, HEIGHT)
    print(houses_list)
    houses_list = helpers.omlig_ruimte(houses_list, BREADTH, HEIGHT)
    print(houses_list)
    houses_list, curr_waarde = helpers.waarde(houses_list)
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
        buur_houses_list = SA.random_replace(HOUSES_NUMBER, houses_list, BREADTH, HEIGHT)
        buur_houses_list = helpers.omlig_ruimte(buur_houses_list, BREADTH, HEIGHT)
        buur_houses_list, buur_waarde = helpers.waarde(buur_houses_list)

        # doorsturen naar SA.py
        # print(buur_waarde)
        temp.append(SA.calc_temp(done_iterations, ITERATIONS))
        if curr_waarde > buur_waarde:
            chance.append(math.e ** ((buur_waarde-curr_waarde)/SA.calc_temp(done_iterations, ITERATIONS)))
            xen.append((buur_waarde-curr_waarde)/SA.calc_temp(done_iterations, ITERATIONS))
            nenc.append(buur_waarde-curr_waarde)
            print(f"CURR: {curr_waarde}")
            print(f"BUUR: {buur_waarde}")

        if SA.sim_an(curr_waarde, buur_waarde, done_iterations, best_worth, ITERATIONS, BREADTH, HEIGHT):
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

    print(f"Done Iterations = {done_iterations}")
    print(f"Waarde wijk: {curr_waarde}")
