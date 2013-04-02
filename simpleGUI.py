import Tkinter as tk
board=[[None]*10 for _ in range(10)]
counter=0
root=tk.Tk()
photo=tk.PhotoImage(file="dude.gif")
label=tk.Label(root,image=photo)
label.image=photo
label.pack()
for i,row in enumerate(board):
	for j,column in enumerate(row):
		if ((i+j) % 2) ==0:
			L=tk.Label(root,text='    ',bg='green')
		else:
			L=tk.Label(root,text='    ',bg='dark green')
		L.grid(row=i,column=j)
root.mainloop()