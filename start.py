import random as ran
import wijk
import helpers
from house import House

def init(houses_number, BREADTH, HEIGHT):
    """
    Initialiseert een random wijk
    """

    # first, randomly place water
    water_list = helpers.gen_water(BREADTH, HEIGHT)

    eensgezins = {'type':'eensgezinswoning', 'width': 16, 'depth': 16, 'base_worth': 285000, 'minvr': 4, 'extra': 3}
    bungalow = {'type': 'bungalow', 'width': 20, 'depth': 15, 'base_worth': 399000, 'minvr': 6, 'extra': 4}
    maison = {'type': 'maison', 'width': 22, 'depth': 21, 'base_worth': 610000, 'minvr': 12, 'extra': 6}

    # calculate number of houses for each house type
    numb_eensgezins = 0.6*houses_number
    numb_bungalow = 0.25*houses_number
    numb_maison = 0.15*houses_number

    # for each house that needs to be placed, generate random coordinates
    houses_list = []
    house_id = 1
    for number in range(houses_number):

        # check which house needs to be placed
        if numb_maison > 0:
            type = maison
            numb_maison = numb_maison - 1
        elif numb_bungalow > 0:
            type = bungalow
            numb_bungalow = numb_bungalow - 1
        elif numb_eensgezins > 0:
            type = eensgezins
            numb_eensgezins = numb_eensgezins - 1

        ymin, ymax, xmin, xmax = helpers.gen_rand_coord(BREADTH, HEIGHT, type['depth'], type['width'], type['minvr'])

        house = House(house_id, type['type'], xmin, xmax, ymin, ymax, type['minvr'], 0, type['width'], type['depth'], type['extra'], type['base_worth'], type['base_worth'])
        houses_list.append(house)

        # while the free space requirements aren't yet satisfied, generate new random coordinates
        while helpers.check_surr(house_id, water_list, houses_list, BREADTH, HEIGHT) == False:
            ymin, ymax, xmin, xmax = helpers.gen_rand_coord(BREADTH, HEIGHT, type['depth'], type['width'], type['minvr'])
            house.ymin = ymin
            house.ymax = ymax
            house.xmin = xmin
            house.xmax = xmax
            house.update_worth()

        placed = True
        house_id = house_id + 1

    return water_list, houses_list
