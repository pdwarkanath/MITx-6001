"""

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5

"""


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

print('Number of vowels: ' + str(countVowels(s)))   #Printing out the result in the desired format by converting result of countVowels to string

