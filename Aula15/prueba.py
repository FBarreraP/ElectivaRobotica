from roboticstoolbox import *
from spatialmath.base import *
from sympy import *
import numpy
from numpy.linalg import multi_dot

a1 = 12
a2 = 14
a3 = 6
a4 = 4

q1 = 0
q2 = 0

R = []
R.append(RevoluteDH(d=a1, alpha=numpy.pi/2, a=a2, offset=0))
R.append(RevoluteDH(d=a3, alpha=0, a=a4, offset=0))

Robot = DHRobot(R, name='Bender')
print(Robot)

Robot.teach([q1, q2], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])

#zlim([-15,30]);

MTH = Robot.fkine([q1,q2])
print(MTH)

#Matriz (DH)
TZ0 = numpy.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, a1],[0, 0, 0, 1]])
RZ0 = numpy.array([[cos(q1), -sin(q1), 0, 0],[sin(q1), cos(q1), 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
TX1 = numpy.array([[1, 0, 0, a2],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
RX1 = numpy.array([[1, 0, 0, 0],[0, cos(pi/2), -sin(pi/2), 0],[0, sin(pi/2), cos(pi/2), 0],[0, 0, 0, 1]])
T01 = multi_dot([TZ0,RZ0,TX1,RX1])
print(f'T01 = {T01}')
T01 = multi_dot([RZ0,TZ0,RX1,TX1])
print(f'T01 = {T01}')

TZ1 = numpy.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, a3],[0, 0, 0, 1]])
RZ1 = numpy.array([[cos(q2), -sin(q2), 0, 0],[sin(q2), cos(q2), 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
TX2 = numpy.array([[1, 0, 0, a4],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
RX2 = numpy.array([[1, 0, 0, 0],[0, cos(0), -sin(0), 0],[0, sin(0), cos(0), 0],[0, 0, 0, 1]])
T12 = multi_dot([TZ1,RZ1,TX2,RX2])
print(f'T12 = {T12}')
T12 = multi_dot([RZ1,TZ1,RX2,TX2])
print(f'T12 = {T12}')

T02 = numpy.matmul(T01,T12)
print(f'T02 = {T02}')

r = T02[:3,:3]
print(f'r = {r}')
print(f'Roll, Pitch, Yaw = {tr2rpy(r, 'deg', 'zyx')}')