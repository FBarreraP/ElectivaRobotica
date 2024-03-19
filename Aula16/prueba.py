from roboticstoolbox import *
from spatialmath.base import *
from sympy import *
import numpy
from numpy.linalg import multi_dot

a1 = 15
a2 = 5
a3 = 8
a4 = 5
a5 = 6

q1 = numpy.pi/3
q2 = numpy.pi/6
q3 = 8
q4 = numpy.pi/4

R = []
R.append(RevoluteDH(d=a1, alpha=0, a=a2, offset=0))
R.append(RevoluteDH(d=0, alpha=numpy.pi, a=a3, offset=0))
R.append(PrismaticDH(theta=0, alpha=0, a=0, offset=a4))
R[2].qlim = [0,10]
R.append(RevoluteDH(d=a5, alpha=0, a=0, offset=0))

Robot = DHRobot(R, name='Bender')
print(Robot)

Robot.teach([q1, q2, q3, q4], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])

#zlim([-15,30]);

MTH = Robot.fkine([q1,q2,q3,q4])
print(MTH)

#Matriz (DH)
TZ0 = numpy.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, a1],[0, 0, 0, 1]])
RZ0 = numpy.array([[cos(q1), -sin(q1), 0, 0],[sin(q1), cos(q1), 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
TX1 = numpy.array([[1, 0, 0, a2],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
RX1 = numpy.array([[1, 0, 0, 0],[0, cos(0), -sin(0), 0],[0, sin(0), cos(0), 0],[0, 0, 0, 1]])
T01 = multi_dot([TZ0,RZ0,TX1,RX1])
print(f'T01 = {T01}')
T01 = multi_dot([RZ0,TZ0,RX1,TX1])
print(f'T01 = {T01}')

TZ1 = numpy.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
RZ1 = numpy.array([[cos(q2), -sin(q2), 0, 0],[sin(q2), cos(q2), 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
TX2 = numpy.array([[1, 0, 0, a3],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
RX2 = numpy.array([[1, 0, 0, 0],[0, cos(-pi), -sin(-pi), 0],[0, sin(-pi), cos(-pi), 0],[0, 0, 0, 1]])
T12 = multi_dot([TZ1,RZ1,TX2,RX2])
print(f'T12 = {T12}')
T12 = multi_dot([RZ1,TZ1,RX2,TX2])
print(f'T12 = {T12}')

TZ2 = numpy.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, a4+q3],[0, 0, 0, 1]])
RZ2 = numpy.array([[cos(0), -sin(0), 0, 0],[sin(0), cos(0), 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
TX3 = numpy.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
RX3 = numpy.array([[1, 0, 0, 0],[0, cos(0), -sin(0), 0],[0, sin(0), cos(0), 0],[0, 0, 0, 1]])
T23 = multi_dot([TZ2,RZ2,TX3,RX3])
print(f'T23 = {T23}')
T23 = multi_dot([RZ2,TZ2,RX3,TX3])
print(f'T23 = {T23}')

TZ3 = numpy.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, a5],[0, 0, 0, 1]])
RZ3 = numpy.array([[cos(q4), -sin(q4), 0, 0],[sin(q4), cos(q4), 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
TX4 = numpy.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
RX4 = numpy.array([[1, 0, 0, 0],[0, cos(0), -sin(0), 0],[0, sin(0), cos(0), 0],[0, 0, 0, 1]])
T34 = multi_dot([TZ3,RZ3,TX4,RX4])
print(f'T34 = {T34}')
T34 = multi_dot([RZ3,TZ3,RX4,TX4])
print(f'T34 = {T34}')

T04 = multi_dot([T01,T12,T23,T34])
print(f'T04 = {T04}')

r = T04[:3,:3]
print(f'r = {r}')
print(f'Roll, Pitch, Yaw = {tr2rpy(r, 'deg', 'zyx')}')