from Player import *
from unit import *
from feworld import *
from AI_ZachAttempt import *
from simpleGUI import *

#initialize everything
level = fe_map()

eliwood = unit(space = level.get_space(0,0), name = "eliwood")
hector = unit(space = level.get_space(0,1), name = "hector")

sonia = unit(space = level.get_space(5,5), name = "sonia")
limstella = unit(space = level.get_space(5,6), name = "limstella")

com = player()
human = player(com, [eliwood, hector], "human", "human")
com.initialize(human,[sonia, limstella],"com", "com")

while(len(human.units) == 2 or len(com.units) == 2):
    #run while no units have died
    while(len(human.movedUnits) != len(human.units)):
        #tell player what units can move.
        #there must be a better way
        print "Moveable units: "
        for unit in human.units:
            if unit not in human.movedUnits:
                print unit.name

        #take input from player
        command = raw_input("Unit name, (x, y)\n")
        for unit in human.units:
            to_move = command[0:command.find(',')]
            if unit.name == to_move:
                x = int(command[command.find('(')+1:command.find('(')+2])
                y = int(command[command.find(')')-1:command.find(')')])
                human.move_Unit(unit,level,x,y)
        display(level)
    while (len(com.units) != len(com.actedUnits)):
        #this function also has a while loop
        #Not sure where it makes more sense
        computer_player(com, level)
    #reset everything
    human.movedUnits = []
    human.actedUnits = []
    com.movedUnits = []
    com.actedUnits = []
    human.status()
    com.status()
