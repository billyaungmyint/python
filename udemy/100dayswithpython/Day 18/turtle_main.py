from turtle import Turtle , Screen

tim = Turtle()

# change to turtle shape
# https://docs.python.org/3/library/turtle.html#turtle.shape
tim.shape('turtle')
# https://docs.python.org/3/library/turtle.html#turtle.color
# https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html
# https://trinket.io/docs/colors
tim.color('red')

# https://docs.python.org/3/library/turtle.html#turtle.forward
tim.forward(100)
i=0

while i < 3:
    tim.right(90)
    tim.forward(100)
    i += 1


screen = Screen()
screen.exitonclick()