#err lets give this a try
from feworld import *
from unit import *
from Player import *

that_level_with_the_villages=fe_map()

fiona=unit()
a_small_dog=unit()
that_boss_that_one_hits_noobs=unit()

that_level_with_the_villages.get_space(1,1).add_unit(fiona)
that_level_with_the_villages.get_space(1,2).add_unit(a_small_dog)
that_level_with_the_villages.get_space(3,3).add_unit(that_boss_that_one_hits_noobs)

computer=player()
human=player(computer,[fiona,a_small_dog],"Mon-Keigh")

human.move_Unit(fiona,that_level_with_the_villages,2,1,fiona.get_x(),fiona.get_y())