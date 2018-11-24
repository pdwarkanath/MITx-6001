"""
Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other element of the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').

"""

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
            
