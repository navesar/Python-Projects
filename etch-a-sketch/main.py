from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():

    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_counter_clockwise():
    tim.left(10)


def move_clockwise():
    tim.right(10)


def clear_screen():
    screen.clear()
    tim.penup()
    tim.goto(0, 0)
    tim.pendown()


tim.speed("fastest")
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="A", fun=move_counter_clockwise)
screen.onkey(key="D", fun=move_clockwise)
screen.onkey(key="C", fun=clear_screen)


screen.exitonclick()
