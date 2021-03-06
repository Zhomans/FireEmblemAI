#human.py
#Jazmin Gonzalez-Rivero, Zachary Homans, Elizabeth Mahon, Brendan Ritter
#Artificial Intelligence, Olin College, Spring 13

#Handles human commands.

#Takes the player it is playing for and the map.
#Returns true if the player wants to end the game, false otherwise
def human_player(human, level):
    #Tell player what units can move.
    print "Moveable units: "
    for unit in human.units:
        if unit not in human.movedUnits:
            print unit.name + " (HP:" + str(unit.hp) + "), " + str(unit.space)

    print "\n"
    #Take input from player
    command = raw_input("To move: Unit name, (x, y)\nTo lookup: lookup unit name\nTo end turn: end\nTo quit: quit\n")
    if command == 'quit':
        return True
    elif command == 'end':
        human.movedUnits = human.units
    elif command[0:6] == 'lookup':
        #Search for unit player looked up
        for unit in human.units:
            if unit.name == command[7:]:
                print "\n"
                print_unit(unit)
                print "\n"
        for enemy in human.opponent.units:
            if enemy.name == command[7:]:
                print "\n"
                print_unit(enemy)
                print "\n"
    else:
        #search for unit player wants to move
        for unit in human.units:
            comma = command.find(',')
            to_move = command[0:comma]
            if unit.name == to_move:
                try:
                    x = int(command[command.find('(')+1:command.find(',',comma+1)])
                    y = int(command[command.find(',',comma+1)+1:command.find(')')])
                    moved = human.move_Unit(unit,level,x,y)
                except ValueError:
                    print "Invalid input, try again."
                    return False
                #if an enemy next to the unit
                #ask if you want to attack
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
                                    if enemy not in human.opponent.units:
                                        #if you killed the enemy, end the game
                                        human.movedUnits = human.units
                                        return False
    return False
                 
#Simply a neat container for unit display               
def print_unit(unit):
    print "Name: " + unit.name
    print "Owner: " + unit.player.name
    print "Location: ("+str(unit.get_x())+", "+str(unit.get_y())+")"
    print "Current Terrain: " + unit.space.terrain.type
    print "HP: " + str(unit.hp)
    print "Attack: " + str(unit.attack)
    print "Defense: " + str(unit.defense)
    print "Movement: " + str(unit.move)
    print "Unit Type: " + unit.unitType
