#FinalAI.py
#Jazmin Gonzalez-Rivero, Zachary Homans, Elizabeth Mahon, Brendan Ritter
#Artificial Intelligence, Olin College, Spring 13

#This is what determines how the enemy AI works.

import math
from feworld import *

#checks whether the units attacking each side are different or not
#takes two lists that contain a unit, an int (damage), and a list of spaces
#as well as two arrays of those lists
#returns whether it found different attackers
def check_diff(dir_attacker1,dir_attacker2,array1,array2):
    #takes an array of the lists
    #returns the one that has the unit that does the most damage
    def maxdamage(array):
        new_dir_attacker = None
        for unit in array:
            if new_dir_attacker == None:
                new_dir_attacker = unit
            else:
                if unit[1] > new_dir_attacker[1]:
                    new_dir_attacker = unit
        return new_dir_attacker

    if dir_attacker1 == dir_attacker2 and dir_attacker1 != None and array1 != [] and array2 != []:
        new_dir_attacker1=maxdamage(array1)
        new_dir_attacker2=maxdamage(array2)
        if new_dir_attacker1[1] > new_dir_attacker2[1]:
            dir_attacker1 = new_dir_attacker1
            array1.remove(new_dir_attacker1)
        else:
            dir_attacker2 = new_dir_attacker2
            array2.remove(new_dir_attacker2)
        return False
    else:
        return True

#finds the unit that can do the most damage from a list of units
#takes in an array of lists that contain:
#    a unit, an int (damage), and a list of spaces
#returns a tuple that contains:
#    the list from the array that contains the unit that can do the most damage
#    the array that came in minus the other element of the tuple
def max_damage(dir_attacker,array):
    for unit in array:
        if dir_attacker == None:
            dir_attacker = unit
        else:
            if unit[1] > dir_attacker[1]:
                dir_attacker = unit
    if array !=[]:
        array.remove(dir_attacker)
    return (dir_attacker,array)
        
#calculates Manhattan distance between two spaces
def distance(space1, space2):
    return (abs(space1.get_x() - space2.get_x()) + abs(space1.get_y() - space2.get_y()))
    
#finds the closest space in the list to the desired space
#desired is a space object, move_list is a list of space objects
def find_closest(desired, move_list):
    #init outputs
    dist = distance(desired,move_list[0])
    closest = move_list[0]
    for place in move_list:
        new_dist = distance(desired, place)
        if new_dist < dist:
            dist = new_dist
            closest = place
    return closest

