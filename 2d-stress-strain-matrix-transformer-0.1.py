# -*- coding: utf-8 -*-
""" 2D Stress / Strain Matrix Transformer
    Version 0.1
    @author: Ryan Fung
    Create Date: 2013-12-06
"""

from math import cos as cos
from math import sin as sin
from math import radians
from numpy import dot
from numpy import array as array


def matrix_transform(matrix, angle):
    """Given a list 'matrix' in the form [xx,yy,xy] corresponding to the three
    components of stress or strain matrix, and an angle in degrees to rotate
    the stress or strain values by, compute and return the transformed values
    as an array.
    / xx' \   /   cos²θ      sin²θ       2cosθsinθ  \   / xx \
    | yy' | = |   sin²θ      cos²θ      -2cosθsinθ  | × | yy |
    \ xy' /   \ -cosθsinθ   cosθsinθ    cos²θ-sin²θ /   \ xy /
    """
    if len(matrix) != 3:
        raise ValueError("Matrix must be a list with 3 values.")
    if type(angle) not in [int, float, long]:
        raise ValueError("Angle must be a number.")
    c = cos(radians(angle))
    s = sin(radians(angle))
    coeffs = array([[c*c,  s*s, 2*c*s],
                   [s*s,  c*c, -2*c*s],
                   [-c*s, c*s, (c*c)-(s*s)]])
    matrixarray = array([[matrix[0]],
                         [matrix[1]],
                         [matrix[2]]])
    return dot(coeffs, matrixarray)
