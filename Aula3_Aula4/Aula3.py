from roboticstoolbox import *
import math

l1 = 12
l2 = 14
l3 = 6
l4 = 4

q1 = 0
q2 = 0

R = []
R.append(RevoluteDH(d=l1, alpha=math.pi/2, a=l2, offset=0))
R.append(RevoluteDH(d=l3, alpha=0, a=l4, offset=0))

Robot = DHRobot(R, name='Bender')
print(Robot)

Robot.teach([q1, q2], limits=[-30,30,-30,30,-30,30])

#zlim([-15,30]);

MTH = Robot.fkine([q1,q2])
print(MTH)