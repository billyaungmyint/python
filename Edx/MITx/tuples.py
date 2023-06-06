t = (2 , 'One' , 3)
print(type(t))
print(t[0])
print()

#swapping tuples
x = 2
y = 4
print(str(x) + ',' + str(y))
(y ,x ) = (x , y)
print(str(x) + ',' + str(y))
print()

# or return a tuple from a function
def return_tuple(x,y) :
    return (y , x)

print(return_tuple(3,4))

