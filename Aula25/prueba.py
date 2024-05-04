#------------------------------- Peter Corke ----------------------------------
from roboticstoolbox import *
from spatialmath.base import *
import numpy
from sympy import *

l1 = 12
l2 = 10
l3 = 10
l4 = 10
l5 = 10
l6 = 10

q1 = 0
q2 = 0
q3 = 0
q4 = 0
q5 = 0
q6 = 0

q = [q1,q2,q3,q4,q5,q6]

L = []
L.append(RevoluteDH(d=l1, alpha=numpy.pi/2, a=0, offset=0))
L.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
L.append(RevoluteDH(d=0, alpha=numpy.pi/2, a=0, offset=numpy.pi/2))
L.append(RevoluteDH(d=l3+l4, alpha=-numpy.pi/2, a=0, offset=-numpy.pi/2))
L.append(RevoluteDH(d=0, alpha=numpy.pi/2, a=0, offset=0))
L.append(RevoluteDH(d=l5+l6, alpha=0, a=0, offset=0))

Robot = DHRobot(L, name='Bender')
print(Robot)

Robot.teach(q, 'rpy/zyx', limits=[-50,50,-50,50,-50,50])

#zlim([-15,30]);

MTH = Robot.fkine(q)
print(MTH)
print(f'Roll, Pitch, Yaw = {tr2rpy(MTH.R, 'deg', 'zyx')}')
#theta = Robot.ikine_6s(MTH,'llllll',)
#print(f'theta1, theta2, theta3, theta4, theta5, theta6 = {theta}')


#------------------------------- Paso 1 ----------------------------------
#Paso 1 (Posición y orientación deseada del TCP) DH 6R
from NRotarX import *
from NRotarY import *
from NRotarZ import *
from numpy.linalg import multi_dot

d = [-9.4519, 33.8090, 42.7623]
R = multi_dot([NRotarZ(numpy.deg2rad(51.7776)),NRotarY(numpy.deg2rad(10.0935)),NRotarX(numpy.deg2rad(-26.561))])
mth = numpy.array([[R[0][0],R[0][1],R[0][2],d[0]], [R[1][0],R[1][1],R[1][2],d[1]], [R[2][0],R[2][1],R[2][2],d[2]], [0, 0, 0, 1]])
print(f'MTH = {mth}')

rz = R[0:3,2]#Desplazamiento en Z
print(f'rz = {rz}')
PosWrist = d-(l5+l6)*rz
print(f'PosWrist = {PosWrist}')
Tw = mth
Tw[0,3] = PosWrist[0]
Tw[1,3] = PosWrist[1]
Tw[2,3] = PosWrist[2]
print(f'Tw = {Tw}')

#------------------------------- Paso 2 ----------------------------------
# Cinemática inversa
import math

Px = PosWrist[0]
Py = PosWrist[1]
Pz = PosWrist[2]

e = sqrt(Px**2+Py**2)
c = Pz - l1
b = sqrt(e**2+c**2)
# Theta 1
theta1 = float(atan2(Py,Px))
print(f'theta 1 = {numpy.rad2deg(theta1):.4f}')
# Theta 3
cos_theta3 = (b**2-l2**2-(l3+l4)**2)/(2*l2*(l3+l4))
sen_theta3 = sqrt(1-(cos_theta3)**2)
theta3 = float(atan2(sen_theta3, cos_theta3))
print(f'theta 3 = {numpy.rad2deg(theta3):.4f}')
# Theta 2
alpha = math.atan2(c,e)
phi = math.atan2((l3+l4)*sen_theta3, l2+(l3+l4)*cos_theta3)
theta2 = float(alpha - phi)
if theta2 <= -numpy.pi:
    theta2 = (2*numpy.pi)+theta2

print(f'theta 2 = {numpy.rad2deg(theta2):.4f}')
#-------------

q1 = theta1
q2 = theta2
q3 = theta3

F = []
F.append(RevoluteDH(d=l1, alpha=numpy.pi/2, a=0, offset=0))
F.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
F.append(RevoluteDH(d=0, alpha=0, a=l3+l4, offset=0))

Robot = DHRobot(F, name='Bender')
print(Robot)

Robot.teach([q1, q2, q3], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])

#zlim([-15,30]);

MTH = Robot.fkine([q1,q2,q3])
print(MTH)
print(f'Roll, Pitch, Yaw = {tr2rpy(MTH.R, 'deg', 'zyx')}')

