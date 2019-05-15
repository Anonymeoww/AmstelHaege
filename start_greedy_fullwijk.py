import random as ran
import wijk
import helpers
from house import House

def init(houses_number, n, m):
    """
    Initialiseert 3 random wijken, neemt de beste daarvan als startoplossing
    """
    eensgezins = {'type':'eensgezinswoning', 'width': 8, 'depth': 8, 'worth': 285000}
    bungalow = {'type': 'bungalow', 'width': 10, 'depth': 7.5, 'worth': 399000}
    maison = {'type': 'maison', 'width': 11, 'depth': 10.5, 'worth': 610000}

    worth = 0

    for i in range(3):
        print("I IS MINDER DAN 3 VERDOMME")
        houses_list = []
        house_id = 1
        for number in range(houses_number):
            house = House(house_id, maison['type'], None, None, None, maison['width'], maison['depth'], maison['worth'])
            houses_list.append(house)
            houses_number = houses_number + 1

            placed = False
            while placed == False:
                i = ran.randint(1, n)
                j = ran.randint(1, (m - 5))

                if helpers.check_surr(i, j, house_id, houses_list, n, m):
                    house.y = i
                    house.x = j

                    placed = True
                    house_id = house_id + 1

        new_worth = helpers.waarde(houses_list)
        print(new_worth[1])
        if new_worth[1] > worth:
            worth = new_worth[1]
            final_houses_list = houses_list


    print("FINAL")
    print(worth)

    return final_houses_list
