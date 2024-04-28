from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
R_POSITION = (100, 180)
L_POSITION = (-R_POSITION[0], R_POSITION[1])


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.speed("fastest")
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(L_POSITION)
        self.write(arg=f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(R_POSITION)
        self.write(arg=f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.write_score()

    def r_point(self):
        self.r_score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"   Game Over!\n{"right player" if self.r_score > self.l_score else "left player"} wins!",
                   align=ALIGNMENT, font=("Courier", 20, "normal"))

