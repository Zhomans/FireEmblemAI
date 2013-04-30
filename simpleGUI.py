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
	forest_dude_img = ImageTk.PhotoImage(Image.open('forest_dude.gif'))
	desert_dude_img = ImageTk.PhotoImage(Image.open('desert_dude.gif'))
	mountain_dude_img = ImageTk.PhotoImage(Image.open('mountain_dude.gif'))
	dirt_dude_img = ImageTk.PhotoImage(Image.open('dirt_dude.gif'))
	forest_bandit_img = ImageTk.PhotoImage(Image.open('forest_bandit.gif'))
	desert_bandit_img = ImageTk.PhotoImage(Image.open('desert_bandit.gif'))
	mountain_bandit_img = ImageTk.PhotoImage(Image.open('mountain_bandit.gif'))
	dirt_bandit_img = ImageTk.PhotoImage(Image.open('dirt_bandit.gif'))
	for i in range(maps.x):
		for j in range(maps.y):
			if maps.grid[i][j].terrain.terrainType == 'desert':
				if (maps.grid[i][j].unit == None):
					L = tk.Label(root, image = desert_img)
					L.image = desert_img
				else:
					if maps.grid[i][j].unit.player.name == 'human':
						L = tk.Label(root, image = desert_dude_img)
						L.image = desert_dude_img
					else:
						L = tk.Label(root, image = desert_bandit_img)
						L.image = desert_bandit_img

			if maps.grid[i][j].terrain.terrainType == 'mountain':
				if (maps.grid[i][j].unit == None):
					L = tk.Label(root, image = mountain_img)
					L.image = mountain_img
				else:
					if maps.grid[i][j].unit.player.name == 'human':
						L = tk.Label(root, image = mountain_dude_img)
						L.image = mountain_dude_img
					else:
						L = tk.Label(root, image = mountain_bandit_img)
						L.image = mountain_bandit_img

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


