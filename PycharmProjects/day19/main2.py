from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def rotate_counterclockwise():
    tim.left(10)


def rotate_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


# or

# def rotate_clockwise():
#    tim.right(10)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="W", fun=move_forward)
screen.onkey(key="S", fun=move_backward)
screen.onkey(key="A", fun=rotate_counterclockwise)
screen.onkey(key="D", fun=rotate_clockwise)
# screen.onkey(key="C", fun=clear_drawing)
screen.onkey(clear_drawing, "C")

screen.exitonclick()
