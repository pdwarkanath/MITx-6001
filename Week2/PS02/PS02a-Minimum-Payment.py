# Paste your code into this box

totalPaid = 0 #Initializing total paid amount for final printing
    
for i in range(1,13):                                                #from 1 to 12 for 12 months
    print 'Month: ' + str(i)                                         
    monthlyPaid = round(monthlyPaymentRate * balance,2)              
    totalPaid += monthlyPaid
    print 'Minimum monthly payment: ' + str(monthlyPaid)
    balance -= monthlyPaid
    balance = round(balance * (1 + annualInterestRate/12.0),2)       #Adding interest. Annual interest/12 = monthly interest
    print 'Remaining balance: ' + str(balance)
    
        
print 'Total paid: ' + str(totalPaid)
print 'Remaining balance: ' + str(balance)
