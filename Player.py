#Player structure 
#not yet tested
# ROUGH DRAFT
#AAAH WHY DOES THIS USE TABS INSTEAD OF 4 SPACES????

from feworld import *
from unit import*
from FinalAI import *
from human import *

class player(object):
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
        #since the first one we make can't have its opponent
        #we need to initialize it after creating the second one
		self.units = units
		self.movedUnits = []
		self.actedUnits = []
		self.name = name
		self.opponent = opponent
		self.type = type
		if units != None:
			for unit in units:
				unit.player=self

	def play_turn(self, world):
		if self.type == "com":
			computer_player(self,world,"a")
		else:
			human_player(self, world)

	def move_Unit(self, unit, world_map, new_location_x, new_location_y):
		movable = 1
		#go through the list of moved units and see if it is legal to move
		if (unit in self.movedUnits):
			movable = 0
			print('error unit has already been moved')

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

		if(actable == 1):	#if it hasnt acted, make it act
			unit.attack_enemy(unit_to_attack)
			self.actedUnits.append(unit)
			print unit.name+" attacked "+unit_to_attack.name+" at "+str(unit_to_attack.space)+" from "+str(unit.space)
