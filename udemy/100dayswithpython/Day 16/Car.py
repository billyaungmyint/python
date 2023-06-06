class Car():
    def __init__(self,colour,speed):
        self.colour = colour
        self.speed = speed

    def setColour(self,colour):
        self.colour = colour

    def getColour(self):
        return self.colour


car1 = Car("Blue", 200)
car1.setColour("Black")


print(car1.speed)
print(car1.colour)