import numpy as np


ccountries = {
    'england': ['wales', 'irish channel', 'scotland'],
    'ireland': ['irish channel'],
    'scotland': ['england'],
    'wales': ['england']
}


class cartographer():

    def __init__(self, countries):
        self.make_nodes(countries)
        self.make_coords(countries)
        self.make_map(countries)

    def make_nodes(self, countries):
        for idx, i in enumerate(countries):
            self.nodes = {i: node()}

    def make_coords(self, countries):
        for idx, i in enumerate(countries):
            self.coords = {i: idx}

    def make_map(self, countries):
        for i in countries:
            for j in countries[i]:
                self.nodes[i].connect(self.coords[j])

class node():

    def __init__(self):
        #flags
        self.is_land = False
        self.has_unit = False
        self.is_occupi = False
        self.occupying_nation = None

        self.links_to = np.ndarray(0, int)  # coords of neighbors (or just a 1D array?)

    def connect(self, coords):
        self.links_to.append(coords)
