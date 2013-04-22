from Player import *
from unit import *
from feworld import *
from AI_ZachAttempt import *
from simpleGUI import *

#initialize everything
level = fe_map()

eliwood = unit(world = level, space = level.get_space(0,0), name = "eliwood")
hector = unit(world = level, space = level.get_space(0,1), name = "hector")
sonia = unit(world = level, space = level.get_space(5,5), name = "sonia")
limstella = unit(world = level, space = level.get_space(5,6), name = "limstella")

com = player()
human = player(com, [eliwood, hector], "human", "human")
com.initialize(human,[sonia, limstella],"com", "com")

while(len(human.units) == 2 and len(com.units) == 2):
    #run while no units have died
    display(level)
    while(len(human.movedUnits) != len(human.units)):
        human.play_turn(level)
        display(level)

    while (len(com.units) != len(com.actedUnits)):
        com.play_turn(level)
        display(level)
    #reset everything
    human.movedUnits = []
    human.actedUnits = []
    com.movedUnits = []
    com.actedUnits = []
if len(human.units) != 2:
    print "Computer wins!"
else:
    print "Human wins!"
