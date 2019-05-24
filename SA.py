import random as ran
import helpers
import math
import visualize as vis

def call(ITERATIONS, HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT, current_worth):

    # verander random positie huis annealing en plot
    done_iterations = 0
    waardes = []
    SA_values = {'temperature': [], 'N-C': [], 'X': [], 'chance': []}
    # temp = []
    # chance = []
    # xen = []
    # nenc = []
    best_worth = current_worth
    waardes.append(current_worth / 1000000)

    while done_iterations < ITERATIONS:
        buur_houses_list = helpers.random_replace(HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT)
        # for house in buur_houses_list:
        #     print(house.olr)
        # DIT GEBEURT NU DUBBEL, KAN MSS OOK IN EEN KEER
        # buur_houses_list = helpers.omlig_ruimte(water_list, buur_houses_list, BREADTH, HEIGHT)
        for house in buur_houses_list:
            house.update_worth()

        buur_waarde = helpers.waarde(buur_houses_list)

        # doorsturen naar SA.py
        # temp.append(calc_temp(done_iterations, ITERATIONS))
        # if current_worth > buur_waarde:
        #     nc = 0.0008 * (buur_waarde - current_worth)
        #     chance.append(math.e ** (nc / calc_temp(done_iterations, ITERATIONS)))
        #     xen.append(nc / calc_temp(done_iterations, ITERATIONS))
        #     nenc.append(nc)

        SA_results = sim_an(current_worth, buur_waarde, done_iterations, ITERATIONS, SA_values)
        if SA_results[0]:
            houses_list = buur_houses_list
            current_worth = buur_waarde
            if best_worth < current_worth:
                best_worth = current_worth

        done_iterations = done_iterations + 1
        waardes.append(current_worth / 1000000)

        # print(f"Done Iterations = {done_iterations}")
    # print(houses_list)

    # vis.linegraph(done_iterations, waardes)
    # vis.SA(temp, chance, xen, nenc)
    vis.SA(SA_values)
    # vis.grid(houses_list, best_worth)

    return waardes, houses_list

    # print(f"Done Iterations = {done_iterations}")
    # print(f"Waarde wijk: {curr_waarde}")


def calc_temp(done_iterations, iterations):
    """
    calculate temperature for current solution, scheme must be updated for viable solutions
    """
    max_temp = 100
    min_temp = 1
    temperature = max_temp * (min_temp/max_temp) ** (done_iterations/iterations)

    # print(temperature)

    return temperature


def sim_an_chance(current_worth, next_worth, temperature, SA_values):
    """
    calculate chance of acceptance
    """
    # print(f"temperature: {temperature}")
    # print(f"NW - CW: {next_worth - current_worth}")
    diff = next_worth - current_worth
    SA_values['N-C'].append(diff)
    map = 0.0008 * diff
    # print(map)
    x = map / temperature
    SA_values['X'].append(x)
    # print(f"X: {x}")
    chance = math.e ** x
    SA_values['chance'].append(chance)
    # print(f"Chance: {chance}")
    return SA_values, chance


def sim_an(current_worth, next_worth, done_iterations, iterations, SA_values):

    # save data to check if simulated annealing works well

    # Although not used every iteration, the temperature has to be calculated
    # every iteration to give a good graph of its path
    temperature = calc_temp(done_iterations, iterations)
    SA_values['temperature'].append(temperature)

    # als de buur beter is dan huidig, dan buur accepteren
    if next_worth > current_worth:
        return [True, SA_values]

    # als de buur slechter is, bereken temperatuur en kans
    else:
        SA_values, chance = sim_an_chance(current_worth, next_worth, temperature, SA_values)

        #als de kans groter is dan de radomwaarde, accepteer de buur
        randomvalue = ran.uniform(0.0, 1.0)
        if (chance > randomvalue) or (chance == randomvalue):
            return [True, SA_values]
        else:
            return [False, SA_values]
