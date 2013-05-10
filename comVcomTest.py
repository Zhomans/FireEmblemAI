#comVcomTest.py
#Jazmin Gonzalez-Rivero, Zachary Homans, Elizabeth Mahon, Brendan Ritter
#Artificial Intelligence, Olin College, Spring 13

#Test that pits the two AIs against each other

from Player import *
from unit import *
from feworld import *
import Tkinter as tk
import random
from framework import *

#initialize everything
level = fe_map(20,20)
root=tk.Tk()

#Set the bottom right corner of the map to be filled with forest
for j in range(1,12):
    for i in range(j):
        level.grid[(20-j)+i][19-i].terrain = terrain('forest')

#Randomly place forest in the rest of the map
for i in range(50):
    level.grid[int(random.randint(0,19))][int(random.randint(0,19))].terrain = terrain('forest')

#Create units
enemy2_units = []
for i in range (8):
    hero = unit(world=level,space=level.get_space(i, 19-i),name="hero"+str(i))
    enemy2_units.append(hero)

enemy_units = []
for i in range(8):
    grunt = unit(world=level,space=level.get_space(12+i, 19-i),name="grunt"+str(i))
    enemy_units.append(grunt)

#create players
com = player()
com2 = player()
com.initialize(com2,list(enemy_units),"com", "com")
com2.initialize(com, list(enemy2_units), "com2", "com")

#start the game
play_game(root, level, com2, com, "t", "a")
