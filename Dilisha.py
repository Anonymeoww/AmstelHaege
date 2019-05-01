import random
import math

def iter():
    """
    can be used to create neighboring solution
    """
    # Should return the value of the neighboring solution (wijk waarde)
    pass

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
        temperature = 0.5 * current_worth

    return temperature

def sim_an(current_worth):

    current_worth = current_worth
    best_worth = current_worth
    #for loop needs stop condition
    for i in range(1, 10):
        next_worth = iter()
        print(f'current: {current_worth}')
        print(f'next: {next_worth}')

        #als de buur beter is dan huidig, dan buur accepteren
        if next_worth > current_worth:
            current_worth = next_worth

            if next_worth > best_worth:
                best_worth = next_worth
                print(f'best: {best_worth}')

        #als de buur slechter is, bereken temperatuur en kans
        elif next_worth < current_worth:
            temperature = calc_temp(i, current_worth)
            chance = sim_an_chance(current_worth, next_worth, temperature)
            print(f'chance: {chance}')

            #als de kans groter is dan de radomwaarde, accepteer de buur
            randomvalue = random.uniform(0.0, 1.0)
            if (chance > randomvalue) or (chance == randomvalue):
                current_worth = next_worth
        else:
            pass
    print(f'best: {best_worth}')

if __name__ == "__main__":
    current_worth = 5 #adjust value to relevant
    sim_an(current_worth)
