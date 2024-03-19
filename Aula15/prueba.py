from roboticstoolbox import *
from spatialmath.base import *
import math

a1 = 12
a2 = 14
a3 = 6
a4 = 4

q1 = 0
q2 = 0

R = []
R.append(RevoluteDH(d=a1, alpha=math.pi/2, a=a2, offset=0))
R.append(RevoluteDH(d=a3, alpha=0, a=a4, offset=0))

Robot = DHRobot(R, name='Bender')
print(Robot)

Robot.teach([q1, q2], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])

#zlim([-15,30]);

MTH = Robot.fkine([q1,q2])
print(MTH)
print(f'Roll, Pitch, Yaw = {tr2rpy(MTH.R, 'deg', 'zyx')}')