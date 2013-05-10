#comVcomTest.py
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

#enemy units
#in 7 there's just under twice as many enemies as your units at first
#then a bunch of reinforcements
#we aren't accounting for reinforcements....
enemy2_units = []
for i in range (8):
    hero = unit(world=level,space=level.get_space(i, 19-i),name="hero"+str(i))
    enemy2_units.append(hero)

enemy_units = []
for i in range(8):
    grunt = unit(world=level,space=level.get_space(12+i, 19-i),name="grunt"+str(i))
    enemy_units.append(grunt)

com = player()
com2 = player()
# create players
com.initialize(com2,list(enemy_units),"com", "com")
com2.initialize(com, list(enemy2_units), "com2", "com")
#start the game
play_game(root, level, com2, com, "t", "a")
