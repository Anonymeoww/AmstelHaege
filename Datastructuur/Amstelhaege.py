
class Amstelhaege():
    """
    This is the full neighbourhood class.
    """

    def __init__(self, numhouses):
        """
        Create houses & water
        """
        self.houses = self.load_houses(TXTFILE, numhouses)
        self.water = self.load_water()

    def load_houses(self, TXTFILE, numhouses):

        # should return list of dictionaries for each house. Each dictionary is {'house_id': 'x,y'}


    def load_water(self):

        # should return list of dictionaries for each water body? Each dictionary is {'water_id': 'x,y'}
        #woooooop