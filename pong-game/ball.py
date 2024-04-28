from turtle import Turtle
STARTING_SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("blue")
        self.penup()
        self.y_direction = self.x_direction = STARTING_SPEED

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto((new_x, new_y))

    def y_bounce(self):
        self.y_direction *= -1

    def x_bounce(self):
        self.y_direction += 2 if self.y_direction > 0 else -2
        self.x_direction += 2 if self.x_direction > 0 else -2
        self.x_direction *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_direction = STARTING_SPEED if self.x_direction < 0 else -STARTING_SPEED
        self.y_direction = STARTING_SPEED
