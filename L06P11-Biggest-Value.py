def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    result = None
    biggestValue = 0
    for i in aDict.keys():
        if len(aDict[i]) >= biggestValue:
            biggestValue = len(aDict[i])
            result = i
    return result
