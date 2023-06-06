# using range to find the sum of even numbers fom 1 - 100

total = 0

for number in range(1,101):
    if number % 2 == 0:
        total += number

print(total)

