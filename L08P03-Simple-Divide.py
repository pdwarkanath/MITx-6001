#define the SimpleDivide function here
def SimpleDivide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError, e:
        return 0