#the actual full code that executes
#takes the player it is playing for
#the level map, and what strategy it should use
def computer_player(com, world, strat = "t"):
    #initialize all the data structures we need
    damage = dict()
    enemies = dict()
    enemy_attack = dict()
    dist = dict()
    opponent = com.opponent

    for enemy in opponent.units:
        enemies[enemy] = []
        enemy_attack[enemy] = []

    #figure out which units can attack
    available_units = list()
    for unit in com.units:
        if unit not in com.actedUnits:
            available_units.append(unit)

    #determine which units can attack which opponent units
    for unit in available_units:
        #unit is of type unit
        unit.move_list = unit.get_move_list()
        unit.attack_list = unit.get_attack_list()
        dist[unit] = dict()

        for enemy in opponent.units:
            #enemy is of type unit
            if enemy.space in unit.attack_list:
                surrounding_spaces = []
                for move_poss in ([0, 1], [0, -1], [1, 0], [-1, 0]):
                    surrounding_space=world.get_space(enemy.get_x()+move_poss[0], enemy.get_y()+move_poss[1])
                    if surrounding_space in unit.move_list:
                        #check which spaces the unit can attack the enemy from
                        surrounding_spaces.append(surrounding_space)

                #for every enemy, remember which units can attack it
                #how much they can do, and where they can attack from
                enemies[enemy].append([unit, (unit.attack - enemy.defense - enemy.space.terrain.defenseMod) * (unit.accuracy - enemy.space.terrain.evasionMod), surrounding_spaces])
                #Attack * Hit % can be changed to a better scaler
            else:
            #not in range; remember distance
                dist[unit][distance(enemy.get_space(),unit.get_space())] = enemy

    #now that we know who can attack who
    #figure out the best combination of attackers
    for enemy in opponent.units:
        #enemy is of type unit
        #initialize spaces to attack from and who can attack from each
        top_space = world.get_space(enemy.get_x(), enemy.get_y()-1)
        units_that_can_attack_top = []
        bottom_space = world.get_space(enemy.get_x(), enemy.get_y()+1)
        units_that_can_attack_bottom = []
        left_space = world.get_space(enemy.get_x()-1, enemy.get_y())
        units_that_can_attack_left = []
        right_space = world.get_space(enemy.get_x()+1, enemy.get_y())
        units_that_can_attack_right = []

        #go through each potential attacker for each enemy
        for unit in enemies[enemy]:
            #unit is a list of a unit, an int (damage), and a list of spaces
            #get lists of who can attack from each space
            if top_space in unit[2]:
                units_that_can_attack_top.append(unit)
            if bottom_space in unit[2]:
                units_that_can_attack_bottom.append(unit)
            if left_space in unit[2]:
                units_that_can_attack_left.append(unit)
            if right_space in unit[2]:
                units_that_can_attack_right.append(unit)
            
        final_attackers = False
        top_attacker = None
        bottom_attacker = None
        right_attacker = None
        left_attacker = None

        #determine which unit can do the most damage in each position
        #the outer ifs are to prevent errors from being on the edge of the map
        #the loop prioritizes moving to better terrain
        for i in range(3,-1,-1):
            if isinstance(top_space, space):
                if top_space.terrain.defenseMod == i:
                    temptop=max_damage(top_attacker,units_that_can_attack_top)
                    top_attacker=temptop[0]
                    units_that_can_attack_top=temptop[1]
            if isinstance(bottom_space, space):
                if bottom_space.terrain.defenseMod == i:
                    tempbottom=max_damage(bottom_attacker,units_that_can_attack_bottom)
                    bottom_attacker=tempbottom[0]
                    units_that_can_attack_bottom=tempbottom[1]
            if isinstance(left_space, space):
                if left_space.terrain.defenseMod == i:
                    templeft=max_damage(left_attacker,units_that_can_attack_left)
                    left_attacker=templeft[0]
                    units_that_can_attack_left=templeft[1]
            if isinstance(right_space, space):
                if right_space.terrain.defenseMod == i:
                    tempright=max_damage(right_attacker,units_that_can_attack_right)
                    right_attacker=tempright[0]
                    units_that_can_attack_right=tempright[1]
                              
        
        while final_attackers == False:
            #check whether the same unit is in two slots
            #if so, find the next best one for one of the slots
            #only loops if duplicates are found
                
            #this is final_attackers
            #the short variable name is to keep things pretty.
            b = True

            b = b and check_diff(top_attacker,bottom_attacker,units_that_can_attack_top,units_that_can_attack_bottom)
            b = b and check_diff(top_attacker,right_attacker,units_that_can_attack_top,units_that_can_attack_right)
            b = b and check_diff(top_attacker,left_attacker,units_that_can_attack_top,units_that_can_attack_left)

            b = b and check_diff(bottom_attacker,right_attacker,units_that_can_attack_bottom,units_that_can_attack_right)
            b = b and check_diff(bottom_attacker,left_attacker,units_that_can_attack_bottom,units_that_can_attack_left)

            b = b and check_diff(right_attacker,left_attacker,units_that_can_attack_right,units_that_can_attack_left)

            final_attackers = b

        #we've finally figured out the best configurations for each enemy
        attackers=[top_attacker,bottom_attacker,left_attacker,right_attacker]
        total_damage = 0.0
        #calculate how much damage we can do to each enemy
        for attacker in attackers:
            if attacker != None:
                total_damage += attacker[1]

        damage[enemy] = total_damage
        enemy_attack[enemy]= attackers

    optimal = None
    for enemy in opponent.units:
        #figure out which enemy to attack first
        if optimal == None:
            optimal = enemy
        else:
            if damage[optimal]/optimal.hp<damage[enemy]/enemy.hp:
                optimal = enemy

    #Only the strongest attacks before recalculation
    move_next = None
    for attacker in enemy_attack[optimal]:
        if (move_next == None and attacker != None):
            move_next = attacker
        if (attacker != None and attacker[0].attack > move_next[0].attack):
            move_next = attacker

    #deal with what happens if no one can attack
    if move_next == None and strat == "d":
        #defensive strategy: just stay in place
        com.movedUnits = com.units
        com.actedUnits = com.units
    elif move_next==None and strat == "t":
        #tricky strategy: move just out of range of player units
        
        #construct a no-go zone of spaces enemies can attack
        no_go = []
        for enemy in com.opponent.units:
            for tile in enemy.get_attack_list():
                if tile not in no_go:
                     no_go.append(tile)

        #this for loop deals with all units that can't attack
        for unit in dist.keys():
            #find closest space where you could be attacked
            edge = find_closest(unit.get_space(),no_go)
            if distance(unit.get_space(),edge)==1 or unit.get_space() in no_go:
                #in the sweet spot or inside the threat range; stay put
                com.move_Unit(unit,world, unit.get_x(),unit.get_y())
            else:
                #not on the edge of the attack range
                #not inside the attack range
                #move to the edge
                possible = list()
                desired = None
                #find which side of edge space you want to be on
                for side in ([0,1],[0,-1],[1,0],[-1,0]):
                    poss_space = world.get_space(edge.get_x()+side[0],edge.get_y()+side[1])
                    if poss_space not in no_go and poss_space != None:
                        possible.append(poss_space)
                        if poss_space in unit.get_move_list():
                            #if we can just go there, do that
                            desired = poss_space
                #if can't go straight there, get as close as possible
                if desired == None:
                    desired = find_closest(unit.get_space(),possible)
                final = find_closest(desired, unit.get_move_list())
                com.move_Unit(unit,world,final.get_x(),final.get_y())
        com.actedUnits = com.units
        com.movedUnits = com.units
    elif move_next == None:
        #agressive strategy: chaaarge!
        #this is the default strategy
        for unit in dist.keys():
            dists = dist[unit].keys()[:]
            dists.sort()
            min_dist = dists[0]
            closest = find_closest(dist[unit][min_dist],unit.get_move_list())
            com.move_Unit(unit,world,closest.get_x(),closest.get_y())
        com.actedUnits = com.units
        com.movedUnits = com.units
                                
    else:
        #can attack, so do it!
        #figure out which slot the next unit to move was in then move it there
        slot = enemy_attack[optimal].index(move_next)
        toMove = move_next[0]
        if slot == 0:
            com.move_Unit(toMove,world,optimal.get_x(),optimal.get_y()-1)
        elif slot == 1:
            com.move_Unit(toMove,world,optimal.get_x(),optimal.get_y()+1)
        elif slot == 2:
            com.move_Unit(toMove,world,optimal.get_x()-1,optimal.get_y())
        elif slot == 3:
            com.move_Unit(toMove,world,optimal.get_x()+1,optimal.get_y())
        else:
            print "Shouldn't get here."
        com.act_Unit(toMove, world, optimal)
