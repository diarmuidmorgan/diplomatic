class country () :

    def __init__ (self, NAME, isMilitaryBase, isNavalBase, adjacencies = []):
        self.NAME = NAME
        self.adjacent = adjacencies
        self.isMilitaryBase = isMilitaryBase
        self.isNavalBase = isNavalBase

    def add_adjacency(self, adjacency):
        self.adjacent.append(adjacency)
