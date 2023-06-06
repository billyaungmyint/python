def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")

#fancy_divide([0, 2, 4], 1)
#fancy_divide([0, 2, 4], 4)
fancy_divide([0, 2, 4], 0)