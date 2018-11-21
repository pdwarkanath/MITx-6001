
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
