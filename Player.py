#Player structure 
#not yet tested
# ROUGH DRAFT 

import feworld.py
import unit.py

class player(object):
	def __init__(self, player, units, name):
		self.units = units
		self.movedUnits = []
		self.actedUnits = []
		self.name = name
		self.opponent = player
	def decide_turn():
		#to be over written by the enemy and the AI classes


	def move_Unit(self, unit, world_map, new_location_x, new_location_y, old_location_x, old_location_y):
		int moved = 0
#	int reset = 0
		int movable = 1

		for k in range(length(self.movedUnits)): #go through the list of moved units and see if it is legal to move
			if (unit == self.movedUnits[k]):
				movable = 0;
				print('error unit has already been moved')

		if (movable == 1):
			for i in range(length(world_map.grid)):	#find the correct row
				for j in range(length(world_map.grid[i])):	#find the correct column
					if(world_map.grid[i][j].x == new_location_x && world.map.grid[i][j].y == new_location_y):
						if(world_map.grid[i][j].unit == None) #check if space is free
							world_map.grid[i][j].add_unit(unit) #move unit to proper space
							moved = 1
							self.movedUnits.append(unit)
							print('unit moved successfully')
							return
						else:
							print('error another unit is already occupying that space')
#					if(world_map.grid[i][j].x == old_location_x && world.map.grid[i][j].y == old_location_y):
#						world_map.grid[i][j].add_unit(None)
#						reset = 1
#					if(reset == 1 && moved == 1):
				if( i == length(world_map.grid) - 1):
					print('an error has occured')
				
	def act_Unit(self, unit, world_map, unit_to_attack):
		#have the unit act and add it to the list of acting units
		int actable = 1

		for k in range(length(self.actedUnits)): #make sure the unit hasn't acted yet
			if (unit == self.actedUnits[k]):
				actable = 0
				print('error that unit has already acted')

		if(actable == 1)	#if it hasnt acted, make it act
			if(k == length(self.actedUnits)- 1):
				unit.attack(unit_to_attack)
				self.actedUnits.append(unit)
				print('unit has successfully attacked enemy unit')
