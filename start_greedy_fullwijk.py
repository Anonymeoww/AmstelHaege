import random as ran
import wijk
import helpers
import visualize as vis
from house import House

def init(houses_number, n, m):
    """
    Initialiseert 3 random wijken, neemt de beste daarvan als startoplossing
    """
    eensgezins = {'type':'eensgezinswoning', 'width': 16, 'depth': 16, 'worth': 285000, 'minvr': 4}
    bungalow = {'type': 'bungalow', 'width': 20, 'depth': 15, 'worth': 399000, 'minvr': 6}
    maison = {'type': 'maison', 'width': 22, 'depth': 21, 'worth': 610000, 'minvr': 12}

    worth = 0

    numb_eensgezins = 0.6*houses_number
    numb_bungalow = 0.25*houses_number
    numb_maison = 0.15*houses_number

    for i in range(3):
        print("I IS MINDER DAN 3 VERDOMME")
        houses_list = []
        house_id = 1
        for number in range(houses_number):

            if numb_eensgezins > 0:
                type = eensgezins
                numb_eensgezins = numb_eensgezins - 1
            elif numb_bungalow > 0:
                type = bungalow
                numb_bungalow = numb_bungalow - 1
            elif numb_maison > 0:
                type = maison
                numb_maison = numb_maison - 1

            house = House(house_id, type['type'], None, None, None, None, type['minvr'], None, type['width'], type['depth'], type['worth'])
            houses_list.append(house)

            placed = False
            while placed == False:
                i = ran.randint(1, n)
                j = ran.randint(1, (m - 5))

                if helpers.check_surr(i, j, house_id, houses_list, n, m):
                    house.ymin = i
                    house.ymax = i + house.depth
                    house.xmin = j
                    house.xmax = j + house.width

                    placed = True
                    house_id = house_id + 1

        houses_list, new_worth = helpers.waarde(houses_list)

        vis.grid(houses_list, new_worth)

        # print(new_worth[1])
        if new_worth > worth:
            worth = new_worth
            final_houses_list = houses_list


    print("FINAL")
    print(worth)

    return final_houses_list
