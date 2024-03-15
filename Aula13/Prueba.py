from sympy import *
from RotarZ import *
import numpy

theta1, theta2 = symbols('theta1 theta2')
RZ1 = simplify(numpy.matmul(RotarZ(theta1),RotarZ(theta2)))
print(f'RZ1 = {RZ1}')
RZ2 = simplify(numpy.matmul(RotarZ(theta2),RotarZ(theta1)))
print(f'RZ2 = {RZ2}')
RZ3 = simplify(RotarZ(theta1+theta2))
print(f'RZ3 = {RZ3}')