class House(object):
    """
    Representation of a house in AmstelHaege
    """

    def __init__(self, id, name, depth, height, minvr, extra_wpm, worth):
        """
        Initializes a House
        """
        self.id = id
        self.name = name
        self.depth = depth
        self.height = height
        self.minvr = minvr
        self.extra_wpm = extra_wpm
        self.worth = worth

    def __str__(self):
        return f"{self.name}"