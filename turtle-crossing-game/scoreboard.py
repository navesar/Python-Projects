from turtle import Turtle
FONT = ("Courier", 24, "normal")
POSITION = (-200, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.level = 0
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align="center", font=FONT)

