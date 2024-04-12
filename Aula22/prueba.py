from roboticstoolbox import *
from spatialmath.base import *
import math
import numpy

l1 = 10
l2 = 10

# Cinemática inversa
Px = -10.577
Py = -3.808

b = math.sqrt(Px**2+Py**2)
# Theta 2
cos_theta2 = (b**2-l2**2-l1**2)/(2*l1*l2)
sen_theta2 = math.sqrt(1-(cos_theta2)**2)#(+)codo abajo y (-)codo arriba
theta2 = math.atan2(sen_theta2, cos_theta2)
print(f'theta 2 = {numpy.rad2deg(theta2):.4f}')
# Theta 1
alpha = math.atan2(Py,Px)
phi = math.atan2(l2*sen_theta2, l1+l2*cos_theta2)
theta1 = alpha - phi
print(f'theta 1 = {numpy.rad2deg(theta1):.4f}')
#-------------

q1 = theta1
q2 = theta2

R = []
R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))

Robot = DHRobot(R, name='Bender')
print(Robot)

Robot.teach([q1, q2], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])

#zlim([-15,30]);

MTH = Robot.fkine([q1,q2])
print(MTH)
print(f'Roll, Pitch, Yaw = {tr2rpy(MTH.R, 'deg', 'zyx')}')