def remainingPayment(balance, lowestPayment):
    for i in range(1,13):
        balance = (balance - lowestPayment)*(1+annualInterestRate/12.0)
    return balance

lowestPayment = 10

while remainingPayment(balance, lowestPayment) > 0:
    lowestPayment += 10

print 'Lowest Payment: ' + str(lowestPayment)
