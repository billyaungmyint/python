balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12.0
monthlyPaymentLowerBound = balance / 12
monthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate) * 12) / 12.0

guessMinimum = (monthlyPaymentLowerBound + monthlyPaymentUpperBound)/2
remain = balance
precision = 0.10

while remain >= precision:

    guessMinimum = (monthlyPaymentLowerBound + monthlyPaymentUpperBound)/2

    for i in range (12):
        newBalance = remain - guessMinimum
        monthlyInterestRate = annualInterestRate/ 12 * newBalance
        remain = newBalance+monthlyInterestRate

    if remain < 0:
        monthlyPaymentUpperBound = guessMinimum
        remain = balance

    elif remain > precision:
        monthlyPaymentLowerBound = guessMinimum
        remain = balance

guessMinimum = round(guessMinimum , 2)
print("Lowest Payment : " + str(guessMinimum))