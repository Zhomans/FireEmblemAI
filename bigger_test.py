#bigger_test.py
#Jazmin Gonzalez-Rivero, Zachary Homans, Elizabeth Mahon, Brendan Ritter
#Artificial Intelligence, Olin College, Spring 13

#Tests on a larger map to better test:
#   Group behavior
#   Terrain
#   Moving when no enemies are in range

from Player import *
from unit import *
from feworld import *
import Tkinter as tk
import random
from framework import *

#Initialize map and GUI
level = fe_map(20,20)
root=tk.Tk()

#Set the bottom right corner of the map to be filled with forest
for j in range(1,12):
    for i in range(j):
        level.grid[(20-j)+i][19-i].terrain = terrain('forest')

#Randomly place forest in the rest of the map
for i in range(50):
    level.grid[int(random.randint(0,19))][int(random.randint(0,19))].terrain = terrain('forest')

#Create player units
#Number is based on the number of units given to the player in Fire Emblem 7
eliwood = unit(world = level, space = level.get_space(0,0), name = "eliwood")
hector = unit(world = level, space = level.get_space(0,1), name="hector",hp=30)
lyn = unit(world = level, space = level.get_space(2,0), name = "lyn", hp = 15)
roy = unit(world = level, space = level.get_space(2,2), name = "roy", hp = 15)
erika = unit(world = level, space = level.get_space(1,1), name="erika",hp =18)
ephraim = unit(world = level, space=level.get_space(2,3),name="ephraim",hp=25)
player_units = [eliwood, hector, lyn, roy, erika, ephraim]

#Create enemy units
enemy_units = []
for i in range(8):
    grunt=unit(world=level,space=level.get_space(12+i,19-i),name="grunt"+str(i))
    enemy_units.append(grunt)

#make players
com = player()
#note: python lists are passed by reference, so the copy is necessary
human = player(com, list(player_units), "human", "human")
com.initialize(human,list(enemy_units),"com", "com")

#run the game code
play_game(root, level, human, com, strat2 = "t")
