from math import sqrt
from water import Water
import random as ran


def waarde(houses_list):
    """
    Calculates the worth of the neighbourhood
    """
    tot_value = 0

    for house in houses_list:
        tot_value = tot_value + house.worth

    return tot_value

def random_replace(houses_number, water_list, houses_list, BREADTH, HEIGHT):
    """
    Moves a random house in houses_list by half a meter
    """

    # select a random house
    house_id = ran.randint(1, houses_number)

    # generate new coordinates
    for house in houses_list:
        if house.id == house_id:
            while True:
                # randomly determine the direction of movement
                x_change = ran.randint(-1, 1)
                y_change = ran.randint(-1, 1)

                house.xmin = house.xmin + x_change
                house.xmax = house.xmax + x_change
                house.ymin = house.ymin + y_change
                house.ymax = house.ymax + y_change
                if check_surr(house_id, water_list, houses_list, BREADTH, HEIGHT):
                    return houses_list

def check_surr(house_id, water_list, houses_list, BREADTH, HEIGHT):
    """
    Checks whether or not a house has the correct amount of free space
    """

    neigh_sol = houses_list

    for house in neigh_sol:

        # check if house is placed too close to the edge of the map
        if house.xmin > BREADTH - house.width - house.minvr or house.xmin < house.minvr or \
            house.ymin > HEIGHT - house.depth - house.minvr or house.ymin < house.minvr:
            return False

    # save free space data into the neighbouring solution & check for minimum requirement
    neigh_sol = omlig_ruimte(water_list, neigh_sol, BREADTH, HEIGHT)
    for house in neigh_sol:
        if house.olr < house.minvr:
            return False
    return True

def omlig_ruimte(water_list, houses_list, BREADTH, HEIGHT):
    """
    Calculates the amount of free space and saves that data to each house
    """

    for house in houses_list:
        house.olr = BREADTH*HEIGHT
        x1min = house.xmin
        x1max = house.xmax
        y1min = house.ymin
        y1max = house.ymax
        id = house.id

        house_coords = [x1min, x1max, y1min, y1max]
        combinations = [[x1min, y1min], [x1min, y1max], [x1max, y1min], [x1max, y1max]]

        # check if house is placed in water
        for water in water_list:
            water_xmin = water.xmin
            water_xmax = water.xmax
            water_ymin = water.ymin
            water_ymax = water.ymax

            water_combinations = [[water_xmin, water_ymin], [water_xmin, water_ymax], [water_xmax, water_ymin], [water_xmax, water_ymax]]

            # check if houses does not overlap water
            for combination in combinations:
                if combination[0] >= water_xmin and combination[0] <= water_xmax and \
                    combination[1] >= water_ymin and combination[1] <= water_ymax:
                    house.olr = 0
                    break


        # check if house is placed too close to or on top op another house
        if len(houses_list) > 1:
            for other_house in houses_list:
                if not other_house.id == id:
                    x2min = other_house.xmin
                    x2max = other_house.xmax
                    y2min = other_house.ymin
                    y2max = other_house.ymax

                    other_combinations = [[x2min, y2min], [x2min, y2max], [x2max, y2min], [x2max, y2max]]

                    house = pythagoras(combinations, other_combinations, house_coords, house)

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


def pythagoras(combinations, other_combinations, house_coords, house):
    """
    This function calculates the distance to other houses and checks if houses do not overlap
    """
    for combination in combinations:
        for other_combination in other_combinations:
            dist = sqrt((pow((other_combination[0]-combination[0]), 2) + pow((other_combination[1]-combination[1]), 2)))

            # seeks the lowest distance
            if house.olr > dist:
                house.olr = dist

    # check if houses do not overlap
    for other_combination in other_combinations:
        if other_combination[0] >= house_coords[0] + house.minvr and other_combination[0] <= house_coords[1] + house.minvr and \
        other_combination[1] >= house_coords[2] + house.minvr and other_combination[1] <= house_coords[3] + house.minvr:
            house.olr = 0
            break

    return house

def gen_water(BREADTH, HEIGHT):
    """
    Generates water in predetermined places
    """

    houses_list = []
    water_list = []
    water_id = 1
    water_depth = 80.5
    water_width = 71.6

    water_combinations = [[0, HEIGHT], [0, water_depth], [BREADTH - water_width, HEIGHT], [BREADTH - water_width, water_depth]]

    # generate the coordinates for water
    for water_combination in water_combinations:
        xmin = water_combination[0]
        ymax = water_combination[1]
        xmax = water_combination[0] + water_width
        ymin = water_combination[1] - water_depth
        water = Water(water_id, xmin, xmax, ymin, ymax, water_width, water_depth, 4)
        water_list.append(water)

        water_id = water_id + 1

    return water_list

def gen_rand_coord(BREADTH, HEIGHT, depth, width, minvr):
    """
    Randomly generates coordinates in the vicinity of the house
    """

    i = ran.randint(1, (BREADTH - minvr))
    j = ran.randint(1, (HEIGHT - depth - minvr))

    ymin = j
    ymax = j + depth
    xmin = i
    xmax = i + width

    return ymin, ymax, xmin, xmax

def gen_quadr_coord(depth, width, minvr, temp_houses_list, BREADTH, HEIGHT):
    """
    Generate coordinates within the quadrant with the lowest house density
    """
    # get the coordinates of the quadrant in which the house should be placed
    xminQ, xmaxQ, yminQ, ymaxQ = check_lowest_dens(temp_houses_list, BREADTH, HEIGHT)

    # generate random coordinates within that quadrant
    i = ran.randint(yminQ, (ymaxQ - minvr))
    j = ran.randint(xminQ, (xmaxQ - depth - minvr))

    ymin = i
    ymax = i + depth
    xmin = j
    xmax = j + width

    return ymin, ymax, xmin, xmax


def check_lowest_dens(temp_houses_list, BREADTH, HEIGHT):
    """
    Checks which quadrant has the lowest density in houses
    """

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    # count houses per quadrant
    for house in temp_houses_list:
        if house.xmin < (BREADTH / 2) and house.ymin > (HEIGHT / 2):
            q1 += 1
        elif house.xmin > (BREADTH / 2) and house.ymin > (HEIGHT / 2):
            q2 += 1
        elif house.xmin < (BREADTH / 2) and house.ymin < (HEIGHT / 2):
            q3 += 1
        elif house.xmin > (BREADTH / 2) and house.ymin < (HEIGHT / 2):
            q4 += 1

    # if one quadrant has less houses than the rest, return those coordinates as bounds
    if q1 < q2 and q1 < q3 and q1 < q4:
        return 0, (BREADTH / 2), (HEIGHT / 2), HEIGHT
    elif q2 < q1 and q2 < q3 and q2 < q4:
        return (BREADTH / 2), BREADTH, (HEIGHT / 2), HEIGHT
    elif q3 < q2 and q3 < q1 and q3 < q4:
        return 0, (BREADTH / 2), 0, (HEIGHT / 2)
    elif q4 < q1 and q4 < q2 and q4 < q3:
        return (BREADTH / 2), BREADTH, 0, (HEIGHT / 2)
    else:
        return 0, BREADTH, 0, HEIGHT
