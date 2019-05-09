from math import sqrt

def waarde(houses):
    """
    Bepaalt de waarde van de wijk
    """
    tot_value = 0
    print(houses)
    for house in houses:
        print(house)
        olr = house['o.r.']
        house['waarde'] = 610000*(1+0.01*(olr*6))
        tot_value = tot_value + house['waarde']

    return houses, tot_value

def check_surr(new_y, new_x, house_id, houses_list, BREADTH, HEIGHT):
    """
    Checkt of het huis de juiste omliggende ruimte heeft
    """

    if new_x > BREADTH - 1 or new_x < 1 or new_y > HEIGHT - 1 or new_y < 1:
        return False

    neigh_sol = houses_list
    for house in neigh_sol:
        if house['id'] == house_id:
            house['x'] = new_x
            house['y'] = new_y

    neigh_sol = omlig_ruimte(neigh_sol, BREADTH, HEIGHT)
    for house in neigh_sol:
        # print(house['id'])
        if house['id'] == house_id:
            print(f"ID: {house_id}")
            print(f"OR: {house['o.r.']}")
            if house['o.r.'] > 1:
                return True
            else:
                return False

def omlig_ruimte(houses, BREADTH, HEIGHT):
    """
    Bepaalt de hoeveelheid omliggende ruimte en voegt toe aan de huizen dict
    """

    olr = BREADTH*HEIGHT
    for house in houses:
        x1 = house['x']
        y1 = house['y']
        id = house['id']

        for other_house in houses:
            if not other_house['id'] == id:
                # print(f"ID_2: {house['id']}")
                x2 = other_house['x']
                y2 = other_house['y']
                dist = sqrt((pow((x2-x1), 2) + pow((y2-y1), 2)))

                # seeks the lowest distance
                if dist < olr:
                    olr = int(dist)

        #check distance to border, if smaller than current olr, change
        dist_to_border = 0.5*BREADTH
        if x1 < olr:
            olr = x1
        elif y1 < olr:
            olr = y1
        elif BREADTH - x1 < olr:
            olr = BREADTH - x1
        elif HEIGHT - y1 < olr:
            olr = HEIGHT - y1

        # save surrounding space to the dictionary houses
        house['o.r.'] = olr

    return houses