import random as ran
import wijk
import helpers
import visualize
from house import House

def init(houses_number, n, m):
    """
    Initialiseert een greedy wijk, plaatst PER HUIS de beste optie
    """
    eensgezins = {'type':'eensgezinswoning', 'width': 16, 'depth': 16, 'worth': 285000, 'minvr': 4}
    bungalow = {'type': 'bungalow', 'width': 20, 'depth': 15, 'worth': 399000, 'minvr': 6}
    maison = {'type': 'maison', 'width': 22, 'depth': 21, 'worth': 610000, 'minvr': 12}

    houses_list = []
    house_id = 1

    # randomly initiate first house
    i = ran.randint(1, n)
    j = ran.randint(1, (m - 5))

    numb_eensgezins = 0.6*houses_number
    numb_bungalow = 0.25*houses_number
    numb_maison = 0.15*houses_number

    # house = House(house_id, maison['type'], i, j, None, maison['width'], maison['depth'], maison['worth'])
    type = maison
    i = ran.randint(1, n)
    j = ran.randint(1, (m - 5))
    house = House(house_id, type['type'], j, None, i, None, type['minvr'], None, type['width'], type['depth'], type['worth'])
    numb_maison = numb_maison + 1
    houses_list.append(house)

    houses_list = helpers.omlig_ruimte(houses_list, n, m)
    houses_list, wijkwaarde = helpers.waarde(houses_list)

    temp_houses_list = houses_list

    # randomly generate
    for number in range(houses_number - 1):
        house_id = number + 2

        if numb_eensgezins > 0:
            type = eensgezins
            numb_eensgezins = numb_eensgezins - 1
        elif numb_bungalow > 0:
            type = bungalow
            numb_bungalow = numb_bungalow - 1
        elif numb_maison > 0:
            type = maison
            numb_maison = numb_maison - 1

        temphouse = House(house_id, type['type'], None, None, None, None, type['minvr'], None, type['width'], type['depth'], type['worth'])
        print(temphouse.id)
        temp_houses_list.append(temphouse)

        tries = 0
        while tries < 10:
            placed = False

            while placed == False:
                i = ran.randint(1, n)
                j = ran.randint(1, (m - 5))

                if helpers.check_surr(i, j, house_id, temp_houses_list, n, m):
                    temphouse.ymin = i
                    temphouse.ymax = i + temphouse.depth
                    temphouse.xmin = j
                    temphouse.xmax = j + temphouse.width
                    placed = True

            temp_houses_list, new_worth = helpers.waarde(temp_houses_list)
            # visualize.grid(temp_houses_list, new_worth)

            if new_worth > wijkwaarde:
                wijkwaarde = new_worth
                houses_list = temp_houses_list

            tries = tries + 1

    return houses_list
