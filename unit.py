#Represents a single unit
#Jazmin Gonzalez-Rivero, Zachary Homans, Elizabeth Mahon, Brendan Ritter
#Artificial Intelligence, Olin College, Spring 13

class unit:
    #units have:
    #   the space they're on
    #   their class
    #   their weapons
    #   their stats
    #all we need at the beginning is the space.
    #everything else will be constant.
    def __init__(self, space = (1,1)):
        self.space = space
        self.attack = 10
    def add_space(self, space):
        #units need to know what space they're on
        #need some way to make sure that units and spaces are always paired
        self.space = space
