import random
import math

def iter():
    """
    create fake neighbor
    """

    iter = random.uniform(0.0,2.0)
    iterround = round(iter, 2)

    return iterround

def calc_worth(itervalue):
    """
    calculate fake worth
    """

    worth = itervalue*10

    return worth

def sim_an_chance(current_worth, next_worth, temperature):
    """
    calculate chance of acceptance
    """
    x = (next_worth - current_worth) / temperature
    chance = math.e ** x

    return chance

def calc_temp(i, current_worth):
    """
    calculate temperature for current solution
    """
    if i = 1:
        temperature = 0.2 * current_worth
    else:
        temperature = 0.5 * current_worth

    return temperature

if __name__ == "__main__":

    current_worth = 5000
    for i in range(1, 10):
        best_worth = current_worth
        itervalue = iter()
        next_worth = calc_worth(itervalue)

        #als de buur beter is, dan buur accepteren
        if next_worth > current_worth:
            current_worth = next_worth

            if next_worth > best_worth:
                best_worth = next_worth

        #als de buur slechter is, bereken temperatuur en kans
        elif next_worth < current_worth:
            temperature = calc_temp(i, current_worth)
            chance = sim_an_chance(current_worth, next_worth, temperature)

            #als de kans groter is dan de radomwaarde, accepteer de buur
            randomvalue = random.uniform(0.0, 1.0)
            if (chance > randomvalue) or (chance = randomvalue):
                current_worth = next_worth
        else:
            pass