from sympy import *
import numpy
import math

def NRotarZ(theta):
    Rz = numpy.array([[math.cos(theta), -math.sin(theta), 0],
                      [math.sin(theta), math.cos(theta), 0],
                      [0, 0, 1]])
    print(f'Rz({theta})={Rz}')
    return Rz