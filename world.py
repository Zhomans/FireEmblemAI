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
                self.grid[i].append(space())

    def __str__(self):
        return self.grid.__str__()

class space:
    #needs to know if there's a unit on it
    #type of terrain maybe can just be handled by inheriting? IDK
    def add_unit(unit):
        self.unit = unit
    def __str__(self):
        return "0"
    def __repr__(self):
        #apparently when you stick it in a list and print the list
        #it doesn't use __str__
        return "0"
    #writing python feels weird after doing C and Java so long.
    #where are my type declarations?!?

#simple tests to prove it's working
map = fe_map(10,10)
print map
