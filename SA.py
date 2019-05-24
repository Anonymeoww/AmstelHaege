import random as ran
import helpers
import math
import visualize as vis

def call(ITERATIONS, HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT, current_worth):
    """
    Calls functions used for simulated annealing, sets up new neighbourhood
    """

    done_iterations = 0
    waardes = []
    SA_values = {'temperature': [], 'N-C': [], 'X': [], 'chance': []}
    best_worth = current_worth
    waardes.append(current_worth / 1000000)

    # perform simulated annealing for iterations number
    while done_iterations < ITERATIONS:
        # randomly replace house to create neighbouring solution, calculate neighbourhood value
        buur_houses_list = helpers.random_replace(HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT)
        for house in buur_houses_list:
            house.update_worth()
        buur_waarde = helpers.waarde(buur_houses_list)

        # asks for acceptance of the neighborhood. If accepted, overwrite old neighbourhood
        SA_results = sim_an(current_worth, buur_waarde, done_iterations, ITERATIONS, SA_values)
        if SA_results[0]:
            houses_list = buur_houses_list
            current_worth = buur_waarde
            if best_worth < current_worth:
                best_worth = current_worth

        done_iterations = done_iterations + 1
        waardes.append(current_worth / 1000000)

    # visualize results of generated neighbourhood
    vis.linegraph(done_iterations, waardes)
    vis.SA(SA_results[1])
    vis.grid(houses_list, best_worth)

    return waardes, houses_list


def sim_an(current_worth, next_worth, done_iterations, iterations, SA_values):
    """
    Performs silmulated annealing, returns accept or reject and simulated annealing statistics
    """

    # calculate temperature for every iteration
    temperature = calc_temp(done_iterations, iterations)
    SA_values['temperature'].append(temperature)

    # if neigboring solution is better: accept
    if next_worth >= current_worth:
        return [True, SA_values]

    # if neighboring solution is worse: calculate acceptance chance using simulated annealing
    else:
        SA_values, chance = sim_an_chance(current_worth, next_worth, temperature, SA_values)

        # if exceptance chance exceeds randomly generated value: accept
        randomvalue = ran.uniform(0.0, 1.0)
        if (chance > randomvalue) or (chance == randomvalue):
            return [True, SA_values]
        else:
            return [False, SA_values]


def calc_temp(done_iterations, iterations):
    """
    calculate temperature for current solution, scheme must be updated for viable solutions
    """
    max_temp = 100
    min_temp = 1
    temperature = max_temp * (min_temp/max_temp) ** (done_iterations/iterations)

    return temperature


def sim_an_chance(current_worth, next_worth, temperature, SA_values):
    """
    calculate chance of acceptance
    """

    # calculate difference new and current value
    diff = next_worth - current_worth
    SA_values['N-C'].append(diff)
    map = 0.0008 * diff

    # standardize difference for temperature
    x = map / temperature
    SA_values['X'].append(x)

    # calculate acceptance chance
    chance = math.e ** x
    SA_values['chance'].append(chance)

    return SA_values, chance
