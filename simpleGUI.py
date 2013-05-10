#simpleGUI.py
#Jazmin Gonzalez-Rivero, Zachary Homans, Elizabeth Mahon, Brendan Ritter
#Artificial Intelligence, Olin College, Spring 13

#Displays GUI

import Tkinter as tk
import feworld
from PIL import ImageTk
from PIL import Image

#takes the level map and the GUI initialized in the test code
def display(maps, root):
	
	#get all of the imanges
	player_img = ImageTk.PhotoImage(Image.open('dude.gif'))
	enemy_img = ImageTk.PhotoImage(Image.open('bandit.gif'))
	forest_img = ImageTk.PhotoImage(Image.open('forest.gif'))
	dirt_img = ImageTk.PhotoImage(Image.open('dirt.gif'))
	forest_dude_img = ImageTk.PhotoImage(Image.open('forest_dude.gif'))
	dirt_dude_img = ImageTk.PhotoImage(Image.open('dirt_dude.gif'))
	forest_bandit_img = ImageTk.PhotoImage(Image.open('forest_bandit.gif'))
	dirt_bandit_img = ImageTk.PhotoImage(Image.open('dirt_bandit.gif'))
	
	# loop through each position in the grid
	# check for terrain type
	# check for unit type
	# select the image that has the correct unit and terrain
	# output the image
	for i in range(maps.x):
		for j in range(maps.y):
			if maps.grid[i][j].terrain.type == 'dirt':
				if (maps.grid[i][j].unit == None):
					L = tk.Label(root, image = dirt_img)
					L.image = dirt_img
				else:
					if maps.grid[i][j].unit.player.name == 'human':
						L = tk.Label(root, image = dirt_dude_img)
						L.image = dirt_dude_img
					else:
						L = tk.Label(root, image = dirt_bandit_img)
						L.image = dirt_bandit_img

			else:
				if (maps.grid[i][j].unit == None):
					L = tk.Label(root, image = forest_img)
					L.image = forest_img
				else:
					if maps.grid[i][j].unit.player.name == 'human':
						L = tk.Label(root, image = forest_dude_img)
						L.image = forest_dude_img
					else:
						L = tk.Label(root, image = forest_bandit_img)
						L.image = forest_bandit_img
			L.grid(row=j,column=i)
