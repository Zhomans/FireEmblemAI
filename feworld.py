#feworld.py
#Jazmin Gonzalez-Rivero, Zachary Homans, Elizabeth Mahon, Brendan Ritter
#Artificial Intelligence, Olin College, Spring 13

#Defines the general map, the generic space class, and terrain.

class fe_map(object):
    #The map holds all of the spaces within the game.
    def __init__(self, x=10, y=10):
        #Create the map.
        self.grid = []
        self.x = x
        self.y = y
        for i in range(x):
            self.grid.append([])
            for j in range(y):
                self.grid[i].append(space(i,j,self))

    def __str__(self):
        #Represent the grid as a list of spaces.
        rep = ""
        for line in self.grid:
            rep = rep+line.__str__()+"\n"
        return rep

    def get_space(self, x, y):
        #Check if the space is in bounds. If so, return it. Else, return None.
        if(y < len(self.grid) and y >= 0 and x < len(self.grid[y]) and x >= 0):
            return self.grid[x][y]
        else:
            return None

class terrain(object):
    #Each space has a terrain.
    #Terrain affects several modifiers (defense, movement, and evasion).
    #Terrains are represented by a name string.
    def __init__ (self, terrainType):
        self.terrainType = terrainType
        if (terrainType == 'dirt'):
            self.type = terrainType
            self.moveMod = 1
            self.evasionMod = 0
            self.defenseMod = 0
        if (terrainType == 'forest'):
            self.type = terrainType
            self.moveMod = 2
            self.evasionMod = 20
            self.defenseMod = 1
        else:
            self.type = terrainType
            self.moveMod = 1
            self.evasionMod = 0
            self.defenseMod = 0

class space(object):
    #Spaces hold terrain and either one or zero units.
    def __init__(self, x, y, world,terrain = terrain('dirt')):
        #Spaces start with no unit.
        self.terrain = terrain
        self.unit = None
        self.x = x
        self.y = y
        self.world = world

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    def get_coords(self):
        #Return the coordinates of a space.
        return (self.x, self.y)
    
    def get_x(self):
        #Return the x location of a space.
        return self.x
    
    def get_y(self):
        #Return the y location of a space.
        return self.y
    
    def defense(self):
        #Return the defense modifier of a space.
        return self.terrain.defenseMod
    
    def add_unit(self, unit):
        #If there is unit on the space, move the unit to the space.
        if unit.space != None:
            unit.space.unit = None
        self.unit = unit
        self.unit.space = self

