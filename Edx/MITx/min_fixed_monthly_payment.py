balance = 3926
annualInterestRate = 0.2

# expected result
# Lowest Payment: 310
# minFixedMonthlyPayment = 10
#
# while balance > 0 :
#     monthlyInterestRate = annualInterestRate / 12.0
#     monthlyUnpaidBalance = balance - minFixedMonthlyPayment
#     balance = monthlyUnpaidBalance + (monthlyInterestRate * balance)
#     minFixedMonthlyPayment += 10
#
# print('Lowest payment : ' + str(minFixedMonthlyPayment))

monthlyPayment = 0
monthlyInterestRate = annualInterestRate /12
newbalance = balance
month = 0

while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance

    for month in range(1,13):
        newbalance -= monthlyPayment
        newbalance += monthlyInterestRate * newbalance
        month += 1
print ("Lowest Payment:" + str(monthlyPayment))