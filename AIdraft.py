consider = list()

#assuming that the player has a list of all its units called units
for unit in units:
    #assuming there's also a list of enemy units
    for enemy in enemies:
        xdistance = abs(unit.get_space().get_coords()[1] - enemy.get_space().get_coords[1]) #this is terrible. Need to redo how you get this stuff
        ydistance = abs(unit.get_space().get_coords()[2] - enemy.get_space().get_coords[2])
        if (xdistance + ydistance) <= unit.move:
            #if it's in range, consider it
            consider.append(enemy)
    weakest = consider[1]
    for enemy in consider:
        if enemy.HP < weakest.HP:
            weakest = enemy
        
