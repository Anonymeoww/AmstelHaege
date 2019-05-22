import SA
import helpers
import math
import visualize as vis

def call_SA(HOUSES_NUMBER, ITERATIONS, houses_list, BREADTH, HEIGHT, current_worth):

    # verander random positie huis annealing en plot
    done_iterations = 0
    waardes = []
    temp = []
    chance = []
    xen = []
    nenc = []
    best_worth = current_worth
    waardes.append(current_worth / 1000000)

    while done_iterations < ITERATIONS:
        buur_houses_list = helpers.random_replace(HOUSES_NUMBER, houses_list, BREADTH, HEIGHT)
        # DIT GEBEURT NU DUBBEL, KAN MSS OOK IN EEN KEER
        buur_houses_list = helpers.omlig_ruimte(buur_houses_list, BREADTH, HEIGHT)
        for house in buur_houses_list:
            house.update_worth()

        buur_waarde = helpers.waarde(buur_houses_list)

        # doorsturen naar SA.py
        temp.append(SA.calc_temp(done_iterations, ITERATIONS))
        if current_worth > buur_waarde:
            nc = 0.0008 * (buur_waarde - current_worth)
            chance.append(math.e ** (nc / SA.calc_temp(done_iterations, ITERATIONS)))
            xen.append(nc / SA.calc_temp(done_iterations, ITERATIONS))
            nenc.append(nc)

        if SA.sim_an(current_worth, buur_waarde, done_iterations, ITERATIONS):
            houses_list = buur_houses_list
            current_worth = buur_waarde
            if best_worth < current_worth:
                best_worth = current_worth

        done_iterations = done_iterations + 1
        waardes.append(current_worth / 1000000)

        # print(f"Done Iterations = {done_iterations}")
    # print(houses_list)

    # vis.linegraph(done_iterations, waardes)
    # vis.grid(houses_list, best_worth)
    # vis.SA(temp, chance, xen, nenc)

    return houses_list

    # print(f"Done Iterations = {done_iterations}")
    # print(f"Waarde wijk: {curr_waarde}")
