def func_a() :
    print('inside function a')


def func_b(y) :
    print('inside function b')
    return y


def func_c(z) :
    print('inside function c')
    return z()


print(func_a())
print(5 + func_b(2))
print(func_c(func_a))

