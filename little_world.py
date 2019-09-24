import numpy as np


class Country:
    def __init__(self, name=None):
        self.name = name if name is not None else str(np.random.randint(0, 50000))
        self.connection_count = 0
        self.connection_list = []
        self.citizens = 0

    def __add__(self, other):
        my_class = self.__class__
        other_class = other.__class__
        if my_class == other_class:
            self.add_countries(other)
        else:
            self.add_walker_and_country(other)

    def add_countries(self, other):
        if other not in self.connection_list:
            self.connection_count += 1
            self.connection_list.append(other)
            other.connection_count += 1
            other.connection_list.append(self)
        else:
            print("connection already exists!")

    def add_walker_and_country(self, other):
        if self not in other.home:
            self.citizens += 1
            try:
                other.home.pop()
            except:
                pass
            other.home.append(self)
        else:
            print("already home yall")

    def __sub__(self, other):
        my_class = self.__class__
        other_class = other.__class__
        if my_class == other_class:
            self.sub_countries(other)
        else:
            self.sub_walker_and_country(other)

    def sub_countries(self, other):
        if other in self.connection_list:
            self.connection_count -= 1
            self.connection_list.remove(other)
            other.connection_count -= 1
            other.connection_list.remove(self)
        else:
            print("no connection to break!")

    def sub_walker_and_country(self, other):
        if self in other.home:
            self.citizens -= 1
            other.home.pop()
            other.home.append(self)
        else:
            print("but i dont even live there")

class Walker:
    def __init__(self, name=None):
        self.name = name if name is not None else str(np.random.randint(0, 50000))
        self.love = 0
        self.lovers = []
        self.home = []

    def __add__(self, other):
        my_class = self.__class__
        other_class = other.__class__
        if my_class == other_class:
            self.add_walkers(other)
        else:
            self.add_walker_and_country(other)

    def add_walkers(self, other):
        if other not in self.lovers:
            self.love += 1
            self.lovers.append(other)
            other.love += 1
            other.lovers.append(self)
        else:
            print("way ahead of ja baby")

    def add_walker_and_country(self, other):
        if other not in self.home:
            try:
                self.home.pop()
            except:
                pass
            self.home.append(other)
            other.citizens += 1
        else:
            print("already home yall")

    def __sub__(self, other):
        my_class = self.__class__
        other_class = other.__class__
        if my_class == other_class:
            self.sub_walkers(other)
        else:
            self.sub_walker_and_country(other)

    def sub_walkers(self, other):
        if other in self.lovers:
            self.love -= 1
            self.lovers.remove(other)
            other.love -= 1
            other.lovers.remove(self)
        else:
            print("i dont even know them tho")

    def sub_walker_and_country(self, other):
        if other in self.home:
            self.home.pop()
            self.home.append(other)
            other.citizens += 1
        else:
            print("but i dont live there")

    def step(self):
        if len(self.home):
            current_location = self.home.pop()
            self.home.append(self.choose_destination(current_location))
        else:
            print("I have no home to move from!")

    def choose_destination(self, location):
        if len(location.connection_list):
            choice = np.random.randint(0, len(location.connection_list))
            return location.connection_list.pop(choice)
        else:
            print("there is nowhere else to move to!")
            return location

