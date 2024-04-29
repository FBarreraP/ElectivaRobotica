from sympy import *
import numpy
import math

def NRotarY(theta):
    Ry = numpy.array([[math.cos(theta), 0, math.sin(theta)],
                     [0, 1, 0],
                     [-math.sin(theta), 0, math.cos(theta)]])
    print(f'Ry({theta})={Ry}')
    return Ry