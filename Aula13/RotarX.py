from sympy import *

def RotarX(theta):
    Rx = [1, 0, 0],[0, cos(theta), -sin(theta)],[0, sin(theta), cos(theta)];
    return Rx