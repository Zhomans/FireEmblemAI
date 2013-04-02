#Defines the general map, the generic space class, and terrain
#Jazmin Gonzalez-Rivero, Zachary Homans, Elizabeth Mahon, Brendan Ritter
#Artificial Intelligence, Olin College, Spring 13

class fe_map(object):
    """the map is just a container for spaces"""
    #why doesn't python have 2d arrays? It makes me sad.
    def __init__(self, x=10, y=10):
        self.grid = []
        for i in range(y):
            self.grid.append([])
            for j in range(x):
                #create each row
                #for now, it just makes a generic space
                #we can use specific terrain later
                self.grid[i].append(space(j,i))

    def __str__(self):
        return self.grid.__str__()

    def get_space(self, x, y):
        return self.grid[y][x]

class space(object):
    #needs to know if there's a unit on it
    #type of terrain maybe can just be handled by inheriting? IDK
    def __init__(self, x, y):
        #spaces start with no units by default
        #is null a thing in Python? I can't remember.
        self.unit = None
        self.x = x
        self.y = y
    def __str__(self):
        return self.__repr__
    def __repr__(self):
        #apparently when you stick it in a list and print the list
        #it doesn't use __str__
        if(self.unit == None):
            return "O"
        else:
            return "X"
    def get_coordinates:
        return (self.x, self.y)
    def add_unit(self, unit):
        self.unit = unit

