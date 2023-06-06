# Test Case 1:
# expected result
# Remaining balance: 31.38

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Test Case 2:
# Expected result
# Remaining balance: 361.61
# balance = 484
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
#
for i in range(12):
    monthlyInterestRate = annualInterestRate / 12.0
    minMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minMonthlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

print()
print('Remaining balance  : '  + str(round(balance,2)))
# for i in range(12):
#     monthlyInterestRate = annualInterestRate / 12.0
#     minimumMonthlyPayment = monthlyPaymentRate * balance
#     monthlyUnpaidBalance = balance - minimumMonthlyPayment
#     balance = round(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance) ,2)
#
# print('Remaining balance  : '  + str(balance))