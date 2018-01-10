# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from math import atan2
from .geometry import distance, getNewCoordinates, getTriangleSides, isOnLeft, isOnRight

def eqBalance(p0, p1, p2, p3):
    # check angles of the bcps
    # in-point BCPs will report angle = 0
    alpha = atan2(p1.y - p0.y, p1.x - p0.x)
    beta  = atan2(p2.y - p3.y, p2.x - p3.x)
    if abs(alpha - beta) >= 0.7853981633974483: # 45°
        # check if both handles are on the same side of the curve
        if isOnLeft(p0, p3, p1) and isOnLeft(p0, p3, p2) or isOnRight(p0, p3, p1) and isOnRight(p0, p3, p2):
            a, b, c = getTriangleSides(p0, p1, p2, p3)
            
            # Calculate current handle lengths as percentage of triangle side length
            ca = distance(p3, p2) / a
            cc = distance(p0, p1) / c
            
            # Make new handle length the average of both handle lenghts
            handle_percentage = (ca + cc) / 2
            
            # Scale triangle sides a and c by requested handle length
            a = a * handle_percentage
            c = c * handle_percentage
            
            # move first control point
            p1.x, p1.y = getNewCoordinates(p1, p0, p2, c)
            
            # move second control point
            p2.x, p2.y = getNewCoordinates(p2, p3, p1, a)
    
    return p1, p2

