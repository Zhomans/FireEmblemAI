import Tkinter as tk
import feworld
from PIL import ImageTk
from PIL import Image

def display(maps):
	board=[[None]*10 for _ in range(10)]
	counter=0
	root=tk.Tk()
	player_img = ImageTk.PhotoImage(Image.open('dude.gif'))
	enemy_img = ImageTk.PhotoImage(Image.open('bandit.gif'))
	forest_img = ImageTk.PhotoImage(Image.open('forest.gif'))
	desert_img = ImageTk.PhotoImage(Image.open('desert.gif'))
	mountain_img = ImageTk.PhotoImage(Image.open('mountain.gif'))
	for i,row in enumerate(board):
		for j,column in enumerate(row):
			if (maps.grid[i][j].unit == None):
				if maps.grid[i][j].terrain.terrainType = 'forest':
					L = tk.Label(root, image = forest_img)
				if maps.grid[i][j].terrain.terrainType = 'desert':
					L = tk.Label(root, image = desert_img)
				if maps.grid[i][j].terrain.terrainType = 'mountain':
					L = tk.Label(root, image = mountain_img)
				else:
					L=tk.Label(root,text='    ',bg='green')
			else:
				if maps.grid[i][j].unit.player.name == 'human':
					L = tk.Label(root, image = player_img)
				else:
					L = tk.Label(root, image = enemy_img)
			L.grid(row=j,column=i)
	root.mainloop()
