import random as ran
import helpers
import math
import visualize as vis

def call(ITERATIONS, HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT, current_worth):

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
        temp.append(calc_temp(done_iterations, ITERATIONS))
        if current_worth > buur_waarde:
            nc = 0.0008 * (buur_waarde - current_worth)
            chance.append(math.e ** (nc / calc_temp(done_iterations, ITERATIONS)))
            xen.append(nc / calc_temp(done_iterations, ITERATIONS))
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


def sim_an_chance(current_worth, next_worth, temperature):
    """
    calculate chance of acceptance
    """
    # print(f"temperature: {temperature}")
    # print(f"NW - CW: {next_worth - current_worth}")
    diff = next_worth - current_worth
    map = 0.0008 * diff
    # print(map)
    x = map / temperature
    # print(f"X: {x}")
    chance = math.e ** x
    # print(f"Chance: {chance}")
    return chance

def calc_temp(done_iterations, iterations):
    """
    calculate temperature for current solution, scheme must be updated for viable solutions
    """
    max_temp = 100
    min_temp = 1
    temperature = max_temp * (min_temp/max_temp) ** (done_iterations/iterations)
    # print(temperature)

    return temperature

def sim_an(current_worth, next_worth, done_iterations, iterations):

    #als de buur beter is dan huidig, dan buur accepteren

    if next_worth > current_worth:
        return True

    # als de buur slechter is, bereken temperatuur en kans
    else:
        temperature = calc_temp(done_iterations, iterations)
        chance = sim_an_chance(current_worth, next_worth, temperature)

        #als de kans groter is dan de radomwaarde, accepteer de buur
        randomvalue = ran.uniform(0.0, 1.0)
        if (chance > randomvalue) or (chance == randomvalue):
            # print("ACCEPTS")
            return True
        else:
            return False
