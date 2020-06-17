#Robotic verification of cameras
#Subtasks:
##Robot/Checkerboard:

###Simulate in RoboDK, find feasible placement of arm wrt. camera to cover FOV, make a tentative trajectory
Done, we likely have something that can be used at least as a starting point. However, not having been tested with the actual robot/in the actual room, changes will likely have to be made
###Thoughts on checkerboard design, both visually and for having the mounting in the middle of the board without interfering visually with the checkerboard pattern
For now: Known that the dimensions will be A3 (297mm x 420 mm) with 20mm x 20mm checkers.
###Thoughts on challenges with fitting the robot cage on the side of the calibration room
Measurements, free space in calibration room:
to doorwall: 135cm
other way: 107, 160 if narrower than 135

Cage measurements:
outer dimensions:
length: 156 cm
width: 141 cm
aluminium bar thickness: 4cm
length from robot base center to end of cage (closest): 24 cm
length, controller part of cage (outer dimensions): 28 cm

####First thoughts on challenges:
- The cage needs to be shorter, leading to decreased footprint => basically decreased stability/robustness to falling over.
- The robot arm operates mainly outside of the cage as opposed to within it, leading to more torque acting on the cage in a direction it's not secured against (unless we fasten it to the floor).


###Do inventory of what kinds of resources (hardware or otherwise) might be necessary throughout the project
##Camera/Image recognition/post processing:
###Get an overview of what already exists in terms of checkerboard recognition/fitting code and get acquainted with it, find out optionally what still needs to be written, get a grip on how it can be integrated with the rest of the project
###Test HDR capture using the camera directly from python script/get familiar with the SDK
This turned out to be astoundingly easy. The SDK is easy to work with throughout, and allows for capture assist which simplifies testing things out.

