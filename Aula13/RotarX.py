from sympy import *
import numpy

def RotarX(theta):
    Rx = numpy.array([1, 0, 0],
                     [0, cos(theta), -sin(theta)],
                     [0, sin(theta), cos(theta)])
    return Rx