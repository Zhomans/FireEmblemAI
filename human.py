def human_player(human, level):
    #tell player what units can move.
    #there must be a better way
    print "Moveable units: "
    for unit in human.units:
        if unit not in human.movedUnits:
            print unit.name

    #take input from player
    command = raw_input("To move: Unit name, (x, y)\n To lookup: lookup unit name\n")
    if command[0:6] == 'lookup':
        #search for unit player looked up
        #it'll find duplicates
        #Not sure that's a good idea
        for unit in human.units:
            if unit.name == command[7:]:
                print_unit(unit)
        for enemy in human.opponent.units:
            if enemy.name == command[7:]:
                print_unit(enemy)
    for unit in human.units:
        to_move = command[0:command.find(',')]
        if unit.name == to_move:
            x = int(command[command.find('(')+1:command.find('(')+2])
            y = int(command[command.find(')')-1:command.find(')')])
            moved = human.move_Unit(unit,level,x,y)
            #if an enemy next to the unit
            #ask if you want to attack
            #this is incredibly inefficient and hackish

            if moved == 1:
                can_attack = list()
                #initialize attackable unit as none
                to_test = None
                if (y > 0):
                #check for edge case
                    to_test = level.get_space(x, y-1).unit
                if (to_test != None and to_test.player != human):
                    can_attack.append(to_test)
                    #reset to_test
                    to_test = None
                if (x < len(level.grid[1]) - 1):
                #check for edge case
                    to_test = level.get_space(x + 1, y).unit
                if (to_test != None and to_test.player != human):
                    can_attack.append(to_test)
                    #reset to_test
                    to_test = None
                if (y < (len(level.grid) - 1)):
                #check for edge case
                    to_test = level.get_space(x, y+1).unit
                if (to_test != None and to_test.player != human):
                    can_attack.append(to_test)
                    #reset to_test
                    to_test = None
                if (x > 0):
                #check for edge case
                    to_test = level.get_space(x-1, y).unit
                if (to_test != None and to_test.player != human):
                    can_attack.append(to_test)
                if (len(can_attack) > 0):
                    attack = raw_input("Type unit to attack of "+str(can_attack)+"\n")
                    if attack != "n":
                        for enemy in human.opponent.units:
                            if attack == enemy.name:
                                human.act_Unit(unit, level, enemy)
                                
def print_unit(unit):
    print "Name: " + unit.name
    print "Owner: " + unit.player.name
    print "Location: ("+str(unit.get_x())+", "+str(unit.get_y())+")"
    print "HP: " + str(unit.hp)
    print "Attack: " + str(unit.attack)
    print "Defense: " + str(unit.defense)
    print "Movement: " + str(unit.move)
    print "Unit Type: " + unit.unitType
