import numpy
import math
from sympy import *
from roboticstoolbox import *
from spatialmath.base import *

def ForwardKinematics3R(l1,l2,l3,q1,q2,q3):
    
    Robot = SerialLink([
        RevoluteDH(d=l1, alpha=numpy.pi/2, a=0, offset=0),
        RevoluteDH(d=0, alpha=0, a=l2, offset=0),
        RevoluteDH(d=0, alpha=0, a=l3, offset=0)
    ], name='Bender')

    print(Robot)

    Robot.plot([q1, q2, q3], limits=[-30,30,-30,30,-30,30])

    #zlim([-15,30]);

    MTH = Robot.fkine([q1,q2,q3])
    print(MTH)
    print(f'Roll, Pitch, Yaw = {tr2rpy(MTH.R, 'deg', 'zyx')}')
    
    return MTH