#This is DEFINITELY not optimal, either in terms of speed or intelligence.
#But premature optimization is a bad idea!
#So the goal is to get it working!

#Ideally the list of attackers should have the space they'll attack from too
#So that way we can easily check which ones we could replace
#And then we don't need to figure out where to attack from
#But that's even MORE dicts!
#At this point I'm considering making a custom data type
#The AI's units need to know:
    #Who they can attack
    #How much they can attack for
    #Where they can attack from
#From this, the AI must determine which combination does the most damage
#How?
#For enemy.possible_attackers.sort_by_attack
#if enemy.attackers < 4 and unit.possible_spaces in enemy.available_spaces
#enemy.possible_attackers.add(unit)
#elif unit.damage_to(enemy) > enemy.weakest_attacker
#and enemy.weakest_attacker.space in unit.possible_spaces
#replace enemy.weakest_attacker with unit

#units is a list of usable units the AI owns
#actedUnits is a list of unusable units the AI owns

damage = dict()
attackers = dict()


while length(units) != length(actedUnits):
#while there are units that are usable
    for unit in units:
        for enemy in self.opponent.units:
            #possible spaces to attack from
            top = world.get_space(enemy.get_x(), enemy.get_y() + 1)
            right = world.get_space(enemy.get_x()+1, enemy.get_y())
            bottom = world.get_space(enemy.get_x(), enemy.get_y()-1)
            left = world.get_space(enemy.get_x()-1, enemy.get_y())
            slots = [top, right, bottom, left]

            if((for s in slots) s in unit.get_move_list()):
                #check if you can attack the enemy
                if enemy in attackers.keys():
                    #if other units can attack the enemy, check if you should
                    if(length(attackers[enemy]) < 4):
                        attackers[enemy] = attackers[enemy].append(unit)
                        damage[enemy] = damage[enemy].append(unit)
                    else:
                        #already has maximum number of units attacking it
                        #check whether it's better for this unit to attack

                        #assume order of damage list is same as
                        #order of attacker list
                        #which should be true
                        low_dmg = min(damage[enemy])
                        if((unit.attack - enemy.defense) > low_dmg):
                            #stronger than a current attacker, check spaces
                            index = damage[enemy].index(low_dmg)
                            attacker = attackers[enemy][index]
                            #check whether the intersection of attacker spaces
                            #and possible attacking slots
                            #is in the spaces for new attacker
                            #if so, replace
                            #if not, no

                            damage[enemy][index] = unit.attack - enemy.defense
                            attackers[enemy][index] = unit
                else:
                    #if no one else can attack it, remember that you can
                    attackers[enemy] = list(unit)
                    damage[enemy] = list(unit.attack - enemy.defense)

    #arbitrarily initialize weakest as the last one we looked at
    weakest = enemy

    for enemy in damage.keys():
        #attack the one that you will do the highest % damage to
        percent_e = sum(damage[enemy])/enemy.hp
        percent_w = sum(damage[weakest]/weakest.hp
        if(percent_e > percent_w):
            weakest = enemy
        elif (percent_e == percent_w):
            #attack the one with less health if % same
            if weakest.hp > enemy.hp:
                weakest = enemy

    for unit in attackers[weakest]:
        #most of the arguments are currently placeholders
        #we do need to figure out how to calculate where it needs to move
        #...after this
        move_Unit(unit, world, x, y, unit.get_x(), unit.get_y())
        act_Unit(unit, world, weakest)
