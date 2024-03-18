from roboticstoolbox import *
import math

l1 = 6
l2 = 7
l3 = 3
l4 = 2

q1 = 0
q2 = 0

R = []
R.append(RevoluteDH(d=l1, alpha=math.pi/2, a=l3, offset=math.pi/2))
R.append(PrismaticDH(theta=0, alpha=0, a=0, offset=l2+l4))
R[1].qlim = [0,10]

Robot = DHRobot(R, name='Bender')
print(Robot)

Robot.teach([q1, q2], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])

#zlim([-15,30]);

MTH = Robot.fkine([q1,q2])
print(MTH)