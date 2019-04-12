from house import House
from water import Water

INPUTFILE = 'properties.txt'


class Amstelhaege():
    """
    This is the full neighbourhood class.
    """
    def __init__(self):
        """
        Create houses & water
        """
        self.houses = self.load_houses(INPUTFILE, 10)
        # self.water = self.load_water()

    def load_houses(self, filename, numhouses):

        # reading data from TXTFILE
        houses_data = []

        with open(filename, "r") as f:
            house_data = []
            for line in f:
                if not line == "\n":
                    house_data.append(line.strip())
                else:
                    houses_data.append(house_data)
                    house_data = []
        houses_data.append(house_data)

        houses = {}
        id = 0

        for house_data in houses_data:
            name = house_data[0]
            depth = house_data[1]
            height = house_data[2]
            minvr = house_data[3]
            extra_wpm = house_data[4]
            worth = house_data[5]
            part = house_data[6]
            amount = int(float(part) * numhouses)

            # create house objects
            for woning in range(amount):
                house = House(id, name, depth, height, minvr, extra_wpm, worth)
                houses[id] = house
                id = id + 1

        print(houses)
        return houses


if __name__ == "__main__":
    amstelhaege = Amstelhaege()
