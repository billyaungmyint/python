x = int(input())
y = 0

while x % 4 == 0 and x % 10 == 8:
        if x != 0:
            y = x + y
            x = int(input())
        break
        print(y)
else:
    break