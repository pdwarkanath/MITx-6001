"""
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of

Remaining balance: 813.4141998135 
So your program only prints out one thing: the remaining balance at the end of the year in the format:

Remaining balance: 4784.0
A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

We provide sample test cases below. We suggest you develop your code on your own machine, and make sure your code passes the sample test cases, before you paste it into the box below

"""

# Paste your code into this box


totalPaid = 0 #Initializing total paid amount for final printing
    
for i in range(1,13):                                                #from 1 to 12 for 12 months
    #print('Month: ' + str(i))                                         
    monthlyPaid = round(monthlyPaymentRate * balance,2)              
    totalPaid += monthlyPaid
    #print('Minimum monthly payment: ' + str(monthlyPaid))
    balance -= monthlyPaid
    balance = round(balance * (1 + annualInterestRate/12.0),2)       #Adding interest. Annual interest/12 = monthly interest
    #print('Remaining balance: ' + str(balance))
    
        
#print('Total paid: ' + str(totalPaid))
print('Remaining balance: ' + str(balance))
