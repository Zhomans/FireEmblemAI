from feworld import *
from unit import*
from FinalAI import *
from human import *


# this class is the upper level player. it does not make any decisions it simply has the mechanics needed for moving 
# units and having them act
class player(object):
	# the player has:
	# A list of units
	# A list of moved units
	# A list of units that have acted (attacked)
	# A name
	# knows the Enemy Object
	# A Type (human or computer)
	def __init__(self, player=None, units=None, name="Your mother", type="com"):
		self.units = units
		self.movedUnits = []
		self.actedUnits = []
		self.name = name
		self.opponent = player
		self.type = type
		if units != None:
			for unit in units:
				unit.player=self

	def decide_turn():
		pass
		#to be over written by the enemy and the AI classes

	def initialize(self, opponent, units, name, type):
        # since the first one we make can't have its opponent
        # We need to initialize it after creating the second one
        # Info about what is Initialize can be seen above
		self.units = units
		self.movedUnits = []
		self.actedUnits = []
		self.name = name
		self.opponent = opponent
		self.type = type
		if units != None:
			for unit in units:
				unit.player=self

	def play_turn(self, world, strat = "a"):
		
		# Check if the player is a computer or an object
		# create a player of the right type
		if self.type == "com":
			computer_player(self,world,strat)
			return False
		else:
			return human_player(self, world)

	def move_Unit(self, unit, world_map, new_location_x, new_location_y):
		# have the unit move and add it to the list of moved units
		movable = 1
		#go through the list of moved units and see if it is legal to move
		if (unit in self.movedUnits):
			movable = 0
			print('error unit has already been moved')
		# if you can move then move the unit and add it to the list of units you have moved
		if (movable == 1):
			if (unit.move_unit(world_map.get_space(new_location_x, new_location_y)) == 0):
				self.movedUnits.append(unit)
				return 1
		return 0
				
	def act_Unit(self, unit, world_map, unit_to_attack):
		#have the unit act and add it to the list of acting units
		actable = 1

		for k in range(len(self.actedUnits)): #make sure the unit hasn't acted yet
			if (unit == self.actedUnits[k]):
				actable = 0
				print('error that unit has already acted')

		if(actable == 1):	#if it hasnt acted, make it act and add it to the list
			unit.attack_enemy(unit_to_attack)
			self.actedUnits.append(unit)
			print unit.name+" attacked "+unit_to_attack.name+" at "+str(unit_to_attack.space)+" from "+str(unit.space)
