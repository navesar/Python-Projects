from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)