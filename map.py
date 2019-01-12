import numpy as np


countries = {
    'england': ['wales', 'irish channel', 'scotland'],
    'ireland': ['irish channel'],
    'scotland': ['england'],
    'wales': ['england'],
    'irish channel' : ['ireland', 'england']
}


class cartographer():

    def __init__(self, countries):
        self.nodes = []
        self.make_nodes(countries)
        
        self.coords = {}
        self.make_coords(countries)
        self.make_map(countries)
        
    def make_nodes(self, countries):
        for idx, i in enumerate(countries):
            self.nodes.append(node(i))

    def make_coords(self, countries):
        for idx, i in enumerate(countries):
            self.coords[i] = idx

    def make_map(self, countries):

        for i in countries:
            for index, n in enumerate(self.nodes):
                if n.name == i:
                    node_number = index
                
            print(self.nodes[node_number].name)
            print(countries[i])
            for j in countries[i]:
                for index, n in enumerate(self.nodes):
                    if n.name == j:
                        
                        self.nodes[node_number].connect(index)
                        
                

class node():

    def __init__(self, name):
        #flags
        self.name = name
        self.is_land = False
        self.has_unit = False
        self.is_occupi = False
        self.occupying_nation = None

        self.links_to = []  # coords of neighbors (or just a 1D array?)

    def connect(self, coords):
        self.links_to.append(coords)

c=cartographer(countries)
for n in c.nodes:
    print(n.name)
    print('links to--->')
    for i in n.links_to:
        print(c.nodes[i].name)
