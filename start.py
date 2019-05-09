import random as ran
import wijk
import helpers
from house import House

def init(houses_number, n, m):
    """
    Initialiseert de eerste random wijk
    """
    eensgezins = {'type':'eensgezinswoning', 'width': 8, 'depth': 8, 'worth': 285000}
    bungalow = {'type': 'bungalow', 'width': 10, 'depth': 7.5, 'worth': 399000}
    maison = {'type': 'maison', 'width': 11, 'depth': 10.5, 'worth': 610000}

    houses_list = []
    house_id = 1
    for number in range(houses_number):
        house = House(house_id, maison['type'], None, None, None, maison['width'], maison['depth'], maison['worth'])
        print("yeet")
        print(house.id)
        houses_list.append(house)
        houses_number = houses_number + 1

        placed = False
        while placed == False:
            i = ran.randint(1, n)
            j = ran.randint(1, (m - 5))

            if helpers.check_surr(i, j, house_id, houses_list, n, m):
                house.y = i
                house.x = j
                print("PLACED")
                placed = True
                house_id = house_id + 1

    print(houses_list)

    return houses_list