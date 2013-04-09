#assuming that the player has a list of all its units called units

tot_damage = dict()

for unit in units:
    #assuming there's also a list of enemy units
    for enemy in enemies:
        #check if enemy is in range
        xdistance = abs(unit.get_space().get_coords()[1] - enemy.get_space().get_coords[1]) #this is terrible. Need to redo how you get this stuff
        ydistance = abs(unit.get_space().get_coords()[2] - enemy.get_space().get_coords[2])
        if (xdistance + ydistance) <= unit.move:
            #if it's in range, note the damage you can do
            tot_damage[enemy] = tot_damage[enemy] + unit.attack
    #dictionary that maps from enemies to damage we can do to it
    #update with each unit
    #at the end, we'll go for the one with the most, right?
    #highest percentage, not most total.
