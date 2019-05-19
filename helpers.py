from math import sqrt
from house import House
import random as ran

def waarde(houses_list):
    """
    Bepaalt de waarde van de wijk
    """
    tot_value = 0

    for house in houses_list:

        olr = house.olr

        worth = house.worth * (1 + 0.01 * (olr * 6))
        tot_value = tot_value + worth

    return houses_list, tot_value

def check_surr(house_id, houses_list, BREADTH, HEIGHT):
    """
    Checkt of het huis de juiste omliggende ruimte heeft
    """

    neigh_sol = houses_list
    numb_houses = len(houses_list)
    for house in neigh_sol:

        if house.xmin > BREADTH - house.width - house.minvr or house.xmin < house.minvr or \
            house.ymin > HEIGHT - house.depth - house.minvr or house.ymin < house.minvr:
            return False

    neigh_sol = omlig_ruimte(neigh_sol, house_id, BREADTH, HEIGHT)

    for house in neigh_sol:
        if house.olr < house.minvr:
            return False
    return True

def omlig_ruimte(houses_list, house_id, BREADTH, HEIGHT):
    """
    Bepaalt de hoeveelheid omliggende ruimte en voegt toe aan de huizen dict
    """

    for house in houses_list:
        house.olr = BREADTH*HEIGHT
        x1min = house.xmin
        x1max = house.xmax
        y1min = house.ymin
        y1max = house.ymax
        id = house.id

        combinations = [[x1min, y1min], [x1min, y1max], [x1max, y1min], [x1max, y1max]]

        if len(houses_list) > 1:
            for other_house in houses_list:
                if not other_house.id == id:
                    x2min = other_house.xmin
                    x2max = other_house.xmax
                    y2min = other_house.ymin
                    y2max = other_house.ymax

                    other_combinations = [[x2min, y2min], [x2min, y2max], [x2max, y2min], [x2max, y2max]]

                    for combination in combinations:
                        for other_combination in other_combinations:
                            dist = sqrt((pow((other_combination[0]-combination[0]), 2) + pow((other_combination[1]-combination[1]), 2)))

                            # seeks the lowest distance
                            if house.olr > dist:
                                house.olr = dist

                    # check if houses do not overlap
                    for other_combination in other_combinations:
                        if other_combination[0] >= x1min + house.minvr and other_combination[0] <= x1max + house.minvr and \
                        other_combination[1] >= y1min + house.minvr and other_combination[1] <= y1max + house.minvr:
                            house.olr = 0
                            break

            #check distance to border, if smaller than current olr, change
            if x1min < house.olr:
                house.olr = x1min
            elif y1min < house.olr:
                house.olr = y1min
            elif BREADTH - x1max < house.olr:
                house.olr = BREADTH - x1max
            elif HEIGHT - y1max < house.olr:
                house.olr = HEIGHT - y1max

    return houses_list

def gen_rand_coord(BREADTH, HEIGHT, depth, width, minvr):

    i = ran.randint(1, (HEIGHT - width - minvr))
    j = ran.randint(1, (BREADTH - depth - minvr))
    ymin = i
    ymax = i + depth
    xmin = j
    xmax = j + width


    return ymin, ymax, xmin, xmax
