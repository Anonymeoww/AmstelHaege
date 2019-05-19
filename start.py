import random as ran
import wijk
import helpers
from house import House

def init(houses_number, BREADTH, HEIGHT):
    """
    Initialiseert een random wijk
    """
    eensgezins = {'type':'eensgezinswoning', 'width': 16, 'depth': 16, 'worth': 285000, 'minvr': 4}
    bungalow = {'type': 'bungalow', 'width': 20, 'depth': 15, 'worth': 399000, 'minvr': 6}
    maison = {'type': 'maison', 'width': 22, 'depth': 21, 'worth': 610000, 'minvr': 12}

    numb_eensgezins = 0.6*houses_number
    numb_bungalow = 0.25*houses_number
    numb_maison = 0.15*houses_number

    houses_list = []
    house_id = 1
    for number in range(houses_number):

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

        house = House(house_id, type['type'], xmin, xmax, ymin, ymax, type['minvr'], None, type['width'], type['depth'], type['worth'])
        houses_list.append(house)

        while helpers.check_surr(house_id, houses_list, BREADTH, HEIGHT) == False:
            ymin, ymax, xmin, xmax = helpers.gen_rand_coord(BREADTH, HEIGHT, type['depth'], type['width'], type['minvr'])
            house.ymin = ymin
            house.ymax = ymax
            house.xmin = xmin
            house.xmax = xmax

        placed = True
        house_id = house_id + 1

    return houses_list
