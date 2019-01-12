class node():

    def __init__(self, name):
        #flags
        self.name = name
        self.is_land = False
        self.has_unit = False
        self.is_occupi = False
        self.occupying_nation = None

        self.links_to = []  # Identity of neighbors

    def connect(self, coords):
        self.links_to.append(coords)

