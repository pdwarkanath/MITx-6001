def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    result = min(a,b)
    while max(a,b)%result != 0 or min(a,b)%result !=0:
        result = result - 1
    return result
