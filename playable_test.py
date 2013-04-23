from Player import *
from unit import *
from feworld import *
from AI_ZachAttempt import *
from simpleGUI import *

#initialize everything
level = fe_map()

#player units
#Looks like in 7 you get ~.03 units/space
eliwood = unit(world = level, space = level.get_space(0,0), name = "eliwood")
hector = unit(world = level, space = level.get_space(0,1), name = "hector")
lyn = unit(world = level, space = level.get_space(2,0), name = "lyn")
player_units = [eliwood, hector, lyn]

#enemy units
#in 7 there's just under twice as many enemies as your units at first
#then a bunch of reinforcements
#we aren't accounting for reinforcements....
sonia = unit(world = level, space = level.get_space(0,5), name = "sonia")
limstella = unit(world = level, space = level.get_space(1,5),attack = 7,name ="limstella")
enemy_units = [sonia, limstella]
for i in range(4):
    grunt = unit(world=level,space=level.get_space(2+i,5),name="grunt"+str(i))
    enemy_units.append(grunt)

com = player()
#note: python lists are passed by reference, so the copy is necessary
human = player(com, list(player_units), "human", "human")
com.initialize(human,list(enemy_units),"com", "com")

while(len(human.units) == len(player_units) and len(com.units) == len(enemy_units)):
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
if len(human.units) != len(player_units):
    print "Computer wins!"
else:
    print "Human wins!"
