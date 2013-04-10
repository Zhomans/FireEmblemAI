#units is a list of usable units the AI owns
#used_units is a list of unusable units the AI owns

tot_damage = dict()
attackers = dict()


while units != []
#while there are units that are usable
    for unit in units:
    #assuming there's also a list of enemy units
        for enemy in enemies:
            #check if enemy is in range
            xdistance = abs(unit.get_space().get_x() - enemy.get_space().get_x())
            ydistance = abs(unit.get_space().get_y() - enemy.get_space().get_y())
            if (xdistance + ydistance) <= unit.move:
                #if it's in range, note the damage you can do
                tot_damage[enemy] = tot_damage[enemy] + unit.attack
                #and remember that you can attack it
                if enemy in attackers:
                    attackers[enemy] = attackers[enemy].append(unit)
                else:
                    attackers[enemy] = list(unit)
    #loop through the dictionary of enemies that can be attacked?
    #there's gotta be a faster way.
    #Premature optimization is the death of working code
    #so let's just do the inefficient way
    #after we move all units for first enemy, do we want to recalculate?
    #so if we do so
    #we don't actually need a list
    #we only need the weakest one.

    #arbitrarily initialize weakest as the last one we looked at
    weakest = enemy

    for enemy in tot_damage.keys():
        if(tot_damage[enemy]/enemy.hp < tot_damage[weakest]/weakest.hp):
            weakest = enemy

    for unit in attackers[enemy]:
        #go attack the enemy
        #not sure how to do it
