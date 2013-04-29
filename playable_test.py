from Player import *
from unit import *
from feworld import *
from AI_ZachAttempt import *
import Tkinter as tk
from PIL import ImageTk
from PIL import Image
import time

def _delete_window():
    try:
        print "Prof Oak: You can't run from a trainer battle!"
        #root.destroy()
    except:
        pass
def _destroy(event):
    pass




#initialize everything
level = fe_map()
root=tk.Tk()

#test terrain; make (1,1) a forest
level.grid[1][1].terrain = terrain('forest')

root.protocol("WM_DELETE_WINDOW", _delete_window)
root.bind("<Destroy>", _destroy)


player_img = ImageTk.PhotoImage(Image.open('dude.gif'))
enemy_img = ImageTk.PhotoImage(Image.open('bandit.gif'))
forest_img = ImageTk.PhotoImage(Image.open('forest.gif'))
desert_img = ImageTk.PhotoImage(Image.open('desert.gif'))
mountain_img = ImageTk.PhotoImage(Image.open('mountain.gif'))
dirt_img = ImageTk.PhotoImage(Image.open('dirt.gif'))

def display(maps,root,good,bad, forest = forest_img, desert = desert_img, mountain = mountain_img, dirt = dirt_img):
    for i,row in enumerate(maps.grid):
        for j,column in enumerate(row):
            if (maps.grid[i][j].unit == None):
                if maps.grid[i][j].terrain.type == 'forest':
                    L = tk.Label(root, image = forest)
                elif maps.grid[i][j].terrain.type == 'desert':
                    L = tk.Label(root, image = desert)
                elif maps.grid[i][j].terrain.type == 'mountain':
                    L = tk.Label(root, image = mountain)
                elif maps.grid[i][j].terrain.type == 'dirt':
                    L = tk.Label(root, image = dirt)
                else:
                    L=tk.Label(root,text='    ',bg='green')
            else:
                if maps.grid[i][j].unit.player.name == 'human':
                    L = tk.Label(root, image = good)
                else:
                    print i,j
                    L = tk.Label(root, image = bad)
            L.grid(row=j,column=i)

#player units
#Looks like in 7 you get ~.03 units/space
eliwood = unit(world = level, space = level.get_space(0,0), name = "eliwood")
hector = unit(world = level, space = level.get_space(0,1), name = "hector")
lyn = unit(world = level, space = level.get_space(2,0), name = "lyn", hp = 15)
player_units = [eliwood, hector, lyn]

#enemy units
#in 7 there's just under twice as many enemies as your units at first
#then a bunch of reinforcements
#we aren't accounting for reinforcements....
sonia = unit(world = level, space = level.get_space(0,8), name = "sonia")
limstella = unit(world = level, space = level.get_space(1,8),attack = 7,name ="limstella")
enemy_units = [sonia, limstella]
for i in range(4):
    grunt = unit(world=level,space=level.get_space(2+i,8),name="grunt"+str(i))
    enemy_units.append(grunt)

com = player()
#note: python lists are passed by reference, so the copy is necessary
human = player(com, list(player_units), "human", "human")
com.initialize(human,list(enemy_units),"com", "com")

while(len(human.units) == len(player_units) and len(com.units) == len(enemy_units)):
    #run while no units have died
    display(level,root,player_img,enemy_img)
    while(len(human.movedUnits) != len(human.units)):
        human.play_turn(level)
        display(level,root,player_img,enemy_img)

    if(len(human.units) == len(player_units) and len(com.units) == len(enemy_units)):
        #only let the computer move if the game has not ended
        while (len(com.units) != len(com.actedUnits)):
            com.play_turn(level)
            display(level,root,player_img,enemy_img)
            time.sleep(1)
    #reset everything
    human.movedUnits = []
    human.actedUnits = []
    com.movedUnits = []
    com.actedUnits = []
if len(human.units) != len(player_units):
    print "Computer wins!"
else:
    print "Human wins!"
display(level,root,player_img,enemy_img)
root.destroy()
root.mainloop() 
