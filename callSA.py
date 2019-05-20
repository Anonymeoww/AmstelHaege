import SA
import helpers
import math
import visualize as vis

def call_SA(HOUSES_NUMBER, ITERATIONS, houses_list, BREADTH, HEIGHT, curr_waarde, best_worth):

    # verander random positie huis annealing en plot
    done_iterations = 0
    waardes = []
    temp = []
    chance = []
    xen = []
    nenc = []

    while done_iterations < ITERATIONS:
        buur_houses_list = helpers.random_replace(HOUSES_NUMBER, houses_list, BREADTH, HEIGHT)
        # DIT GEBEURT NU DUBBEL, KAN MSS OOK IN EEN KEER
        buur_houses_list = helpers.omlig_ruimte(buur_houses_list, BREADTH, HEIGHT)
        for house in buur_houses_list:
            house.update_worth()

        buur_waarde = helpers.waarde(buur_houses_list)

        # doorsturen naar SA.py
        temp.append(SA.calc_temp(done_iterations, ITERATIONS))
        if curr_waarde > buur_waarde:
            chance.append(math.e ** ((buur_waarde - curr_waarde) / SA.calc_temp(done_iterations, ITERATIONS)))
            xen.append((buur_waarde - curr_waarde) / SA.calc_temp(done_iterations, ITERATIONS))
            nenc.append(buur_waarde - curr_waarde)
            # print(f"CURR: {curr_waarde}")
            # print(f"BUUR: {buur_waarde}")

        if SA.sim_an(curr_waarde, buur_waarde, done_iterations, ITERATIONS):
            # print("yoot")
            houses_list = buur_houses_list
            curr_waarde = buur_waarde
            if best_worth < curr_waarde:
                best_worth = curr_waarde

            waardes.append(curr_waarde / 1000000)
        done_iterations = done_iterations + 1
        # print(waardes)

        # print(f"Waarde wijk: {buur_waarde}")
        print(f"Done Iterations = {done_iterations}")
    # print(houses_list)
    iter = len(waardes)
    vis.linegraph(iter, waardes)
    vis.grid(houses_list, best_worth)
    # vis.linegraph(temp)
    # vis.linegraph(xen)
    # vis.linegraph(nenc)
    vis.SA(temp, chance, xen, nenc)

    # print(f"Done Iterations = {done_iterations}")
    # print(f"Waarde wijk: {curr_waarde}")
