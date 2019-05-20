class House(object):
    """
    Representation of a house in AmstelHaege
    """

    def __init__(self, id, type, xmin, xmax, ymin, ymax, minvr, olr, width, depth, extra, base_worth, worth):
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
        self.extra = extra
        self.base_worth = base_worth
        self.worth = worth

    def update_worth(self):
        self.worth = self.base_worth * (1 + 0.01 * (self.olr * self.extra))

    def __str__(self):
        return f"{self.id}: {self.type} at {self.xmin},{self.ymin}, olr: {self.olr}"
