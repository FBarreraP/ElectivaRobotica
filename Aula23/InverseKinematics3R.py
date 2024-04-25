import numpy
import math
from sympy import *
from roboticstoolbox import *
from spatialmath.base import *

def InverseKinematics3R(l1,l2,l3,Px,Py,Pz):
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
    
    return theta1, theta2, theta3
    