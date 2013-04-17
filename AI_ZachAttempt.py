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
            for unit in units_that_can_attack_top:
                #unit is a list of a unit, an int (damage), and a list of spaces
                if top_attacker == None:
                    top_attacker = unit
                else:
                    if unit[1] > top_attacker[1]:
                        top_attacker = unit
            if units_that_can_attack_top != []:
                units_that_can_attack_top.remove(top_attacker)


            for unit in units_that_can_attack_bottom:
                if bottom_attacker == None:
                    bottom_attacker = unit
                else:
                    if unit[1] > bottom_attacker[1]:
                        bottom_attacker = unit
            if units_that_can_attack_bottom !=[]:
                units_that_can_attack_bottom.remove(bottom_attacker)


            for unit in units_that_can_attack_right:
                if right_attacker == None:
                    right_attacker = unit
                else:
                    if unit[1] > right_attacker[1]:
                        right_attacker = unit
            if units_that_can_attack_right != []:
                units_that_can_attack_right.remove(right_attacker)


            for unit in units_that_can_attack_left:
                if left_attacker == None:
                    left_attacker = unit
                else:
                    if unit[1] > left_attacker[1]:
                        left_attacker = unit
            if units_that_can_attack_left != []:
                units_that_can_attack_left.remove(left_attacker)

        
            while final_attackers == False:
                #check whether the same unit is in two slots
                #if so, find the next best one for one of the slots
                #only loops if duplicates are found
                final_attackers = True

                if top_attacker == bottom_attacker and top_attacker != None and units_that_can_attack_top != [] and units_that_can_attack_bottom != []:
                    final_attackers = False

                    new_top_attacker = None
                    for unit in units_that_can_attack_top:
                        #unit is a list of a unit, an int (damage), and a list of spaces
                        if new_top_attacker == None:
                            new_top_attacker = unit
                        else:
                            if unit[1] > new_top_attacker[1]:
                                new_top_attacker = unit
                
                    new_bottom_attacker = None
                    for unit in units_that_can_attack_bottom:
                        if new_bottom_attacker == None:
                            new_bottom_attacker = unit
                        else:
                            if unit[1] > new_bottom_attacker[1]:
                                new_bottom_attacker = unit

                    if new_top_attacker[1] > new_bottom_attacker[1]:
                        top_attacker = new_top_attacker
                        units_that_can_attack_top.remove(new_top_attacker)
                    else:
                        bottom_attacker = new_bottom_attacker
                        units_that_can_attack_bottom.remove(new_bottom_attacker)

            ###############################################################################################

                if top_attacker == right_attacker and top_attacker != None and units_that_can_attack_top != [] and units_that_can_attack_right != []:
                    final_attackers = False

                    new_top_attacker = None
                    for unit in units_that_can_attack_top:
                        if new_top_attacker == None:
                            new_top_attacker = unit
                        else:
                            if unit[1] > new_top_attacker[1]:
                                new_top_attacker = unit
                
                    new_right_attacker = None
                    for unit in units_that_can_attack_right:
                        if new_right_attacker == None:
                            new_right_attacker = unit
                        else:
                            if unit[1] > new_right_attacker[1]:
                                new_right_attacker = unit

                    if new_top_attacker[1] > new_right_attacker[1]:
                        top_attacker = new_top_attacker
                        units_that_can_attack_top.remove(new_top_attacker)
                    else:
                        right_attacker = new_right_attacker
                        units_that_can_attack_right.remove(new_right_attacker)

            ###############################################################################################

                if top_attacker == left_attacker and top_attacker != None and units_that_can_attack_top != [] and units_that_can_attack_left != []:
                    final_attackers = False

                    new_top_attacker = None
                    for unit in units_that_can_attack_top:
                        if new_top_attacker == None:
                            new_top_attacker = unit
                        else:
                            if unit[1] > new_top_attacker[1]:
                                new_top_attacker = unit
                
                    new_left_attacker = None
                    for unit in units_that_can_attack_left:
                        if new_left_attacker == None:
                            new_left_attacker = unit
                        else:
                            if unit[1] > new_left_attacker[1]:
                                new_left_attacker = unit

                    if new_top_attacker[1] > new_left_attacker[1]:
                        top_attacker = new_top_attacker
                        units_that_can_attack_top.remove(new_top_attacker)
                    else:
                        left_attacker = new_left_attacker
                        units_that_can_attack_left.remove(new_left_attacker)

            ###############################################################################################

                if bottom_attacker == right_attacker and bottom_attacker != None and units_that_can_attack_bottom != [] and units_that_can_attack_right != []:
                    final_attackers = False

                    new_bottom_attacker = None
                    for unit in units_that_can_attack_bottom:
                        if new_bottom_attacker == None:
                            new_bottom_attacker = unit
                        else:
                            if unit[1] > new_bottom_attacker[1]:
                                new_bottom_attacker = unit
                
                    new_right_attacker = None
                    for unit in units_that_can_attack_right:
                        if new_right_attacker == None:
                            new_right_attacker = unit
                        else:
                            if unit[1] > new_right_attacker[1]:
                                new_right_attacker = unit

                    if new_bottom_attacker[1] > new_right_attacker[1]:
                        bottom_attacker = new_bottom_attacker
                        units_that_can_attack_bottom.remove(new_bottom_attacker)
                    else:
                        right_attacker = new_right_attacker
                        units_that_can_attack_right.remove(new_right_attacker)

            ###############################################################################################

                if bottom_attacker == left_attacker and bottom_attacker != None and units_that_can_attack_bottom != [] and units_that_can_attack_left != []:
                    final_attackers = False

                    new_bottom_attacker = None
                    for unit in units_that_can_attack_bottom:
                        if new_bottom_attacker == None:
                            new_bottom_attacker = unit
                        else:
                            if unit[1] > new_bottom_attacker[1]:
                                new_bottom_attacker = unit
                
                    new_left_attacker = None
                    for unit in units_that_can_attack_left:
                        if new_left_attacker == None:
                            new_left_attacker = unit
                        else:
                            if unit[1] > new_left_attacker[1]:
                                new_left_attacker = unit

                    if new_bottom_attacker[1] > new_left_attacker[1]:
                        bottom_attacker = new_bottom_attacker
                        units_that_can_attack_bottom.remove(new_bottom_attacker)
                    else:
                        left_attacker = new_left_attacker
                        units_that_can_attack_left.remove(new_left_attacker)

            ###############################################################################################

                if right_attacker == left_attacker and right_attacker != None and units_that_can_attack_right != [] and units_that_can_attack_left != []:
                    final_attackers = False

                    new_right_attacker = None
                    for unit in units_that_can_attack_right:
                        if new_right_attacker == None:
                            new_right_attacker = unit
                        else:
                            if unit[1] > new_right_attacker[1]:
                                new_right_attacker = unit
                
                    new_left_attacker = None
                    for unit in units_that_can_attack_left:
                        if new_left_attacker == None:
                            new_left_attacker = unit
                        else:
                            if unit[1] > new_left_attacker[1]:
                                new_left_attacker = unit

                    if new_right_attacker[1] > new_left_attacker[1]:
                        right_attacker = new_right_attacker
                        units_that_can_attack_right.remove(new_right_attacker)
                    else:
                        left_attacker = new_left_attacker
                        units_that_can_attack_left.remove(new_left_attacker)

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
    
