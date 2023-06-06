class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_square = (self.x - other.x) ** 2
        y_diff_square = (self.y - other.y) ** 2
        return (x_diff_square + y_diff_square) ** 0.5

    # here __str__ override the parent's __str_ method to include < >
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"


c = Coordinate(3, 4)
origin = Coordinate(0, 0)

print(c.x)
print(origin.x)
print(c.distance(origin))
# these two retuns the same but the below call the class and above calls the instance
print(Coordinate.distance(c, origin))
# here str from parent class is overridden by subclass
print(c)


class Clock(object):
    def __init__(self, time):
        self.time = time

    def print_time(self):
        time = '6:30'
        print(self.time)


clock = Clock('5:30')
clock.print_time()

print("5")
print(5)

print()


class Weird(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def getX(self):
        return x

    def getY(self):
        return y


class Wild(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def getX(self):
        return self.x

    def getY(self):
        return self.y


X = 7
Y = 8
w1 = Weird(X, Y)
#print(w1.getX())

w2 = Wild(X, Y)
print(w2.getX())

w3 = Wild(17, 18)
print(w3.getX())