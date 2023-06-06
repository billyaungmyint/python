# Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    monthlyInterestRate = annualInterestRate / 12.0
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = round(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance) ,2)

print('Remaining balance  : '  + str(balance))
