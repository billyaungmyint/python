def fancy_divide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("fdjdfjkfd")
    except Exception as ex:
        print(ex)

fancy_divide([0, 2, 4], 0)

def simple_divide(item, denom):
    try :
        item / denom
    except ZeroDivisionError :
        return 0