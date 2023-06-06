import math

def polysum(n,s) :
    area = (0.25 * n * (s ** 2)) / math.tan(math.pi / n)
    parameter = n * s
    ans = area + (parameter * parameter)
    return round(ans , 4)

