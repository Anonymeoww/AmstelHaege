class Wijk(object):
    """
    Object with relevant information on found solution
    """

    def __init__(self, id, worth, size, map):
        """
        Initializes a neighbourhood element
        """
        self.id = id
        self.worth = worth
        self.size = size
        self.map = map

    def __str__(self):
        return f"Solution {self.id} of {self.size} houses is worth {self.worth}."