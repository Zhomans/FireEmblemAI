#Player structure 
#not yet tested
# ROUGH DRAFT
#AAAH WHY DOES THIS USE TABS INSTEAD OF 4 SPACES????

from feworld import *
from unit import*

class player(object):
	def __init__(self, player=None, units=None, name="Your mother", type="com"):
		self.units = units
		self.movedUnits = []
		self.actedUnits = []
		self.name = name
		self.opponent = player
		self.type = type
	def decide_turn():
		pass
		#to be over written by the enemy and the AI classes

	def initialize(self, opponent, units, name, type):
        #since the first one we make can't have its opponent
        #we need to initialize it after creating the second one
		self.units = units
		self.movedUnits = []
		self.actedUnits = []
		self.name = name
		self.opponent = opponent
		self.type = type


	def move_Unit(self, unit, world_map, new_location_x, new_location_y):
		movable = 1
		#go through the list of moved units and see if it is legal to move
		if (unit in self.movedUnits):
			movable = 0
			print('error unit has already been moved')

		if (movable == 1):
			for i in range(len(world_map.grid)):	#find the correct row
				for j in range(len(world_map.grid[i])):	#find the correct column
					if(world_map.grid[i][j].x == new_location_x and world_map.grid[i][j].y == new_location_y):
						if(world_map.grid[i][j].unit == None):
							#check if space is free
							world_map.grid[i][j].add_unit(unit)
							#move unit to proper space
							self.movedUnits.append(unit)
							print('unit moved successfully')
							return
						else:
							print('error another unit is already occupying that space')
				if( i == len(world_map.grid) - 1):
					print('an error has occured')
				
	def act_Unit(self, unit, world_map, unit_to_attack):
		#have the unit act and add it to the list of acting units
		actable = 1

		for k in range(len(self.actedUnits)): #make sure the unit hasn't acted yet
			if (unit == self.actedUnits[k]):
				actable = 0
				print('error that unit has already acted')

		if(actable == 1):	#if it hasnt acted, make it act
			if(k == len(self.actedUnits)- 1):
				unit.attack(unit_to_attack)
				self.actedUnits.append(unit)
				print('unit has successfully attacked enemy unit')
