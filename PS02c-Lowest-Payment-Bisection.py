def remainingPayment(balance, installment):
    for i in range(1,13):
        balance = (balance - installment)*(1+annualInterestRate/12.0)
    return balance

lowestPayment = balance/12
highestPayment = balance * ((1+annualInterestRate/12.0)**12)/12.0
installment = (lowestPayment + highestPayment)/2.0

while 1:
    installment = (lowestPayment + highestPayment)/2.0
    if remainingPayment(balance, installment) > 0.01:
        lowestPayment = installment
    elif remainingPayment(balance, installment) < 0:
        highestPayment = installment
    else:
        break
print 'Lowest Payment: ' + str(round(lowestPayment,2))
