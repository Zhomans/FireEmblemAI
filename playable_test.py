#playable_test.py
#Jazmin Gonzalez-Rivero, Zachary Homans, Elizabeth Mahon, Brendan Ritter
#Artificial Intelligence, Olin College, Spring 13


from Player import *
from unit import *
from feworld import *
from FinalAI import *
import Tkinter as tk
from PIL import ImageTk
from PIL import Image
import time
from simpleGUI import display
from framework import *

#initialize everything
level = fe_map()
root=tk.Tk()

#test terrain; make (1,1) a forest
level.grid[1][1].terrain = terrain('forest')

#player units
#Looks like in 7 you get ~.03 units/space
eliwood = unit(world = level, space = level.get_space(0,0), name = "eliwood")
hector = unit(world=level,space=level.get_space(1,0), name = "hector", move=3)
lyn = unit(world=level,space=level.get_space(2,0),name ="lyn", hp = 15, move=6)
player_units = [eliwood, hector, lyn]

#enemy units
#in 7 there's just under twice as many enemies as your units at first
#then a bunch of reinforcements
#we aren't accounting for reinforcements....
sonia = unit(world = level, space = level.get_space(0,8), name = "sonia")
limstella = unit(world = level, space = level.get_space(1,8),attack = 7,name ="limstella")
enemy_units = [sonia, limstella]
for i in range(1):
    grunt = unit(world=level,space=level.get_space(2+i,8),name="grunt"+str(i))
    enemy_units.append(grunt)

com = player()
#note: python lists are passed by reference, so the copy is necessary
human = player(com, list(player_units), "human", "human")
com.initialize(human,list(enemy_units),"com", "com")

play_game(root, level, human, com, strat2 = "t")
