def nfruits(fruitPattern,fruitString):
    if len(fruitString) == 1:
        biggestValue = 0
        for i in fruitPattern.keys():
            if i == fruitString:
                fruitPattern[i] -= 1
            if fruitPattern[i] >= biggestValue:
                biggestValue = fruitPattern[i]
        return biggestValue
    else:
        for i in fruitPattern.keys():
            if i == fruitString[0]:
                fruitPattern[i] -= 1
            else:
                fruitPattern[i] += 1
        return nfruits(fruitPattern, fruitString[1:])
