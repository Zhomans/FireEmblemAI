#FinalAI.py
#Jazmin Gonzalez-Rivero, Zachary Homans, Elizabeth Mahon, Brendan Ritter
#Artificial Intelligence, Olin College, Spring 13


import math
from feworld import *

def check2(dir_attacker1,dir_attacker2,array1,array2):
    #top=1
    #bottom=2
    def check(array):
        new_dir_attacker = None
        for unit in array:
            if new_dir_attacker == None:
                new_dir_attacker = unit
            else:
                if unit[1] > new_dir_attacker[1]:
                    new_dir_attacker = unit
        return new_dir_attacker

    if dir_attacker1 == dir_attacker2 and dir_attacker1 != None and array1 != [] and array2 != []:
        new_dir_attacker1=check(array1)
        new_dir_attacker2=check(array2)
        if new_dir_attacker1[1] > new_dir_attacker2[1]:
            dir_attacker1 = new_dir_attacker1
            array1.remove(new_dir_attacker1)
        else:
            dir_attacker2 = new_dir_attacker2
            array2.remove(new_dir_attacker2)
        return False
    else:
        return True
            
def damage_checker(dir_attacker,array):
    for unit in array:
        if dir_attacker == None:
            dir_attacker = unit
        else:
            if unit[1] > dir_attacker[1]:
                dir_attacker = unit
    if array !=[]:
        array.remove(dir_attacker)
    return (dir_attacker,array)
    
def distance(unit1,unit2):
    return math.sqrt((unit1.get_x() - unit2.get_x())**2 + (unit1.get_y() - unit2.get_y())**2)
        
#calculates 'square' distance between two spaces
def space_distance(space1, space2):
    return (abs(space1.get_x() - space2.get_x()) + abs(space1.get_y() - space2.get_y()))
    
#finds the closest space in the list to the desired space
#desired is a space object, move_list is a list of space objects
def find_closest(desired, move_list):
    #init outputs
    distance = space_distance(desired,move_list[0])
    closest = move_list[0]
    for place in move_list:
        dist = space_distance(desired, place)
        if dist < distance:
            distance = dist
            closest = place
    return closest

def computer_player(com, world, strat = "t"):
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
                dist[unit][distance(enemy,unit)] = enemy

    for enemy in opponent.units:
        #enemy is of type unit
        top_space = world.get_space(enemy.get_x(), enemy.get_y()-1)
        units_that_can_attack_top = []
        bottom_space = world.get_space(enemy.get_x(), enemy.get_y()+1)
        units_that_can_attack_bottom = []
        left_space = world.get_space(enemy.get_x()-1, enemy.get_y())
        units_that_can_attack_left = []
        right_space = world.get_space(enemy.get_x()+1, enemy.get_y())
        units_that_can_attack_right = []

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


        #these next 4 for loops determine which unit can do the most damage
        #in the position that it's labelled for

        for i in range(3,-1,-1):
            if isinstance(top_space, space):
                if top_space.terrain.defenseMod == i:
                    temptop=damage_checker(top_attacker,units_that_can_attack_top)
                    top_attacker=temptop[0]
                    units_that_can_attack_top=temptop[1]
            if isinstance(bottom_space, space):
                if bottom_space.terrain.defenseMod == i:
                    tempbottom=damage_checker(bottom_attacker,units_that_can_attack_bottom)
                    bottom_attacker=tempbottom[0]
                    units_that_can_attack_bottom=tempbottom[1]
            if isinstance(left_space, space):
                if left_space.terrain.defenseMod == i:
                    templeft=damage_checker(left_attacker,units_that_can_attack_left)
                    left_attacker=templeft[0]
                    units_that_can_attack_left=templeft[1]
            if isinstance(right_space, space):
                if right_space.terrain.defenseMod == i:
                    tempright=damage_checker(right_attacker,units_that_can_attack_right)
                    right_attacker=tempright[0]
                    units_that_can_attack_right=tempright[1]
                              
        
        while final_attackers == False:
            #check whether the same unit is in two slots
            #if so, find the next best one for one of the slots
            #only loops if duplicates are found
                
            #this is final_attackers
            #the short variable name is to keep things pretty.
            b = True

            b = b and check2(top_attacker,bottom_attacker,units_that_can_attack_top,units_that_can_attack_bottom)
            b = b and check2(top_attacker,right_attacker,units_that_can_attack_top,units_that_can_attack_right)
            b = b and check2(top_attacker,left_attacker,units_that_can_attack_top,units_that_can_attack_left)

            b = b and check2(bottom_attacker,right_attacker,units_that_can_attack_bottom,units_that_can_attack_right)
            b = b and check2(bottom_attacker,left_attacker,units_that_can_attack_bottom,units_that_can_attack_left)

            b = b and check2(right_attacker,left_attacker,units_that_can_attack_right,units_that_can_attack_left)

            final_attackers = b

        ###################################################################

        attackers = [top_attacker,bottom_attacker,left_attacker,right_attacker]
        total_damage = 0.0
        for attacker in attackers:
            if attacker != None:
                total_damage += attacker[1]

        damage[enemy] = total_damage
        enemy_attack[enemy]= attackers


    optimal_target = None
    for enemy in opponent.units:
        #figure out which enemy to attack first
        if optimal_target == None:
            optimal_target = enemy
        else:
            if damage[optimal_target]/optimal_target.hp<damage[enemy]/enemy.hp:
                optimal_target = enemy

    #Only the strongest attacks before recalculation
    move_next = None
    for attacker in enemy_attack[optimal_target]:
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
        #I am making the assumption right now that the closest enemy has the most important threat zone. 
        #This is incorrect, example a pegasus knight 7 spaces away and a lord 6 spaces. pegasus is more of a threat.
        #construct a no-go zone of spaces enemies can attack
        no_go = []
        for enemy in com.opponent.units:
            for tile in enemy.get_attack_list():
                if tile not in no_go:
                     no_go.append(tile)

        #this for loop deals with all units that can't attack
        for unit in dist.keys():
            edge = find_closest(unit.get_space(),no_go)
            if space_distance(unit.get_space(),edge) == 1 or unit.get_space() in no_go:
                #in the sweet spot or inside the threat range; stay put
                com.move_Unit(unit,world, unit.get_x(),unit.get_y())
            else:
                #not on the edge of the attack range, and not inside the attack range
                #move to the edge
                #find which side of that you want to be on
                possible = list()
                desired = None
                for side in ([0,1],[0,-1],[1,0],[-1,0]):
                    poss_space = world.get_space(edge.get_x()+side[0],edge.get_y()+side[1])
                    if poss_space not in no_go and poss_space != None:
                        possible.append(poss_space)
                        if poss_space in unit.get_move_list():
                            desired = poss_space
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
        slot = enemy_attack[optimal_target].index(move_next)
        if slot == 0:
            com.move_Unit(move_next[0],world,optimal_target.get_x(), optimal_target.get_y()-1)
        elif slot == 1:
            com.move_Unit(move_next[0],world,optimal_target.get_x(), optimal_target.get_y()+1)
        elif slot == 2:
            com.move_Unit(move_next[0],world,optimal_target.get_x()-1, optimal_target.get_y())
        elif slot == 3:
            com.move_Unit(move_next[0],world,optimal_target.get_x()+1, optimal_target.get_y())
        else:
            print "What the heck?"
        com.act_Unit(move_next[0], world, optimal_target)
        if optimal_target not in com.opponent.units:
            com.movedUnits = com.units
            com.actedUnits = com.units
