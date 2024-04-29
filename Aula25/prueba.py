#Paso 1 (Posición y orientación deseada del TCP) DH 6R

from RotarX import *
from RotarY import *
from RotarZ import *
import numpy
from numpy.linalg import multi_dot

l5 = 10
l6 = 10

d = [-9.4519, 33.8090, 42.7623]
R = multi_dot([RotarZ(numpy.deg2rad(51.7776)),RotarY(numpy.deg2rad(10.0935)),RotarX(numpy.deg2rad(-26.561))])
mth = numpy.array([[R[0][0],R[0][1],R[0][2],d[0]], [R[1][0],R[1][1],R[1][2],d[0]], [R[2][0],R[2][1],R[2][2],d[0]], [0, 0, 0, 1]])
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