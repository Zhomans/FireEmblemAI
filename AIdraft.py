#This is DEFINITELY not optimal, either in terms of speed or intelligence.
#But premature optimization is a bad idea!
#So the goal is to get it working!

#units is a list of usable units the AI owns
#actedUnits is a list of unusable units the AI owns

damage = dict()
attackers = dict()


while length(units) != length(actedUnits):
#while there are units that are usable
    for unit in units:
        for enemy in self.opponent.units:
            #check if enemy is in range
            xdistance = abs(unit.get_space().get_x() - enemy.get_space().get_x())
            ydistance = abs(unit.get_space().get_y() - enemy.get_space().get_y())
            if (xdistance + ydistance) <= unit.move:
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
                            #stronger than a current attacker, replace it
                            index = damage[enemy].index(low_dmg)
                            damage[enemy][index] = unit.attack - enemy.defense
                            attackers[enemy][index] = unit
                else:
                    #if no one else can attack it, remember that you can
                    attackers[enemy] = list(unit)
                    damage[enemy] = list(unit.attack - enemy.defense)

    #arbitrarily initialize weakest as the last one we looked at
    weakest = enemy

    for enemy in damage.keys():
        if(sum(damage[enemy])/enemy.hp < sum(damage[weakest])/weakest.hp):
            weakest = enemy
        elif (sum(damage[enemy])/enemy.hp == sum(damage[weakest])/weakest.hp):
            #attack the one with less health if % same
            if weakest.hp > enemy.hp:
                weakest = enemy

    for unit in attackers[enemy]:
        #most of the arguments are currently placeholders
        #we do need to figure out how to calculate where it needs to move
        #...after this
        move_Unit(unit, world, x, y, unit.get_space.get_x(), unit.get_space.get_y())
        act_Unit(unit, world, enemy)
