
class Amstelhaege():
    """
    This is the full neighbourhood class.
    """

    def __init__(self, numhouses):
        """
        Create houses & water
        """
        self.houses = self.load_houses(properties.txt)
        # self.water = self.load_water()

    def load_houses(self, filename):

        houses_data = []

        with open(filename, "r") as f:
            for line in f:
                house_data = []
                house_data.append(line)
                houses_data.append(house_data)
                print(house_data)
        print(houses_data)

        # should return list of dictionaries for each house. Each dictionary is {'house_id': 'x,y'}


    def load_water(self):

        # should return list of dictionaries for each water body? Each dictionary is {'water_id': 'x,y'}


if __name__ == "__main__":

    Amstelhaege = 
