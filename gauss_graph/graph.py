from gauss import GaussInteger as gi
from random import randint
from math import sin, cos, pi


class Graph(object):
    def __init__(self):
        pass


class Engine(object):
    options = [float(0)*pi, float(pi)/2, float(pi), 3*float(pi)/2]
    current_option = 0
    current_direction = []

    def __init__(self, starting_gauss, rand):
        """
        Initialization method for engine object
        :param starting_gauss: Starting gaussian integer
        :param rand: random integer between 0 and 3 corresponding to 0pi, pi/2, pi, 3pi/2
        """
        self.starting_gauss = starting_gauss
        self.current_option = rand
        self.current_direction = [cos(self.current_option), sin(self.current_option)]

    def rotate(self):
        if self.current_option == 3:
            self.current_option = 0
        else:
            self.current_option += 1
        self.current_direction = [cos(self.current_option), sin(self.current_option)]

    def move(self):
        pass

if __name__ == "__main__":
    pass
