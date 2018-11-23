"""
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: n*s^2/4tan(pi/n)
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
"""


import math
def polysum(n,s):
    '''
    This function calculates the sum of perimeter squared and the area of a regular polygon with n sides of length s each
    n is an integer
    s is a float
    '''
    perimeterSquared = (n*s)**2 #calculate perimeter = number of sides * length of side. Taking square of this perimeter
    area = (0.25*n*(s**2))/(math.tan(math.pi/n)) #calculate area using the formula area = (0.25*n*s^2)/tan(pi/n)
    return round(perimeterSquared + area,4) #round upto 4 decimals
