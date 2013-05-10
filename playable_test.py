#playable_test.py
#Jazmin Gonzalez-Rivero, Zachary Homans, Elizabeth Mahon, Brendan Ritter
#Artificial Intelligence, Olin College, Spring 13

#Small test to quickly test changes

from Player import *
from unit import *
from feworld import *
import Tkinter as tk
from framework import *

#Initialize map and GUI
level = fe_map()
root=tk.Tk()

#Test terrain; make (1,1) a forest
level.grid[1][1].terrain = terrain('forest')

#Create player units
#Number is based on the number of units given to the player in Fire Emblem 7
eliwood = unit(world = level, space = level.get_space(0,0), name = "eliwood")
hector = unit(world=level,space=level.get_space(1,0), name = "hector", move=3)
lyn = unit(world=level,space=level.get_space(2,0),name ="lyn", hp = 15, move=6)
player_units = [eliwood, hector, lyn]

#Create enemy units
sonia = unit(world = level, space = level.get_space(0,8), name = "sonia")
erik = unit(world = level, space = level.get_space(1,8),attack = 7,name="erik")
enemy_units = [sonia, limstella]
for i in range(1):
    grunt = unit(world=level,space=level.get_space(2+i,8),name="grunt"+str(i))
    enemy_units.append(grunt)

#Create players
com = player()
#note: python lists are passed by reference, so the copy is necessary
human = player(com, list(player_units), "human", "human")
com.initialize(human,list(enemy_units),"com", "com")

#Start the game
play_game(root, level, human, com, strat2 = "t")
