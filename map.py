import numpy as np
import node
countries = {
    'england': ['wales', 'irish channel', 'scotland'],
    'ireland': ['irish channel'],
    'scotland': ['england', 'irish channel'],
    'wales': ['england', 'irish channel'],
    'irish channel' : ['ireland', 'england', 'scotland', 'wales']
}

## The cartographer puts the map together from the individual countries.
class cartographer():

    def __init__(self, countries):
        self.nodes = []
        self.make_nodes(countries)

        self.coords = {}
        self.make_coords(countries)
        self.make_map(countries)

    # Initialise the nodes
    def make_nodes(self, countries):
        for idx, i in enumerate(countries):
            self.nodes.append(node(i))

    # Give them a position in an array
    def make_coords(self, countries):
        for idx, i in enumerate(countries):
            self.coords[i] = idx

    # Link them all up
    def make_map(self, countries):
        for i in countries:
            for index, n in enumerate(self.nodes):
                if n.name == i:
                    node_number = index

            for j in countries[i]:
                for index, n in enumerate(self.nodes):
                    if n.name == j:
                        self.nodes[node_number].connect(index)
c=cartographer(countries)
for n in c.nodes:
    print(
        '{0} links to {1}'
        .format(n.name, ', '.join([c.nodes[i].name for i in n.links_to]))
    )
