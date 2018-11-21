def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    count = 0
    for i in aDict.keys():
        count = count + len(aDict[i])
    return count
