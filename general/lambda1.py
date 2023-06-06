f1 = lambda x:x
print(f1(2))
print()

f2 = lambda x,y:x+y
print(f2(2,4))
print()

f3 = lambda x,y: 'factor' if (x%y) == 0 else 'not a factor'
print(f3(4,2))
print(f3(4,3))