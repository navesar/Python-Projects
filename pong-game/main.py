from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time
# screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
# paddles and ball setup
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
# up and down functionality
screen.listen()
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)
screen.onkey(key="W", fun=left_paddle.up)
screen.onkey(key="S", fun=left_paddle.down)
# start the game
while scoreboard.l_score < 1 and scoreboard.r_score < 1:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # detect if the ball hit the wall and if so bounce from it
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_bounce()
    # detect if the ball hit a paddle and if so bounce from it
    if ((ball.distance(right_paddle) <= 50 and ball.xcor() >= 330 and ball.x_direction > 0) or  # right paddle
            (ball.distance(left_paddle) <= 50 and ball.xcor() <= -330 and ball.x_direction < 0)):  # left paddle
        ball.x_bounce()
    elif ball.xcor() > 375:
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() < -375:
        ball.reset_position()
        scoreboard.r_point()
scoreboard.game_over()
screen.exitonclick()
