def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    h = len(aStr)
    l = 0
    if aStr == "":
        return False
    elif len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[(l+h)/2]:
        return True
    else:
        if char < aStr[(l+h)/2]:
            h = (l+h)/2
        if char > aStr[(l+h)/2]:
            l = (l+h)/2+1
        return isIn(char,aStr[l:h])
