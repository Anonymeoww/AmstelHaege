import random as ran
import wijk
import helpers
from house import House

def init(houses_number, n, m):
    """
    Initialiseert een greedy wijk, plaatst PER HUIS de beste optie
    """
    eensgezins = {'type':'eensgezinswoning', 'width': 8, 'depth': 8, 'worth': 285000}
    bungalow = {'type': 'bungalow', 'width': 10, 'depth': 7.5, 'worth': 399000}
    maison = {'type': 'maison', 'width': 11, 'depth': 10.5, 'worth': 610000}

    houses_list = []
    house_id = 1

    i = ran.randint(1, n)
    j = ran.randint(1, (m - 5))

    house = House(house_id, maison['type'], i, j, None, maison['width'], maison['depth'], maison['worth'])
    house_id += 1
    houses_list.append(house)

    houses_list = helpers.omlig_ruimte(houses_list, maison['width'], maison['depth'])

    wijkwaarde = helpers.waarde(houses_list)

    for x in range (5):
        for y in range (10):
            temphouse = House(house_id, maison['type'], None, None, None, maison['width'], maison['depth'], maison['worth'])
            houses_list.append(temphouse)
            placed = False

            while placed == False:
                i = ran.randint(1, n)
                j = ran.randint(1, (m - 5))

                if helpers.check_surr(i, j, house_id, houses_list, n, m):
                    temphouse.y = i
                    temphouse.x = j
                    placed = True

            print(house)

            new_worth = helpers.waarde(houses_list)

            print(new_worth[1])

            if new_worth[1] > wijkwaarde[1]:
                wijkwaarde = new_worth
                best_spot = [temphouse.x, temphouse.y]

            houses_list.pop(1)


        print("finally:")
        print(wijkwaarde[1])

        greedyhouse = House(house_id, maison['type'], best_spot[0], best_spot[1], None, maison['width'], maison['depth'], maison['worth'])
        houses_list.append(greedyhouse)
        house_id += 1


    return houses_list
