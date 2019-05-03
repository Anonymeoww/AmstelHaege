import random
import math

def sim_an_chance(current_worth, next_worth, temperature):
    """
    calculate chance of acceptance
    """
    x = (next_worth - current_worth) / temperature
    chance = math.e ** x

    return chance

def calc_temp(i, current_worth):
    """
    calculate temperature for current solution, scheme must be updated for viable solutions
    """
    if i == 1:
        temperature = 0.8 * current_worth
    else:
        temperature = 0.3 * current_worth

    return temperature

def sim_an(current_worth, next_worth, done_iterations, best_worth):

    #als de buur beter is dan huidig, dan buur accepteren
    # print(next_worth)
    # print(current_worth)
    if next_worth > current_worth:
        current_worth = next_worth

        if next_worth > best_worth:
            best_worth = next_worth
            # print(f'best: {best_worth}')

        return True

    # als de buur slechter is, bereken temperatuur en kans
    else:
        temperature = calc_temp(done_iterations, current_worth)
        chance = sim_an_chance(current_worth, next_worth, temperature)
        # print(f'chance: {chance}')

        #als de kans groter is dan de radomwaarde, accepteer de buur
        randomvalue = random.uniform(0.0, 1.0)
        if (chance > randomvalue) or (chance == randomvalue):
            current_worth = next_worth
            return True
        else:
            return False
