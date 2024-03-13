from sympy import *
import numpy

def RotarZ(theta):
    Rz = numpy.array([[cos(theta), -sin(theta), 0],
                      [sin(theta), cos(theta), 0],
                      [0, 0, 1]])
    return Rz