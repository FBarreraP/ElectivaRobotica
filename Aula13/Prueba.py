from sympy import *
from RotarZ import *
import numpy

#Transformaciones (MTH)

syms h1 h2 theta1 theta2 l1 l2
# theta1 = pi/2
# theta2 = pi/2
# l1 = 5;
# l2 = 5;
# h1 = 3;
# h2 = 2;

T01 = [1 0 0 0;
       0 1 0 0;
       0 0 1 h1;
       0 0 0 1]

T12 = [cos(theta1) -sin(theta1) 0 l1*cos(theta1);
       sin(theta1) cos(theta1)  0 l1*sin(theta1);
       0           0            1 0;
       0           0            0 1]
   
T23 = [cos(theta2) -sin(theta2) 0 l2*cos(theta2);
       sin(theta2) cos(theta2)  0 l2*sin(theta2);
       0           0            1 0;
       0           0            0 1]
   
T34 = [1 0 0 0;
       0 1 0 0;
       0 0 1 -h2;
       0 0 0 1]

T04 = simplify(T01*T12*T23*T34)
% T04 = T01*T12*T23*T34

% r = T04(1:3,1:3)
% m = rad2deg(tr2rpy(r,'zyx'))
