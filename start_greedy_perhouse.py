import random as ran
import wijk
import helpers
import visualize
from house import House

def init(houses_number, BREADTH, HEIGHT):
    """
    Initialiseert een greedy wijk, plaatst PER HUIS de beste optie
    """

    # first, randomly place water
    water_list = helpers.gen_water(BREADTH, HEIGHT)

    eensgezins = {'type':'eensgezinswoning', 'width': 16, 'depth': 16, 'base_worth': 285000, 'minvr': 4, 'extra': 3}
    bungalow = {'type': 'bungalow', 'width': 20, 'depth': 15, 'base_worth': 399000, 'minvr': 6, 'extra': 4}
    maison = {'type': 'maison', 'width': 22, 'depth': 21, 'base_worth': 610000, 'minvr': 12, 'extra': 6}

    houses_list = []
    house_id = 1

    # randomly initiate first house
    numb_eensgezins = 0.6*houses_number
    numb_bungalow = 0.25*houses_number
    numb_maison = 0.15*houses_number

    # house = House(house_id, maison['type'], i, j, None, maison['width'], maison['depth'], maison['worth'])
    type = maison
    ymin, ymax, xmin, xmax = helpers.gen_rand_coord(BREADTH, HEIGHT, type['depth'], type['width'], type['minvr'])

    house = House(house_id, type['type'], xmin, xmax, ymin, ymax, type['minvr'], 0, type['width'], type['depth'], type['extra'], type['base_worth'], type['base_worth'])
    houses_list.append(house)

    numb_maison = numb_maison + 1

    houses_list = helpers.omlig_ruimte(water_list, houses_list, BREADTH, HEIGHT)
    wijkwaarde = helpers.waarde(houses_list)

    temp_houses_list = houses_list

    # randomly generate
    for number in range(houses_number - 1):
        house_id = number + 2

        if numb_maison > 0:
            type = maison
            numb_maison = numb_maison - 1
        elif numb_bungalow > 0:
            type = bungalow
            numb_bungalow = numb_bungalow - 1
        elif numb_eensgezins > 0:
            type = eensgezins
            numb_eensgezins = numb_eensgezins - 1

        temphouse = House(house_id, type['type'], xmin, xmax, ymin, ymax, type['minvr'], 0, type['width'], type['depth'], type['extra'], type['base_worth'], type['base_worth'])
        temp_houses_list.append(temphouse)

        tries = 0
        while tries < 10:
            placed = False

            while placed == False:
                ymin, ymax, xmin, xmax = helpers.gen_rand_coord(BREADTH, HEIGHT, type['depth'], type['width'], type['minvr'])
                temphouse.ymin = ymin
                temphouse.ymax = ymax
                temphouse.xmin = xmin
                temphouse.xmax = xmax
                temphouse.update_worth()

                if helpers.check_surr(house_id, water_list, temp_houses_list, BREADTH, HEIGHT):
                    placed = True

            new_worth = helpers.waarde(temp_houses_list)

            if new_worth > wijkwaarde:
                wijkwaarde = new_worth
                houses_list = temp_houses_list

            tries = tries + 1

    return water_list, houses_list
