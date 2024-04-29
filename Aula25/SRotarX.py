from sympy import *
import numpy

def SRotarX(theta):
    Rx = numpy.array([[1, 0, 0],
                     [0, cos(theta), -sin(theta)],
                     [0, sin(theta), cos(theta)]])
    print(f'Rx({theta})={Rx}')
    return Rx