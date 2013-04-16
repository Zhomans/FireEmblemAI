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
    def __init__(self, space = None, hp = 20, attack = 10, defense = 0, move = 5, unitType = 'infantry', name = ""):
        self.space = space
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.move = move
        self.unitType = unitType
        self.name = name
    def get_space(self):
        return self.space
    #doing unit.get_space().get_x() is driving me crazy....
    def get_x(self):
        return self.space.get_x()
    def get_y(self):
        return self.space.get_y()
    def move_unit(self, space):
        self.move_list = self.get_move_list() #This should go somewhere else.
        if space in self.move_list:
            space.add_unit(self)
            self.space = space
            self.move_list = self.get_move_list()
            print "Moved to " + str(space)
        else:
            print "Can't move there!"
            #error!!
    def attack(self, enemy):
        #I know this breaks proper getters and setters
        #we can make it better later.
        #we'll need to change it to add weapons anyway
        enemy.hp = enemy.hp - (self.attack - enemy.defense)
        if enemy.hp <= 0:
            enemy.die()

    def die(self):
        self.space.unit = None
        self.space = None
        #Add in "Unit disappears from player's unit list"

    def get_move_list(self):
        start_space = self.get_space()
        world = start_space.world
        moves_remaining = self.move
        move_list = []
        recent_moves = [start_space]
        next_moves = []

        while moves_remaining > 0:
            while recent_moves != []:
                considered_space = recent_moves.pop(0)
                for move_poss in ([0, 1], [0, -1], [1, 0], [-1, 0]):
                    space = world.get_space(considered_space.get_x()+move_poss[0], considered_space.get_y()+move_poss[1])
                    if space != None:
                        if space.unit == None:
                            if space not in move_list:
                                move_list.append(space)
                                next_moves.append(space)

            moves_remaining -= 1
            recent_moves = next_moves
            next_moves = []

        return move_list

    def get_attack_list(self):
        world = self.space.world
        move_list = self.move_list
        attack_list = []
        for space in move_list:
            in_range = []
            for move_poss in ([0, 1], [0, -1], [1, 0], [-1, 0]):
                in_range.append(world.get_space(space.get_x()+move_poss[0], space.get_y()+move_poss[1]))

            for space_in_range in in_range:
                if space_in_range != None and space_in_range not in attack_list:
                    attack_list.append(space_in_range)

        return attack_list
