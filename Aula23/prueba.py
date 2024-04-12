from roboticstoolbox import *
from spatialmath.base import *
import math
import numpy
from sympy import *

l1 = 10
l2 = 10
l3 = 10

# Cinemática inversa
Px = -9.545
Py = 7.896
Pz = 23.192

e = sqrt(Px**2+Py**2)
c = Pz - l1
b = sqrt(e**2+c**2)
# Theta 1
theta1 = float(atan2(Py,Px))
print(f'theta 1 = {numpy.rad2deg(theta1):.4f}')
# Theta 3
cos_theta3 = (b**2-l2**2-l3**2)/(2*l2*l3)
sen_theta3 = sqrt(1-(cos_theta3)**2)
theta3 = float(atan2(sen_theta3, cos_theta3))
print(f'theta 3 = {numpy.rad2deg(theta3):.4f}')
# Theta 2
alpha = math.atan2(c,e)
phi = math.atan2(l3*sen_theta3, l2+l3*cos_theta3)
theta2 = float(alpha - phi)
if theta2 <= -pi:
    theta2 = (2*pi)+theta2

print(f'theta 2 = {numpy.rad2deg(theta2):.4f}')
#-------------

q1 = theta1
q2 = theta2
q3 = theta3

R = []
R.append(RevoluteDH(d=l1, alpha=numpy.pi/2, a=0, offset=0))
R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
R.append(RevoluteDH(d=0, alpha=0, a=l3, offset=0))

Robot = DHRobot(R, name='Bender')
print(Robot)

Robot.teach([q1, q2, q3], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])

#zlim([-15,30]);

MTH = Robot.fkine([q1,q2,q3])
print(MTH)
print(f'Roll, Pitch, Yaw = {tr2rpy(MTH.R, 'deg', 'zyx')}')