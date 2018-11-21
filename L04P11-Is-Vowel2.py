def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    char = char.lower()
    return char in ('a','e','i','o','u')
