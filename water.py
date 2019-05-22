class Water(object):
    """
    Representation of a water element in AmstelHaege
    """

    def __init__(self, id, xmin, xmax, ymin, ymax, width, depth):
        """
        Initializes a House
        """
        self.id = id
        self.xmax = xmax
        self.xmin = xmin
        self.ymax = ymax
        self.ymin = ymin
        self.width = width
        self.depth = depth
