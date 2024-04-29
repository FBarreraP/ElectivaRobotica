from sympy import *
import numpy
import math

def NRotarX(theta):
    Rx = numpy.array([[1, 0, 0],
                     [0, math.cos(theta), -math.sin(theta)],
                     [0, math.sin(theta), math.cos(theta)]])
    print(f'Rx({theta})={Rx}')
    return Rx