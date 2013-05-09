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
        final_attackers = False

        new_dir_attacker1=check(array1)
        new_dir_attacker2=check(array2)

        if new_dir_attacker1[1] > new_dir_attacker2[1]:
            dir_attacker1 = new_dir_attacker1
            array1.remove(new_dir_attacker1)
        else:
            dir_attacker2 = new_dir_attacker2
            array2.remove(new_dir_attacker2)
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
def computer_player(com, world):
        damage = dict()
        enemies = dict()
        enemy_attack = dict()
        opponent = com.opponent

        for enemy in opponent.units:
            enemies[enemy] = []
            enemy_attack[enemy] = []

        available_units = list()
        for unit in com.units:
            if unit not in com.actedUnits:
                available_units.append(unit)
        print available_units

        for unit in available_units:
            #unit is of type unit
            unit.move_list = unit.get_move_list()
            unit.attack_list = unit.get_attack_list()

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
                    enemies[enemy].append([unit, unit.attack - enemy.defense, surrounding_spaces])

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


            #these next four for loops determine which unit can do the most damage
            #in the position that it's labelled for

            temptop=damage_checker(top_attacker,units_that_can_attack_top)
            top_attacker=temptop[0]
            units_that_can_attack_top=temptop[1]

            tempbottom=damage_checker(bottom_attacker,units_that_can_attack_bottom)
            bottom_attacker=tempbottom[0]
            units_that_can_attack_bottom=tempbottom[1]

            tempright=damage_checker(right_attacker,units_that_can_attack_right)
            right_attacker=tempright[0]
            units_that_can_attack_right=tempright[1]

            templeft=damage_checker(left_attacker,units_that_can_attack_left)
            left_attacker=templeft[0]
            units_that_can_attack_left=templeft[1]
            
        
            while final_attackers == False:
                #check whether the same unit is in two slots
                #if so, find the next best one for one of the slots
                #only loops if duplicates are found
                final_attackers = True

                check2(top_attacker,bottom_attacker,units_that_can_attack_top,units_that_can_attack_bottom)
                check2(top_attacker,right_attacker,units_that_can_attack_top,units_that_can_attack_right)
                check2(top_attacker,left_attacker,units_that_can_attack_top,units_that_can_attack_left)

                check2(bottom_attacker,right_attacker,units_that_can_attack_bottom,units_that_can_attack_right)
                check2(bottom_attacker,left_attacker,units_that_can_attack_bottom,units_that_can_attack_left)

                check2(right_attacker,left_attacker,units_that_can_attack_right,units_that_can_attack_left)

            ###############################################################################################

            attackers = [top_attacker, bottom_attacker, left_attacker, right_attacker]
            total_damage = 0
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
                if damage[optimal_target]/optimal_target.hp < damage[enemy]/enemy.hp:
                    optimal_target = enemy

        #Change so only the strongest attacks before recalculation.
        #4-12: I think I got it, so I commented out the first draft. My attempt is below.
        #Let me know if it looks right, Zach. -Elizabeth

        #enemy_attack[optimal_target][0].move_unit(world.get_space(enemy.space.get_x(), enemy.space.get_y()-1))
        #enemy_attack[optimal_target][0].attack(optimal_target)
        #enemy_attack[optimal_target][1].move_unit(world.get_space(enemy.space.get_x(), enemy.space.get_y()+1))
        #enemy_attack[optimal_target][1].attack(optimal_target)
        #enemy_attack[optimal_target][2].move_unit(world.get_space(enemy.space.get_x()-1, enemy.space.get_y()))
        #enemy_attack[optimal_target][2].attack(optimal_target)
        #enemy_attack[optimal_target][3].move_unit(world.get_space(enemy.space.get_x()+1, enemy.space.get_y()))
        #enemy_attack[optimal_target][3].attack(optimal_target)

        move_next = None
        for attacker in enemy_attack[optimal_target]:
            if (move_next == None and attacker != None):
                move_next = attacker
            if (attacker != None and attacker[0].attack > move_next[0].attack):
                move_next = attacker

        #figure out which slot the next unit to move was in then move it there
        slot = enemy_attack[optimal_target].index(move_next)
        if move_next == None:
            #no one can attack, so just finish the turn
            com.movedUnits = com.units
            com.actedUnits = com.units
        else:
            if slot == 0:
                com.move_Unit(move_next[0],world,enemy.get_x(), enemy.get_y()-1)
            elif slot == 1:
                com.move_Unit(move_next[0],world,enemy.get_x(), enemy.get_y()+1)
            elif slot == 2:
                com.move_Unit(move_next[0],world,enemy.get_x()-1, enemy.get_y())
            elif slot == 3:
                com.move_Unit(move_next[0],world,enemy.get_x()+1, enemy.get_y())
            else:
                print "What the heck?"
            com.act_Unit(move_next[0], world, optimal_target)
        print optimal_target.space
    
