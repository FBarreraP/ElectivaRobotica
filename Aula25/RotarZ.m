function [Rz] = RotarZ(theta)
Rz=[cos(theta) -sin(theta) 0;
    sin(theta) cos(theta) 0;
    0 0 1];
end