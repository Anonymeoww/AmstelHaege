import random as ran
import wijk
import helpers

def init(houses_number, n, m):
    """
    Initialiseert de eerste random wijk
    """

    houses_list = []
    house_id = 1
    for number in range(houses_number):
        house = {'id': house_id, 'type': None, 'x': None, 'y': None, 'o.r.': None, 'waarde': None}
        houses_list.append(house)
        houses_number = houses_number + 1

        placed = False
        while placed == False:
            i = ran.randint(1, n)
            j = ran.randint(1, (m - 5))

            if helpers.check_surr(i, j, house_id, houses_list, n, m):
                house['y'] = i
                house['x'] = j
                print("PLACED")
                placed = True
                house_id = house_id + 1

    return houses_list