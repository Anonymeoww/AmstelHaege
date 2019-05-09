import random as ran
import math
import helpers

def random_replace(houses_number, houses_list, BREADTH,HEIGHT):
    """
    verplaatst random een houses_list
    """

    # selecteer een willekeurig huis
    house_id = ran.randint(1, houses_number)

    # bepaal nieuwe coordinaten:
    for house in houses_list:
        if house.id == house_id:
            new_x = house.x + ran.randint(-1, 1)
            new_y = house.y + ran.randint(-1, 1)
            if helpers.check_surr(new_y, new_x, house_id, houses_list, BREADTH, HEIGHT):
                house.x = new_x
                house.y = new_y
                print("VERANDERD!!!")

    return houses_list

def sim_an_chance(current_worth, next_worth, temperature):
    """
    calculate chance of acceptance
    """
    print(f"temperature: {temperature}")
    print(f"NW - CW: {next_worth - current_worth}")
    x = (next_worth - current_worth) / temperature
    print(f"X: {x}")
    chance = math.e ** x
    print(f"Chance: {chance}")
    return chance

def calc_temp(done_iterations, iterations):
    """
    calculate temperature for current solution, scheme must be updated for viable solutions
    """
    max_temp = 500000
    min_temp = 20000
    temperature = max_temp * (min_temp/max_temp) ** (done_iterations/iterations)
    # print(temperature)

    return temperature

def sim_an(current_worth, next_worth, done_iterations, best_worth, iterations, BREADTH, HEIGHT):

    #als de buur beter is dan huidig, dan buur accepteren
    # print(next_worth)
    # print(current_worth)
    if next_worth > current_worth:
        current_worth = next_worth

        # if next_worth > best_worth:
        #     best_worth = next_worth
            # print(f'best: {best_worth}')

        return True

    # als de buur slechter is, bereken temperatuur en kans
    else:
        temperature = calc_temp(done_iterations, iterations)
        chance = sim_an_chance(current_worth, next_worth, temperature)
        # print(f'chance: {chance}')

        #als de kans groter is dan de radomwaarde, accepteer de buur
        randomvalue = ran.uniform(0.0, 1.0)
        if (chance > randomvalue) or (chance == randomvalue):
            # current_worth = next_worth
            return True
        else:
            return False
