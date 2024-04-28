from sympy import *
from RotarZ import *
from RotarX import *
import numpy

theta1 = symbols('theta1')
R01 = numpy.matmul(RotarZ(theta1),RotarX(pi/2))
print(f'R01 = {R01}')