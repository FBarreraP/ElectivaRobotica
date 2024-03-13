from sympy import *
import numpy
# from roboticstoolbox import *
from scipy.spatial.transform import Rotation as R

#Transformaciones (MTH)

theta1, theta2, h1, h2, l1, l2 = symbols('theta1 theta2 h1 h2 l1 l2')
# theta1 = pi/2
# theta2 = pi/2
# l1 = 5;
# l2 = 5;
# h1 = 3;
# h2 = 2;

T01 = numpy.array([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, h1],
                   [0, 0, 0, 1]])

T12 = numpy.array([[cos(theta1), -sin(theta1), 0, l1*cos(theta1)],
                   [sin(theta1), cos(theta1), 0, l1*sin(theta1)],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])

T23 = numpy.array([[cos(theta2), -sin(theta2), 0, l2*cos(theta2)],
                   [sin(theta2), cos(theta2), 0, l2*sin(theta2)],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])

   
T34 = numpy.array([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, -h2],
                   [0, 0, 0, 1]])

T02 = numpy.matmul(T01,T12)
T24 = numpy.matmul(T23,T34)
T04 = simplify(numpy.matmul(T02,T24))
# T04 = (numpy.matmul(T02,T24))
print(f'T04 = {T04}')

# r = R.from_matrix(T04[:3,:3])
# print(f'r = {r}')
# # m = numpy.rad2deg(tr2rpy(r,'zyx'))
# m = r.as_euler('zyx', degrees=True)
# print(f'm = {m}')


# import numpy as np
# from scipy.spatial.transform import Rotation as R

# # Definir una matriz de transformación homogénea (por ejemplo, rotación de 45 grados alrededor del eje z)
# R_matrix = np.array([[np.sqrt(2)/2, -np.sqrt(2)/2, 0, 0],
#                      [np.sqrt(2)/2,  np.sqrt(2)/2, 0, 0],
#                      [          0,            0, 1, 0],
#                      [          0,            0, 0, 1]])

# # Convertir la matriz de transformación en un objeto de rotación
# r = R.from_matrix(R_matrix[:3, :3])

# # Obtener los ángulos de rollo, cabeceo y guiñada (RPY)
# rpy = r.as_euler('zyx', degrees=True)

# print("Angulos de RPY (grados):", rpy)