class Water(object):
    """
    Representation of a water element in AmstelHaege
    """

    def __init__(self, id, size):
        """
        Initializes a water element
        """
        self.id = id
        self.size = size

    def __str__(self):
        return f"{self.id}"