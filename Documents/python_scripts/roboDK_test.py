from robolink import *
from robodk import *

RDK = Robolink()
robot = RDK.Item('UR5e', ITEM_TYPE_ROBOT)
target_1 = RDK.Item('Target 1')
target_2 = RDK.Item('Target 2')

cycle_count = 0

robot.MoveJ(target_1)

while True:
	robot.MoveJ(target_2)
	robot.MoveJ(target_1)
	cycle_count += 1
	print("Cycles performed: ", cycle_count)
