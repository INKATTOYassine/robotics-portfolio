""" 
This file contains functions related to kinematics calculations, for the 2d arm model.
The function : positions_function(theta1, theta2, l1, l2) computes the (x, y) positions of the joints and end-effector.
This function accepts radians only for angles and positive values for lengths, while negative angles are allowed.
The angles theta1 and theta2 are given in radians, and l1 and l2 are the lengths of the arm segments.
The conventions used are:
- The base of the arm is at the origin (0, 0).
- The main frame of reference is horizontal right as the positive x-axis and vertical up as the positive y-axis.
- theta1 is the angle of the first arm segment with respect to the horizontal axis.
- theta2 is the angle of the second arm segment with respect to the first arm segment.
- The function returns the positions of the first joint and the end-effector as tuples of (x, y) coordinates.
- If the input lengths are non-positive, a ValueError is raised.
"""

import math

def positions_function(theta1, theta2, l1, l2):
    """
    
    This function computes the (x, y) positions of the joints and end-effector.
    Args:
        theta1 (float): Angle of the first arm segment in radians.
        theta2 (float): Angle of the second arm segment in radians.
        l1 (float): Length of the first arm segment (must be positive).
        l2 (float): Length of the second arm segment (must be positive).
        
    Returns:
        tuple: A tuple containing two tuples:
            - (0, 0): Position of the base (origin).
            - (x1, y1): Position of the first joint.
            - (x2, y2): Position of the end-effector.
    Raises:
        ValueError: If l1 or l2 are non-positive.
        
    """

    if l1<=0 or l2<=0:
        raise ValueError("Lengths must be positive.")
        
    x1 = l1 * math.cos(theta1)
    y1 = l1 * math.sin(theta1)
    x2 = x1 + l2 * math.cos(theta1 + theta2)
    y2 = y1 + l2 * math.sin(theta1 + theta2)
    return ((0.0, 0.0), (x1, y1), (x2, y2))

