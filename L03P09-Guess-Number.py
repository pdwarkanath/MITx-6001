# Paste your code into this box

print 'Please think of a number between 0 and 100!'
low = 0
high = 100
while 1:
    print 'Is your secret number ' + str((high + low)/2) + '?'
    x = str(raw_input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. '))
    
    if x == 'h':
        high = (high + low)/2
    elif x == 'l':
        low = (high + low)/2
    elif x == 'c':
        break
    else:
        print 'Sorry, I did not understand your input.'

print 'Game over. Your secret number was: ' + str((high + low)/2)
