from robolink import *
from robodk import *

RDK = Robolink()
robot = RDK.Item('UR5e', ITEM_TYPE_ROBOT)
robot.setSpeedJoints(90)