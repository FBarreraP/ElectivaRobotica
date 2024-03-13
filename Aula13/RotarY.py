import math

def RotarY(theta):
    Ry = [math.cos(theta), 0, math.sin(theta)],[0, 1, 0],[-math.sin(theta), 0, math.cos(theta)];
    return Ry