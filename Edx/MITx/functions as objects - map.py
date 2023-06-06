def applyToEach(L ,f) :
    """"
    :param L: a List
    :param f: a Function
    :return: none
    """
    for i in range(len(L)):
        L[i] = f(L[i])

L = [1,-2,3.4]
print(f"Original values of L is : {L}")
applyToEach(L , abs)
print(f"After calling applyToEach(L,abs) : {L}")
applyToEach(L , int)
print(f"After calling applyToEach(L,int) : {L}")

def applyFuns(L , x) :
    """
    :param L: a List of functions to apply to x
    :param x: a value which the list of functions to apply to
    :return: none
    """
    for f in L :
        print(f(x))


print(applyFuns([abs, int], 4.9))
print()

# using map
# R has apply
for elt in map(abs , [1,-2,4,5.5]) :
    print(elt)