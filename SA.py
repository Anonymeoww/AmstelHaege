import random as ran
import math
import helpers


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
