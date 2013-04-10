#Player structure 
#not yet tested
# ROUGH DRAFT 

import feworld.py
import unit.py

class player(object):
	def __init__(self, player):
		self.units = []
		self.movedUnits = []
		self.actedUnits = []
		self.name = ''
		self.opponent = player
	def decide_turn():
		#to be over written by the enemy and the AI classes


	def move_Unit(self, unit, world_map, new_location_x, new_location_y, old_location_x, old_location_y):
		int moved
		moved = 0
		int reset
		reset = 0
		for k in range(length(self.movedUnits)):
			if (unit == self.movedUnits[k]):
				print 'error unit has already been moved'
			if (k == length(self.movedUnits) -1):
				for i in range(length(world_map.grid)):
					for j in range(length(world_map.grid[i])):
						if(world_map.grid[i][j].x == new_location_x && world.map.grid[i][j].y == new_location_y):
							world_map.grid[i][j].unit = unit
							moved = 1
						if(world_map.grid[i][j].x == old_location_x && world.map.grid[i][j].y == old_location_y):
							world_map.grid[i][j] = None
							reset = 1
						if(reset == 1 && moved == 1):
							self.movedUnits.append(unit)
							print 'unit moved successfully'
							return
					if( i == length(world_map.grid) - 1):
						print 'an error has occured'
				
	def attack_Unit(self, unit, world_map, unit_to_attack):
		#to be over written by enemy and AI classes?
		#add the attack unit to the move unit class
		for k in range(length(self.actedUnits)):
			if (unit == self.actedUnits[k]):
				print 'error that unit has already acted'
			if(k == length(self.actedUnits)- 1):
				unit.attack(unit_to_attack)
				self.actedUnits.append(unit)
				print 'unit has successfully attacked enemy unit'