#------------------------------- Paso 3 ----------------------------------
# R03 = R01*R12*R23
# from SRotarX import *
# from SRotarY import *
# from SRotarZ import *
# theta1, theta2, theta3, theta4, theta5, theta6 = symbols('theta1 theta2 theta3 theta4 theta5 theta6')
# R01 = numpy.matmul(SRotarZ(theta1),SRotarX(pi/2))
# R12 = SRotarZ(theta2)
# R23 = multi_dot([SRotarZ(theta3),SRotarX(pi/2),SRotarY(pi/2)])
# R03 = simplify(multi_dot([R01,R12,R23]))
# print(f'R03 = {R03}')
# LR03 = latex(R03)
# print(f'Latex R03 = {LR03}')

R01 = numpy.matmul(NRotarZ(theta1),NRotarX(pi/2))
print(f'R01 = {R01}')
R12 = NRotarZ(theta2)
print(f'R12 = {R12}')
R23 = multi_dot([NRotarZ(theta3),NRotarX(pi/2),NRotarY(pi/2)])
print(f'R23 = {R23}')
R03 = multi_dot([R01,R12,R23])
print(f'R03 = {R03}')
RPY = tr2rpy(R03,'deg','zyx')
print(f'Roll, Pitch, Yaw = {RPY}')

#------------------------------- Paso 4 ----------------------------------
#Inversa de R03
# R03i = simplify(numpy.linalg.inv(R03))#Error de dtype('O') 
# LR03 = latex(R03)
# I = simplify(multi_dot([R03,R03i]))

R03i = numpy.linalg.inv(R03)
print(f'R03i = {R03i}')
I = numpy.matmul(R03i,R03) #Matriz identidad
print(f'I = {I}')

#------------------------------- Paso 5 ----------------------------------
# R36 numérica
R06 = R #Rotación deseada en el efector final
R36A = numpy.matmul(R03i,R06)
print(f'R36A = {R36A}')
# R36 = simplify(R03i*round(Tw.R)) #Error por R03i simbólica
# LR36 = latex(R36)

#------------------------------- Paso 6 ----------------------------------
# R36 simbólica
from SRotarX import *
from SRotarY import *
from SRotarZ import *
theta4, theta5, theta6 = symbols('theta4 theta5 theta6')
R34 = multi_dot([SRotarZ(theta4),SRotarZ(-pi/2),SRotarX(-pi/2)])
R45 = numpy.matmul(SRotarZ(theta5),SRotarX(pi/2))
R56 = SRotarZ(theta6)
R36B=simplify(multi_dot([R34,R45,R56]))
print(f'R36B = {R36B}')
LR36 = latex(R36B)
print(f'Latex R36B = {LR36}')

# R34 = numpy.matmul(NRotarZ(theta4),NRotarX(-pi/2))
# R45 = numpy.matmul(NRotarZ(theta5),NRotarX(pi/2))
# R56 = NRotarZ(theta6)
# R36B = multi_dot([R34,R45,R56])

#------------------------------- Paso 7 ----------------------------------
theta4 = math.atan2(R36A[0,2],-R36A[1,2])
print(f'theta4 = {theta4}')
theta6 = math.atan2(R36A[2,1],-R36A[2,0])
print(f'theta6 = {theta6}')
theta5 = math.atan2(sqrt(1-(R36A[2,2])**2),R36A[2,2])
print(f'theta5 = {theta5}')

#------------------------------- Paso 8 ----------------------------------
q1 = theta1
q2 = theta2
q3 = theta3
q4 = theta4
q5 = theta5
q6 = theta6

q = [q1,q2,q3,q4,q5,q6]

L = []
L.append(RevoluteDH(d=l1, alpha=numpy.pi/2, a=0, offset=0))
L.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
L.append(RevoluteDH(d=0, alpha=numpy.pi/2, a=0, offset=numpy.pi/2))
L.append(RevoluteDH(d=l3+l4, alpha=-numpy.pi/2, a=0, offset=-numpy.pi/2))
L.append(RevoluteDH(d=0, alpha=numpy.pi/2, a=0, offset=0))
L.append(RevoluteDH(d=l5+l6, alpha=0, a=0, offset=0))

Robot = DHRobot(L, name='Bender')
print(Robot)

Robot.teach(q, 'rpy/zyx', limits=[-50,50,-50,50,-50,50])

#zlim([-15,30]);

MTH = Robot.fkine(q)
print(MTH)
print(f'Roll, Pitch, Yaw = {tr2rpy(MTH.R, 'deg', 'zyx')}')
#theta = Robot.ikine_6s(MTH,'llllll',)
#print(f'theta1, theta2, theta3, theta4, theta5, theta6 = {theta}')