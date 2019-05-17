class House(object):
    """
    Representation of a house in AmstelHaege
    """

    def __init__(self, id, type, xmin, xmax, ymin, ymax, minvr, olr, width, depth, worth):
        """
        Initializes a House
        """
        self.id = id
        self.type = type
        self.xmax = xmax
        self.xmin = xmin
        self.ymax = ymax
        self.ymin = ymin
        self.minvr = minvr
        self.olr = olr
        self.width = width
        self.depth = depth
        self.worth = worth

    def __str__(self):
        return f"{self.type} at {self.x},{self.y}"
