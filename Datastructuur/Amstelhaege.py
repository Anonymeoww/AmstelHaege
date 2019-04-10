from house import House

class Amstelhaege():
    """
    This is the full neighbourhood class.
    """

    def __init__(self):
        """
        Create houses & water
        """
        self.houses = self.load_houses("properties.txt")
        # self.water = self.load_water()

    def load_houses(self, filename):

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

        for house_data in houses_data:
            name = house_data[0]
            depth = house_data[1]
            height = house_data[2]
            minvr = house_data[3]
            extra_wpm = house_data[4]
            worth = house_data[5]

            house = House(name, depth, height, minvr, extra_wpm, worth)
            houses[name] = house

        return houses
        # should return list of dictionaries for each house. Each dictionary is {'house_id': 'x,y'}


if __name__ == "__main__":
    amstelhaege = Amstelhaege()
