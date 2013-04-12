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
    def __init__(self, space = None, hp = 20, attack = 10, defense = 0, move = 5, unitType = 'infantry'):
        self.space = space
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.move = move
        self.unitType = unitType
    def get_space(self):
        return self.space
    #doing unit.get_space().get_x() is driving me crazy....
    def get_x(self):
        return self.space.get_x()
    def get_y(self):
        return self.space.get_y()
    def move(self, space):
        deltax = abs(self.space.get_x() - space.get_x())
        deltay = abs(self.space.get_y() - space.get_y())
        if (deltax + deltay) <= self.space:
            self.space.add_unit(None)
            space.add_unit(self)
            self.space = space
        else:
            pass
            #error!!
    def attack(self, enemy):
        #I know this breaks proper getters and setters
        #we can make it better later.
        #we'll need to change it to add weapons anyway
        enemy.hp = enemy.hp - (self.attack - enemy.defense)

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
                top_space = world.get_space(considered_space.get_x(), considered_space.get_y()-1)
                if top_space != None:
                    if top_space.unit != None:
                        if top_space not in move_list:
                            move_list.append(top_space)
                            next_moves.append(top_space)

                right_space = world.get_space(considered_space.get_x()+1, considered_space.get_y())
                if right_space != None:
                    if right_space.unit != None:
                        if right_space not in move_list:
                            move_list.append(right_space)
                            next_moves.append(right_space)

                left_space = world.get_space(considered_space.get_x()-1, considered_space.get_y())
                if left_space != None:
                    if left_space.unit != None:
                        if left_space not in move_list:
                            move_list.append(left_space)
                            next_moves.append(left_space)

                bottom_space = world.get_space(considered_space.get_x(), considered_space.get_y()+1)
                if bottom_space != None:
                    if bottom_space.unit != None:
                        if bottom_space not in move_list:
                            move_list.append(bottom_space)
                            next_moves.append(bottom_space)

            moves_remaining -= 1
            recent_moves = next_moves
            next_moves = []

        return move_list