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
                self.grid[i].append(space(j,i,self))

    def __str__(self):
        rep = ""
        for line in self.grid:
            rep = rep+line.__str__()+"\n"
        return rep

    def get_space(self, x, y):
        if(y < len(self.grid) and y >= 0 and x < len(self.grid[y]) and x >= 0):
            #check that the space is in bounds
            return self.grid[x][y]
        else:
            #if not, just return None
            return None

class terrain(object):
    #Represents the terrain a space has
    #Has movement modifier(s) and an evasion modifier
    #Type of terrain is represented by a string
    def __init__ (self, terrainType):
        if (terrainType == 'dirt'):
            self.moveMod = 0
            self.evasionMod = 0
        else:
            self.moveMod = 0
            self.evasionMod = 0

class space(object):
    #needs to know if there's a unit on it
    #type of terrain maybe can just be handled by inheriting? IDK
    def __init__(self, x, y, world,terrain = terrain('dirt')):
        #spaces start with no units by default
        #is null a thing in Python? I can't remember.
        self.terrain = terrain
        self.unit = None
        self.x = x
        self.y = y
        self.world = world
    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        #apparently when you stick it in a list and print the list
        #it doesn't use __str__
        #if(self.unit == None):
        #    return "O"
        #else:
        #    return "X"
        return "(" + str(self.x) + "," + str(self.y) + ")"
    def get_coords(self):
        return (self.x, self.y)
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def add_unit(self, unit):
        #if the unit came from somewhere, delete it from there
        if unit.space != None:
            unit.space.unit = None
        self.unit = unit
        self.unit.space = self

