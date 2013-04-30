import Tkinter as tk
import feworld
from PIL import ImageTk
from PIL import Image

def display(maps, root):
	player_img = ImageTk.PhotoImage(Image.open('dude.gif'))
	enemy_img = ImageTk.PhotoImage(Image.open('bandit.gif'))
	forest_img = ImageTk.PhotoImage(Image.open('forest.gif'))
	desert_img = ImageTk.PhotoImage(Image.open('desert.gif'))
	mountain_img = ImageTk.PhotoImage(Image.open('mountain.gif'))
	dirt_img = ImageTk.PhotoImage(Image.open('dirt.gif'))
	for i in range(maps.x):
		for j in range(maps.y):
			if (maps.grid[i][j].unit == None):
				if maps.grid[i][j].terrain.terrainType == 'forest':
					L = tk.Label(root, image = forest_img)
					L.image = forest_img
				if maps.grid[i][j].terrain.terrainType == 'desert':
					L = tk.Label(root, image = desert_img)
					L.image = desert_img
				if maps.grid[i][j].terrain.terrainType == 'mountain':
					L = tk.Label(root, image = mountain_img)
					L.image = mountain_img
				if maps.grid[i][j].terrain.terrainType == 'dirt':
					L = tk.Label(root, image = dirt_img)
					L.image = dirt_img
				else:
					L=tk.Label(root,text='    ',bg='green')
			else:
				if maps.grid[i][j].unit.player.name == 'human':
					L = tk.Label(root, image = player_img)
					L.image = player_img
				else:
					L = tk.Label(root, image = enemy_img)
					L.image = enemy_img
			L.grid(row=j,column=i)

