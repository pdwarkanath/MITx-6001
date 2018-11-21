def countBob(s):
    '''
    This function counts the number of times the term 'bob' appears in a string s
    s is a string of lower case characters
    '''
    count = 0                     #Initializing count of 'bob's to zero
    
    for i in range(len(s)-1):     #i goes from 0 to one less than length of string s
        if s[i:i+3] == 'bob':     #Checking three characters starting from i if they equal 'bob'
            count += 1
    
    return count

print 'Number of times bob occurs is: ' + str(countBob(s)) #Printing the desired output by converting count to a string
