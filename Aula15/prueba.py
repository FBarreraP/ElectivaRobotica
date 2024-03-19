from roboticstoolbox import *
from spatialmath.base import *
import math

a1 = 15
a2 = 5
a3 = 8
a4 = 5
a5 = 6

q1 = 0
q2 = 0
q3 = 0
q4 = 0

R = []
R.append(RevoluteDH(d=a1, alpha=0, a=a2, offset=0))
R.append(RevoluteDH(d=0, alpha=math.pi, a=a3, offset=0))
R.append(PrismaticDH(theta=0, alpha=0, a=0, offset=a4))
R[2].qlim = [0,10]
R.append(RevoluteDH(d=a5, alpha=0, a=0, offset=0))

Robot = DHRobot(R, name='Bender')
print(Robot)

Robot.teach([q1, q2, q3, q4], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])

#zlim([-15,30]);

MTH = Robot.fkine([q1,q2,q3,q4])
print(MTH)

r = MTH[:3,:3]
print(f'r = {r}')

print(f'Yaw, Pitch, Roll = {tr2rpy(r, 'deg', 'zyx')}')