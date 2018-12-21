def ndigits(x):
    if abs(x) < 10:
        return 1
    else:
        return ndigits(abs(x)/10) + 1


# Random comment to check
