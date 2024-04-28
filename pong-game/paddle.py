from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__(shape="square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(starting_position)

    def up(self):
        self.forward(20) if self.ycor() < 240 else None

    def down(self):
        self.backward(20) if self.ycor() > -240 else None
