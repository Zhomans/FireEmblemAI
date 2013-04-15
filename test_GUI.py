#Python script to test stuff to make sure it's doing what we want
#separate from other files because we have multiple class files
#also then you don't get weird stuff happening when you import the file
#I know there's a way around that second one that Allen puts in all his code
#But I don't feel like checking it, so deal with it.

from feworld import *
from unit import *
from simpleGUI import *

map = fe_map()
print map

print map.get_space(1,1)
eliwood = unit()
map.get_space(1,1).add_unit(eliwood)
#print map

#eliwood.move_unit(map.get_space(4, 3))
eliwood.move_list = eliwood.get_move_list()
print eliwood.get_attack_list()
#print eliwood.move_list
display(map)