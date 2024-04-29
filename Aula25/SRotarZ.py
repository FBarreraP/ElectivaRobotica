from sympy import *
import numpy

def SRotarZ(theta):
    Rz = numpy.array([[cos(theta), -sin(theta), 0],
                      [sin(theta), cos(theta), 0],
                      [0, 0, 1]])
    print(f'Rz({theta})={Rz}')
    return Rz