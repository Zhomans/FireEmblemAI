#Represents a single unit
#Jazmin Gonzalez-Rivero, Zachary Homans, Elizabeth Mahon, Brendan Ritter
#Artificial Intelligence, Olin College, Spring 13

from feworld import *
import random

#A Unit is the basic moveable piece in Fire Emblem.
#They have a number of stats, an owner, and a name.
#They occupy a space. The death of a unit means defeat.

class unit:
    #Units have the following:
    #   - Their World
    #   - Their Current Space
    #   - Their Major Stats
    #   - Their Class
    #   - Their Name
    #   - Their Owner
    def __init__(self, world, space = None, hp = 20, attack = 10, defense = 0, move = 5, accuracy = .9, unitType = 'infantry', name = "", owner = None):
        self.space = space
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.move = move
        self.unitType = unitType
        self.name = name
        space.add_unit(self)
        self.player = owner
        self.accuracy = accuracy

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_space(self):
        #Returns unit's space.
        return self.space

    def get_x(self):
        #Returns x location.
        return self.space.get_x()

    def get_y(self):
        #Returns y location.
        return self.space.get_y()

    def move_unit(self, space):
        #Moves a unit to a new space, if possible.
        self.move_list = self.get_move_list()
        if space in self.move_list:
            space.add_unit(self)
            self.space = space
            self.move_list = self.get_move_list()
            print str(self.name) + " moved to " + str(space)
            return 0
        else:
            print self.name+" can't move to "+ str(space)
            return 1
    def attack_enemy(self, enemy):
        #Initiates an attack sequence.

        #If the attack hits, do the appropriate damage. Else, nothing happens.
        if random.random() < (self.accuracy-enemy.space.terrain.evasionMod):
            damage = (self.attack - (enemy.defense + enemy.space.defense()))
            enemy.hp = enemy.hp - damage
            print self.name+" hit "+enemy.name+" for "+str(damage)+" damage."
        else:
            print self.name + " missed " + enemy.name

        #Checks to see if the enemy is dead. If not, counterattack.
        if enemy.hp > 0:
        #After an attack comes a counterattack. It's the exact reverse of an attack.
            if random.random() < (enemy.accuracy-self.space.terrain.evasionMod):
                damage = (enemy.attack - (self.defense + self.space.defense()))
                self.hp = self.hp - damage
                print enemy.name+" hit "+self.name+" for "+str(damage)+" damage."

            else:
                print enemy.name + " missed " + self.name
            if self.hp <= 0:
                self.die()
        else:
            enemy.die()

    def die(self): 
        #The unit dies.
        self.space.unit = None
        self.space = None
        self.player.units.remove(self)
        print self.name + " has died."

    def get_move_list(self):
        #Returns the list of possible movements of a unit.
        #Does a basic breadth-first search.
        #Considers movement modifers, terrain, and other units.
        start_space = self.get_space()
        world = start_space.world
        moves_remaining = self.move
        move_list = [start_space]
        recent_moves = [(start_space,moves_remaining)]
        next_moves = []

        while recent_moves != []:
            considered_space = recent_moves.pop(0)
            for move_poss in ([0, 1], [0, -1], [1, 0], [-1, 0]):
                place = world.get_space(considered_space[0].get_x()+move_poss[0], considered_space[0].get_y()+move_poss[1])
                if place != None:
                    new_move = considered_space[1] - place.terrain.moveMod
                    #Units can "walk over" friendly units
                    #So don't make them a block
                    if place.unit in self.player.units or place.unit==None:
                        if place not in move_list:
                            if new_move >= 0:
                                move_list.append(place)
                                if new_move > 0:
                                    recent_moves.append((place,new_move))
        #Units cannot stand on the same spot as another unit
        #So remove any spaces that have units on them.
        for loc in move_list:
            if loc.unit != None and loc.unit != self:
                move_list.remove(loc)
        return move_list

    def get_attack_list(self):
        #Expands one more space out from the movement list
        #to determine the possible spaces a unit can attack.
        world = self.space.world
        move_list = self.get_move_list()
        attack_list = []
        for space in move_list:
            in_range = []
            for move_poss in ([0, 1], [0, -1], [1, 0], [-1, 0]):
                in_range.append(world.get_space(space.get_x()+move_poss[0], space.get_y()+move_poss[1]))

            for space_in_range in in_range:
                if space_in_range != None and space_in_range not in attack_list:
                    attack_list.append(space_in_range)

        return attack_list
