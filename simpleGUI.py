import Tkinter as tk
import feworld
from PIL import ImageTk
from PIL import Image

def display(maps):
	board=[[None]*10 for _ in range(10)]
	counter=0
	root=tk.Tk()
	img = ImageTk.PhotoImage(Image.open('dude.gif'))
	for i,row in enumerate(board):
		for j,column in enumerate(row):
			if (maps.grid[i][j].unit == None):
				if ((i+j) % 2) ==0:
					L=tk.Label(root,text='    ',bg='green')
				else:
					L=tk.Label(root,text='    ',bg='dark green')
			else:
				L = tk.Label(root, image = img)
			L.grid(row=i,column=j)
	root.mainloop()
