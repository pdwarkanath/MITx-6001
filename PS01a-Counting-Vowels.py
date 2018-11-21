def countVowels(s):
    '''
    This function counts the number of vowels in a string
    s is a string of lower case characters
    '''
    
    count = 0  #Variable to keep count of number of variables in s
    vowels = ['a','e','i','o','u'] #List of vowels
    
    for i in s:                 #Looping through all characters in string s
        if i in vowels:         #Incrementing the count variable if character in s is a vowel
            count += 1          
    
    return count                

print 'Number of vowels: ' + str(countVowels(s))    #Printing out the result in the desired format by converting result of countVowels to string

