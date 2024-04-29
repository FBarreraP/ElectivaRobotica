from sympy import *
import numpy

def SRotarY(theta):
    Ry = numpy.array([[cos(theta), 0, sin(theta)],
                     [0, 1, 0],
                     [-sin(theta), 0, cos(theta)]])
    print(f'Ry({theta})={Ry}')
    return Ry