class House(object):
    """
    Representation of a house in AmstelHaege
    """

    def __init__(self, id, type, x, y, olr, width, depth, worth):
        """
        Initializes a House
        """
        self.id = id
        self.type = type
        self.x = x
        self.y = y
        self.olr = olr
        self.width = width
        self.depth = depth
        self.worth = worth

    def __str__(self):
        return f"{self.type} at {self.x},{self.y}"