from Player import *
from unit import *
from feworld import *
from FinalAI import *
import Tkinter as tk
from PIL import ImageTk
from PIL import Image
import time
from simpleGUI import display
import random
from framework import *

#initialize everything
level = fe_map(20,20)
root=tk.Tk()

#test terrain; make (1,1) a forest
for j in range(1,12):
    for i in range(j):
        level.grid[(20-j)+i][19-i].terrain = terrain('forest')

for i in range(50):
    level.grid[int(random.randint(0,19))][int(random.randint(0,19))].terrain = terrain('forest')

#player units
#Looks like in 7 you get ~.03 units/space
eliwood = unit(world = level, space = level.get_space(0,0), name = "eliwood")
hector = unit(world = level, space = level.get_space(0,1), name = "hector", hp = 30)
lyn = unit(world = level, space = level.get_space(2,0), name = "lyn", hp = 15)
roy = unit(world = level, space = level.get_space(2,2), name = "roy", hp = 15)
erika = unit(world = level, space = level.get_space(1,1), name = "erika", hp = 18)
ephraim = unit(world = level, space = level.get_space(2,3), name = "ephraim", hp = 25)
player_units = [eliwood, hector, lyn, roy, erika, ephraim]

#enemy units
#in 7 there's just under twice as many enemies as your units at first
#then a bunch of reinforcements
#we aren't accounting for reinforcements....
enemy_units = []
for i in range(8):
    grunt = unit(world=level,space=level.get_space(12+i, 19-i),name="grunt"+str(i))
    enemy_units.append(grunt)

com = player()
#note: python lists are passed by reference, so the copy is necessary
human = player(com, list(player_units), "human", "human")
com.initialize(human,list(enemy_units),"com", "com")

play_game(root, level, human, com)
