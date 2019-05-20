from math import sqrt
from house import House
import random as ran

def waarde(houses_list):
    """
    Bepaalt de waarde van de wijk
    """
    tot_value = 0

    for house in houses_list:
        tot_value = tot_value + house.worth

    return tot_value

def random_replace(houses_number, houses_list, BREADTH,HEIGHT):
    """
    verplaatst random een houses_list
    """

    # selecteer een willekeurig huis
    house_id = ran.randint(1, houses_number)

    # bepaal nieuwe coordinaten:
    for house in houses_list:
        if house.id == house_id:
            while True:
                # print("yeet")
                # randomly determine the direction of movement
                x_change = ran.randint(-1, 1)
                y_change = ran.randint(-1, 1)

                house.xmin = house.xmin + x_change
                house.xmax = house.xmax + x_change
                house.ymin = house.ymin + y_change
                house.ymax = house.ymax + y_change
                if check_surr(house_id, houses_list, BREADTH, HEIGHT):
                    # print("yeet")
                    return houses_list

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

    neigh_sol = omlig_ruimte(neigh_sol, BREADTH, HEIGHT)

    for house in neigh_sol:
        if house.olr < house.minvr:
            return False
    return True

def omlig_ruimte(houses_list, BREADTH, HEIGHT):
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

    i = ran.randint(1, (BREADTH - minvr))
    j = ran.randint(1, (HEIGHT - depth - minvr))

    ymin = i
    ymax = i + depth
    xmin = j
    xmax = j + width

    return ymin, ymax, xmin, xmax

def gen_quadr_coord(depth, width, minvr, temp_houses_list):

    xminQ, xmaxQ, yminQ, ymaxQ = check_lowest_dens(temp_houses_list)

    i = ran.randint(yminQ, (ymaxQ - minvr))
    j = ran.randint(xminQ, (xmaxQ - depth - minvr))

    ymin = i
    ymax = i + depth
    xmin = j
    xmax = j + width

    return ymin, ymax, xmin, xmax


def check_lowest_dens(temp_houses_list):
    "Checks which quadrant has the lowest density houses"

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for house in temp_houses_list:
        if house.xmin < 180 and house.ymin > 160:
            q1 += 1
        elif house.xmin > 180 and house.ymin > 160:
            q2 += 1
        elif house.xmin < 180 and house.ymin < 160:
            q3 += 1
        elif house.xmin > 180 and house.ymin < 160:
            q4 += 1


    if q1 < q2 and q1 < q3 and q1 < q4:
        return 0, 180, 160, 320
    elif q2 < q1 and q2 < q3 and q2 < q4:
        return 180, 360, 160, 320
    elif q3 < q2 and q3 < q1 and q3 < q4:
        return 0, 180, 0, 160
    elif q4 < q1 and q4 < q2 and q4 < q3:
        return 180, 360, 0, 160
    else:
        return 0, 360, 0, 320
