from sympy import *
import numpy

def RotarY(theta):
    Ry = numpy.array([cos(theta), 0, sin(theta)],
                     [0, 1, 0],
                     [-sin(theta), 0, cos(theta)])
    return Ry