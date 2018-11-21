def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    
    oddTup = ()
    i = 0
    while i < len(aTup):
        if i%2 == 0:
            oddTup += (aTup[i],)
        i += 1
    return oddTup
            
